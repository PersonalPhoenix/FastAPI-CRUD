from decimal import (
    Decimal,
)
from typing import (
    Optional,
)
from pydantic import (
    BaseModel,
)
from app.animal.domain.enums import (
    AnimalStatusEnum,
    AnimalSexEnum,
)


class AnimalsScheme(BaseModel):

    nick_name: str
    status: AnimalStatusEnum
    weight: Decimal
    sex: Optional[AnimalSexEnum] = None
