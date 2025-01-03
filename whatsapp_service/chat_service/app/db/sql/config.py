from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.base_settings import settings  # Import the settings from the config module

# Async engine library settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

# Define the database URL using SQLAlchemy with MySQL and the settings from Pydantic BaseSettings

# DATABASE_URL = f"mysql+pymysql://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}@{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/{settings.MYSQL_DATABASE}"



# SQLAlchemy setup (synchronous)
# engine = create_engine(DATABASE_URL, pool_pre_ping=True)
# ENGINE TO HAE AND CREATE POOLS RAHTER THEN USING  AGAIN
# engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# # Dependency to get the DB session (synchronous method)
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()  # Ensure the session is closed after use


# AYNC SETUP FOR SB LIBRARY WITHI AIOMYSQL
# Async database URL (use asyncpg or aiomysql depending on the DB)
DATABASE_URL = f"mysql+aiomysql://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}@{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/{settings.MYSQL_DATABASE}"

# Async Engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Async session
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

# Dependency to get DB session (asynchronous method)
async def get_db():
    async with SessionLocal() as db:
        yield db

