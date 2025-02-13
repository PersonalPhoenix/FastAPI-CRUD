import pytest

from httpx import (
    AsyncClient,
)

from app.config import (
    settings,
)


@pytest.mark.anyio
@pytest.fixture
async def async_animals_client():
    base_url=f'{settings.BASE_API_URL}{settings.DEFAULT_URL_PREFIX}{settings.ANIMAL_PREFIX}'
    async with AsyncClient(base_url=base_url) as async_animals_client:
        yield async_animals_client
