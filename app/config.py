from pydantic_settings import (
    BaseSettings,
)


class ProjectSettings(BaseSettings):
    """Класс настроек проекта."""

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    ENGINE: str
    TYPE: str

    DEFAULT_URL_PREFIX: str

    BASE_API_URL: str

    ANIMAL_PREFIX: str
    ANIMAL_TAG: str

    @property
    def get_database_url(cls) -> str:
        """Формирует из возвращает Database URL."""

        database_url = (
            f'{cls.ENGINE}+{cls.TYPE}://{cls.DB_USER}:'
            f'{cls.DB_PASS}@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}'
        )

        return database_url

    class Config:
        env_file = '.env'


settings = ProjectSettings()
