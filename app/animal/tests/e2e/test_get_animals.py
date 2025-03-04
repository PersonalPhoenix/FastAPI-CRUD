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


async def test_get_animal_by_id(async_animals_client: AsyncClient, async_animal_prefix: str):

    response = await async_animals_client.get(
        url=async_animal_prefix+'/get-by-id',
        params={
            'obj_id': 15,
        },
    )

    assert response.status_code == status.HTTP_200_OK

    try:
        AnimalsScheme.model_validate(response.json())
    except ValidationError as error:
        pytest.fail(f'Response does not match schema: {error}')


async def test_get_animal_by_ids(async_animals_client: AsyncClient, async_animal_prefix: str):

    response = await async_animals_client.get(
        url=async_animal_prefix+'/get-by-ids',
        params={
            'ids': [15, 16, 17],
        },
    )
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response_data, list)

    try:
        map(AnimalsScheme.model_validate, response_data)
    except ValidationError as error:
        pytest.fail(f'Response does not match schema: {error}')


async def test_get_all_animals(async_animals_client: AsyncClient, async_animal_prefix: str):
    response = await async_animals_client.get(url=async_animal_prefix+'/get-all')
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response_data, list)

    try:
        map(AnimalsScheme.model_validate, response_data)
    except ValidationError as error:
        pytest.fail(f'Response does not match schema: {error}')
