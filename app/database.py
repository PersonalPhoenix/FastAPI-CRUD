from sqlalchemy.orm import (
    sessionmaker,
)
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
)

from app.config import (
    settings,
)


engine = create_async_engine(url=settings.get_database_url)
async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
