import pytest

from pydantic import (
    ValidationError,
)
from fastapi import (
    status,
)

from httpx import (
    AsyncClient,
)

from app.animal.schemas.animals_schemas import (
    AnimalsScheme,
)


@pytest.mark.asyncio
async def test_animals_get_by_id(async_animals_client: AsyncClient):
    path = 'get-by-id'

    response = await async_animals_client.get(
        url=f'{async_animals_client.base_url}{path}',
        params={
            'obj_id': 1,
        },
    )

    assert response.status_code == status.HTTP_200_OK

    try:
        AnimalsScheme.model_validate(response.json())
    except ValidationError as error:
        pytest.fail(f'Response does not match schema: {error}')


@pytest.mark.asyncio
async def test_animals_get_by_ids(async_animals_client: AsyncClient):
    path = 'get-by-ids'

    response = await async_animals_client.get(
        url=f'{async_animals_client.base_url}{path}',
        params={
            'ids': [1, 2, 3],
        },
    )
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response_data, list)

    try:
        map(AnimalsScheme.model_validate, response_data)
    except ValidationError as error:
        pytest.fail(f'Response does not match schema: {error}')


@pytest.mark.asyncio
async def test_animals_get_all(async_animals_client: AsyncClient):
    path = 'get-all'
    response = await async_animals_client.get(
        url=f'{async_animals_client.base_url}{path}',
    )
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response_data, list)

    try:
        map(AnimalsScheme.model_validate, response_data)
    except ValidationError as error:
        pytest.fail(f'Response does not match schema: {error}')
