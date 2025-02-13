from datetime import (
    datetime,
)

from sqlalchemy import (
    DateTime,
    func,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)


class BaseModel(DeclarativeBase):
    """Базовая модель для миграций."""

    id: Mapped[int] = mapped_column( 
        primary_key=True, 
        autoincrement=True, 
        nullable=False,
        unique=True,
    )
    created: Mapped[datetime] = mapped_column(
        type_=DateTime(
            timezone=True,
        ),
        default=func.now(),
        nullable=False,
    )
    modified: Mapped[datetime] = mapped_column(
        type_=DateTime(
            timezone=True,
        ),
        default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
