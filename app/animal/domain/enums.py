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

    ALIVE: int = 1
    SOLD: int = 2
    UNKNOW: int = 3


class AnimalSexEnum(BaseEnumerate):
    """Перечилесние полов животного."""

    MALE: int = 1
    FEMALE: int = 2
