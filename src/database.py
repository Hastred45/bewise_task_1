from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from config import (DB_HOST, DB_PORT, POSTGRES_DB, POSTGRES_PASSWORD,
                    POSTGRES_USER)


DB_URL = (f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@'
          f'{DB_HOST}:{DB_PORT}/{POSTGRES_DB}')

engine = create_async_engine(DB_URL)
SessionLocal = sessionmaker(engine, class_=AsyncSession)
