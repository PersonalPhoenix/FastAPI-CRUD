from sqlalchemy import (
    DECIMAL,
    Enum,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.animal.domain.enums import (
    AnimalSexEnum,
    AnimalStatusEnum,
)
from app.animal.main_models import (
    BaseModel,
)


class Animals(BaseModel):
    """Модель животного."""

    __tablename__ = 'animals'

    nick_name: Mapped[str] = mapped_column(
        type_=String(
            length=25,
        ),
        nullable=False,
    )

    status: Mapped[AnimalStatusEnum] = mapped_column(
        type_=Enum(AnimalStatusEnum), 
        nullable=False,
    )

    weight: Mapped[DECIMAL] = mapped_column(
        type_=DECIMAL(
            precision=6, 
            scale=2,
        ), 
        nullable=False,
    )

    sex: Mapped[AnimalSexEnum] = mapped_column(
        type_=Enum(AnimalSexEnum), 
        nullable=False,
    )
