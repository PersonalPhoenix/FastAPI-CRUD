from fastapi import (
    APIRouter,
    status,
    HTTPException,
)

from app.config import (
    settings,
)
from app.animal.schemas.animals_schemas import (
    AnimalsScheme,
)
from app.animal.dao.animal_dao import (
    AnimalDAO,
)


router = APIRouter(
    prefix=settings.ANIMAL_PREFIX,
    tags=[settings.ANIMAL_TAG],
)


@router.post('/create', response_model=int)
async def create_animal(fields: AnimalsScheme):
    await AnimalDAO.create_obj(fields=dict(fields))

    return status.HTTP_201_CREATED


@router.post('/select/{id}', response_model=AnimalsScheme)
async def get_animal_by_id(id: int):
    if animal := await AnimalDAO.get_obj_by_id(id=id):
        return animal
    else:
        raise HTTPException(status_code=404, detail="Объект не найден")


@router.post('/select-all-animals/', response_model=list[AnimalsScheme])
async def get_all_animals():
    return await AnimalDAO.select_all_obj()


@router.post('/update/{id}', response_model=AnimalsScheme)
async def update_animal(id:int, data: AnimalsScheme):
    return await AnimalDAO.update_obj(id=id, data=dict(data))


@router.post('/delete/{id}', response_model=int)
async def delete_animal(id: int):
    await AnimalDAO.delete_obj(id=id)

    return status.HTTP_200_OK
