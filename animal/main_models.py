from sqlalchemy import (
    Column,
    Integer,
)
from sqlalchemy.orm import (
    DeclarativeBase,
)


class BaseModel(DeclarativeBase):
    """Базовая модель для миграций."""

    id = Column(
        name='id', 
        type_=Integer, 
        primary_key=True, 
        autoincrement=True, 
        nullable=False,
    )
