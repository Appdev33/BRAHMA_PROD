"""Production-oriented CRUD API with Redis cache protection.

Run:
  pip install fastapi uvicorn redis
  uvicorn cache_crud_api:app --reload
"""

import asyncio
import json
import os
import random
import sqlite3
import time
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException, Query, Response, status
from pydantic import BaseModel, Field

try:
    from redis.asyncio import Redis
except ImportError:  # Allows health checks and tests without Redis installed.
    Redis = None

DB_PATH = os.getenv("DATABASE_PATH", "cache_crud.db")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
CACHE_TTL = int(os.getenv("CACHE_TTL_SECONDS", "60"))
NEGATIVE_TTL = int(os.getenv("NEGATIVE_CACHE_TTL_SECONDS", "10"))
LOCK_TTL = 5
MAX_PAGE_SIZE = 100


class ItemIn(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    description: str = Field(default="", max_length=5000)


class Item(ItemIn):
    id: UUID
    created_at: datetime
    updated_at: datetime


class Page(BaseModel):
    items: list[Item]
    limit: int
    offset: int


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def connect() -> sqlite3.Connection:
    db = sqlite3.connect(DB_PATH, timeout=10)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA journal_mode=WAL")
    db.execute("PRAGMA busy_timeout=10000")
    return db


def init_db() -> None:
    with connect() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)


def row_item(row: sqlite3.Row | None) -> Item | None:
    if row is None:
        return None
    return Item(**dict(row))


def db_get(item_id: str) -> Item | None:
    with connect() as db:
        return row_item(db.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone())


def db_list(limit: int, offset: int) -> list[Item]:
    with connect() as db:
        rows = db.execute(
            "SELECT * FROM items ORDER BY created_at DESC LIMIT ? OFFSET ?", (limit, offset)
        ).fetchall()
    return [row_item(row) for row in rows]


def db_create(data: ItemIn) -> Item:
    item = Item(id=uuid4(), created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc), **data.model_dump())
    with connect() as db:
        db.execute("INSERT INTO items VALUES (?, ?, ?, ?, ?)",
                   (str(item.id), item.name, item.description,
                    item.created_at.isoformat(), item.updated_at.isoformat()))
    return item


def db_update(item_id: str, data: ItemIn) -> Item | None:
    updated = datetime.now(timezone.utc)
    with connect() as db:
        result = db.execute(
            "UPDATE items SET name = ?, description = ?, updated_at = ? WHERE id = ?",
            (data.name, data.description, updated.isoformat(), item_id),
        )
        if result.rowcount == 0:
            return None
    return db_get(item_id)


def db_delete(item_id: str) -> bool:
    with connect() as db:
        result = db.execute("DELETE FROM items WHERE id = ?", (item_id,))
    return result.rowcount > 0


class Cache:
    def __init__(self) -> None:
        self.redis: Any = None
        self.local_locks: dict[str, asyncio.Lock] = {}

    async def connect(self) -> None:
        if Redis:
            self.redis = Redis.from_url(REDIS_URL, decode_responses=True,
                                        socket_connect_timeout=1, socket_timeout=1)
            try:
                await self.redis.ping()
            except Exception:
                await self.redis.aclose()
                self.redis = None

    async def close(self) -> None:
        if self.redis:
            await self.redis.aclose()

    async def get(self, key: str) -> Any:
        if not self.redis:
            return None
        try:
            value = await self.redis.get(key)
            return None if value is None else json.loads(value)
        except Exception:
            return None

    async def set(self, key: str, value: Any, ttl: int = CACHE_TTL) -> None:
        if self.redis:
            try:
                await self.redis.set(key, json.dumps(value), ex=max(1, ttl + random.randint(0, 10)))
            except Exception:
                pass

    async def delete(self, *keys: str) -> None:
        if self.redis:
            try:
                await self.redis.delete(*keys)
            except Exception:
                pass

    async def clear_lists(self) -> None:
        if self.redis:
            try:
                keys = [key async for key in self.redis.scan_iter("items:*")]
                if keys:
                    await self.redis.delete(*keys)
            except Exception:
                pass

    async def lock(self, key: str) -> bool:
        if not self.redis:
            lock = self.local_locks.setdefault(key, asyncio.Lock())
            return not lock.locked()
        try:
            return bool(await self.redis.set(key, "1", nx=True, ex=LOCK_TTL))
        except Exception:
            return False

    async def unlock(self, key: str) -> None:
        if self.redis:
            try:
                await self.redis.delete(key)
            except Exception:
                pass


cache = Cache()


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    await cache.connect()
    yield
    await cache.close()


app = FastAPI(title="Cache-safe CRUD API", version="1.0.0", lifespan=lifespan)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "cache": "redis" if cache.redis else "fallback"}


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(data: ItemIn) -> Item:
    item = await asyncio.to_thread(db_create, data)
    await cache.set(f"item:{item.id}", item.model_dump(mode="json"))
    await cache.clear_lists()
    return item


@app.get("/items", response_model=Page)
async def list_items(
    limit: int = Query(20, ge=1, le=MAX_PAGE_SIZE),
    offset: int = Query(0, ge=0),
) -> Page:
    key = f"items:{limit}:{offset}"
    cached = await cache.get(key)
    if cached:
        return Page(**cached)
    page = Page(items=await asyncio.to_thread(db_list, limit, offset), limit=limit, offset=offset)
    await cache.set(key, page.model_dump(mode="json"), ttl=15)
    return page


@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: UUID) -> Item:
    key = f"item:{item_id}"
    cached = await cache.get(key)
    if cached == {"missing": True}:
        raise HTTPException(404, "Item not found")
    if cached:
        return Item(**cached)

    lock_key = f"lock:{key}"
    if await cache.lock(lock_key):
        try:
            item = await asyncio.to_thread(db_get, str(item_id))
            if item is None:
                await cache.set(key, {"missing": True}, NEGATIVE_TTL)
                raise HTTPException(404, "Item not found")
            await cache.set(key, item.model_dump(mode="json"))
            return item
        finally:
            await cache.unlock(lock_key)

    await asyncio.sleep(0.03)
    cached = await cache.get(key)
    if cached and cached != {"missing": True}:
        return Item(**cached)
    item = await asyncio.to_thread(db_get, str(item_id))
    if item is None:
        await cache.set(key, {"missing": True}, NEGATIVE_TTL)
        raise HTTPException(404, "Item not found")
    return item


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: UUID, data: ItemIn) -> Item:
    item = await asyncio.to_thread(db_update, str(item_id), data)
    if item is None:
        raise HTTPException(404, "Item not found")
    await cache.delete(f"item:{item_id}")
    await cache.clear_lists()
    return item


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: UUID) -> Response:
    if not await asyncio.to_thread(db_delete, str(item_id)):
        raise HTTPException(404, "Item not found")
    await cache.delete(f"item:{item_id}")
    await cache.clear_lists()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
