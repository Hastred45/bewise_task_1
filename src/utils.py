from typing import AsyncGenerator
from fastapi import HTTPException
from sqlalchemy.exc import OperationalError

from src.database import SessionLocal


async def check_db() -> AsyncGenerator:
    try:
        async with SessionLocal() as session:
            yield session
    except OperationalError as e:
        raise HTTPException(
            status_code=503,
            detail=f'Server closed the connection unexpectedly: {e}'
        )
