from contextlib import asynccontextmanager
from datetime import datetime, timezone
import json
import random
from typing import AsyncIterator
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException, Query, Response, status
from pydantic import BaseModel, ConfigDict, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from redis.asyncio import Redis
from sqlalchemy import DateTime, String, Text, delete, select
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    app_name: str = "Scalable CRUD API"
    database_url: str = "postgresql+asyncpg://app:app@localhost:5432/app"
    redis_url: str = "redis://localhost:6379/0"
    cache_ttl_seconds: int = 60
    negative_cache_ttl_seconds: int = 10
    max_page_size: int = 100


settings = Settings()


class Base(DeclarativeBase):
    pass


class ItemRow(Base):
    __tablename__ = "items"

    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


class ItemIn(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    description: str = Field(default="", max_length=5000)


class ItemOut(ItemIn):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    created_at: datetime
    updated_at: datetime


class ItemPage(BaseModel):
    items: list[ItemOut]
    limit: int
    offset: int


class AppState:
    engine = None
    sessions = None
    redis: Redis | None = None


state = AppState()


@asynccontextmanager
async def lifespan(_: FastAPI):
    state.engine = create_async_engine(
        settings.database_url,
        pool_pre_ping=True,
        pool_size=20,
        max_overflow=20,
        pool_recycle=1800,
    )
    state.sessions = async_sessionmaker(state.engine, expire_on_commit=False)
    state.redis = Redis.from_url(settings.redis_url, decode_responses=True,
                                 socket_connect_timeout=1, socket_timeout=1)
    try:
        await state.redis.ping()
    except Exception:
        await state.redis.aclose()
        state.redis = None
    async with state.engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield
    if state.redis:
        await state.redis.aclose()
    await state.engine.dispose()


app = FastAPI(title=settings.app_name, version="1.0.0", lifespan=lifespan)


def cache_key(item_id: UUID) -> str:
    return f"item:{item_id}"


async def cache_get(key: str):
    if not state.redis:
        return None
    try:
        value = await state.redis.get(key)
        return None if value is None else json.loads(value)
    except Exception:
        return None


async def cache_set(key: str, value: object, ttl: int = settings.cache_ttl_seconds) -> None:
    if not state.redis:
        return
    try:
        await state.redis.set(key, json.dumps(value, default=str), ex=ttl + random.randint(0, 10))
    except Exception:
        pass


async def cache_delete(*keys: str) -> None:
    if not state.redis:
        return
    try:
        await state.redis.delete(*keys)
    except Exception:
        pass


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "cache": "redis" if state.redis else "database-only"}


@app.post("/v1/items", response_model=ItemOut, status_code=status.HTTP_201_CREATED)
async def create_item(payload: ItemIn) -> ItemRow:
    now = datetime.now(timezone.utc)
    item = ItemRow(created_at=now, updated_at=now, **payload.model_dump())
    async with state.sessions() as session:
        session.add(item)
        await session.commit()
        await session.refresh(item)
    await cache_delete("items:list")
    return item


@app.get("/v1/items", response_model=ItemPage)
async def list_items(
    limit: int = Query(20, ge=1),
    offset: int = Query(0, ge=0),
) -> ItemPage:
    limit = min(limit, settings.max_page_size)
    async with state.sessions() as session:
        result = await session.execute(
            select(ItemRow).order_by(ItemRow.created_at.desc()).limit(limit).offset(offset)
        )
        items = list(result.scalars().all())
    return ItemPage(items=items, limit=limit, offset=offset)


@app.get("/v1/items/{item_id}", response_model=ItemOut)
async def get_item(item_id: UUID) -> ItemRow:
    cached = await cache_get(cache_key(item_id))
    if cached == {"missing": True}:
        raise HTTPException(status_code=404, detail="Item not found")
    if cached:
        return ItemOut(**cached)

    async with state.sessions() as session:
        item = await session.get(ItemRow, item_id)
    if item is None:
        await cache_set(cache_key(item_id), {"missing": True}, settings.negative_cache_ttl_seconds)
        raise HTTPException(status_code=404, detail="Item not found")
    await cache_set(cache_key(item_id), ItemOut.model_validate(item).model_dump(mode="json"))
    return item


@app.put("/v1/items/{item_id}", response_model=ItemOut)
async def update_item(item_id: UUID, payload: ItemIn) -> ItemRow:
    async with state.sessions() as session:
        item = await session.get(ItemRow, item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        item.name = payload.name
        item.description = payload.description
        item.updated_at = datetime.now(timezone.utc)
        await session.commit()
        await session.refresh(item)
    await cache_delete(cache_key(item_id), "items:list")
    return item


@app.delete("/v1/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: UUID) -> Response:
    async with state.sessions() as session:
        result = await session.execute(delete(ItemRow).where(ItemRow.id == item_id))
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Item not found")
        await session.commit()
    await cache_delete(cache_key(item_id), "items:list")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
