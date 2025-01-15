from sqlalchemy import (
    Column,
    DECIMAL,
    Enum,
    String,
)

from app.animal.main_models import (
    BaseModel,
)
from app.animal.domain.enums import (
    AnimalSexEnum,
    AnimalStatusEnum,
)


class Animals(BaseModel):
    """Модель животного."""

    __tablename__ = 'Animals'

    nick_name = Column(
        name='nick_name', 
        type_=String, 
        nullable=False,
    )

    status = Column(
        name='status', 
        type_=Enum(AnimalStatusEnum), 
        nullable=False,
    )

    weight = Column(
        name='weight', 
        type_=DECIMAL(precision=6, scale=2), 
        nullable=False,
    )

    sex = Column(
        name='sex', 
        type_=Enum(AnimalSexEnum), 
        nullable=True,
    )
