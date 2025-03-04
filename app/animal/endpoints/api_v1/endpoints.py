from typing import (
    Optional,
)

from fastapi import (
    APIRouter,
    status,
    HTTPException,
    Query,
)

from app.config import (
    settings,
)
from app.animal.dao.animal_dao import (
    AnimalDAO,
)
from app.animal.schemas.animals_schemas import (
    AnimalsScheme,
)


router = APIRouter(
    tags=[settings.ANIMAL_TAG],
    prefix=settings.ANIMAL_PREFIX,
)


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_animal(fields: AnimalsScheme):
    return await AnimalDAO.create_obj(fields=fields.model_dump())


@router.post('/multi-create', status_code=status.HTTP_201_CREATED)
async def create_animal(data: list[AnimalsScheme]):
    await AnimalDAO.create_objs(data=data)


@router.get('/get-by-id', response_model=AnimalsScheme, status_code=status.HTTP_200_OK)
async def get_animal_by_id(obj_id: int):
    if animal := await AnimalDAO.get_obj_by_id(obj_id=obj_id):
        return animal

    raise HTTPException(status_code=404, detail="Объект не найден")


@router.get('/get-by-ids', response_model=list[AnimalsScheme], status_code=status.HTTP_200_OK)
async def get_animal_by_ids(ids: list[int] = Query(...)):
    return await AnimalDAO.get_obj_by_ids(ids=ids)


@router.get('/get-all', response_model=list[AnimalsScheme], status_code=status.HTTP_200_OK)
async def get_all_animals(limit: Optional[int] = None, offset: Optional[int] = None):
    return await AnimalDAO.get_all_objs(limit=limit, offset=offset)


@router.patch('/update', response_model=AnimalsScheme, status_code=status.HTTP_200_OK)
async def update_animal(obj_id:int, data: AnimalsScheme):
    return await AnimalDAO.update_obj(obj_id=obj_id, data=dict(data))


@router.delete('/delete-by-id', status_code=status.HTTP_200_OK)
async def delete_animal_by_id(obj_id: int):
    return await AnimalDAO.delete_obj_by_id(obj_id=obj_id)


@router.delete('/delete-by-ids', status_code=status.HTTP_200_OK)
async def delete_animal_by_ids(ids: list[int] = Query(...)):
    return await AnimalDAO.delete_obj_by_ids(ids=ids)


@router.delete('/delete-all', status_code=status.HTTP_200_OK)
async def delete_all_animal():
    return await AnimalDAO.delete_all_obj()
