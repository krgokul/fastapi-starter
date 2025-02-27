"""
This file has the code to create a connection with the database.
"""
import os

from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from dotenv import load_dotenv

load_dotenv()

# Load environment-specific configurations
ENV = os.environ.get("ENV", "dev").lower()
# Database configuration
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

# Construct the database connection string
conn_string = (
    f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
# Create SQLAlchemy engine and session
engine = create_async_engine(
    conn_string,
    future=True,
    echo=True,
)

AsyncSessionFactory = async_sessionmaker(
    engine, autoflush=False, expire_on_commit=False
)


async def get_db() -> AsyncGenerator:
    async with AsyncSessionFactory() as session:
        try:
            yield session
        except Exception as e:
            raise
