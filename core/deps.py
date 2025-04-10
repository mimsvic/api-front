from sqlalchemy.ext.asyncio import AsyncSession
from core.database import SessionLocal
from typing import AsyncGenerator

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    session: AsyncSession = SessionLocal()
    try:
        yield session
    finally:
        await session.close()
