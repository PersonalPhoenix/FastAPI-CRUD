import pytest

from httpx import (
    AsyncClient,
    ASGITransport,
)

from app.main import (
    app,
)
from app.config import (
    settings,
)


@pytest.fixture
async def async_animals_client():
    base_url = 'http://test' + settings.DEFAULT_URL_PREFIX_API_V1
    client = AsyncClient(transport=ASGITransport(app=app), base_url=base_url)

    async with client as async_animals_client:
        yield async_animals_client


@pytest.fixture
async def async_animal_prefix():
    return settings.ANIMAL_PREFIX
