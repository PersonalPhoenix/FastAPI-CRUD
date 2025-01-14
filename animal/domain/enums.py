from enum import (
    Enum,
)


class BaseEnumerate(Enum):
    """Базовый класс для Enum'ов."""

    @classmethod
    def get_choices(cls) -> list[tuple]:
        return [(status.value, status.name) for status in cls]


class AnimalStatusEnum(BaseEnumerate):
    """Перечилесние статусов животного."""

    ALIVE = 1
    SOLD = 2
    UNKNOW = 3


class AnimalSexEnum(BaseEnumerate):
    """Перечилесние полов животного."""

    MALE = 1
    FEMALE = 2
