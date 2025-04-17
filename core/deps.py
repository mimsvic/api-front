from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session
from typing import AsyncGenerator, Generator

async def get_session() -> Generator: #AsyncGenerator[AsyncSession, None]:
    session: AsyncSession = Session()
    try:
        yield session
    finally:
        await session.close()
