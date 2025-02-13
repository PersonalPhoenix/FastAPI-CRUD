from decimal import (
    Decimal,
)

from pydantic import (
    BaseModel,
    Field,
)

from app.animal.domain.enums import (
    AnimalSexEnum,
    AnimalStatusEnum,
)


class AnimalsScheme(BaseModel):
    """Pydantic схема животного."""

    nick_name: str
    status: AnimalStatusEnum
    weight: Decimal
    sex: AnimalSexEnum
