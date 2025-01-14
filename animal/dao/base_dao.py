from app.database import (
    async_session,
)
from sqlalchemy import (
    select,
    delete,
)


class BaseDAO:
    """DAO для реализации базовых методов."""

    obj = None

    @classmethod
    async def create_obj(cls, fields: dict) -> None:
        async with async_session() as session:
            new_obj = cls.obj(
                **fields,
            )
            session.add(new_obj)
            await session.commit()

    @classmethod
    async def get_obj_by_id(cls, id: int) -> any:
        async with async_session() as session:
            query = select(cls.obj).where(cls.obj.id==id)
            result = await session.execute(query)
            obj = result.scalars().first()
    
            if not obj:
                raise ValueError(f"Объект с ID {id} не найден")

            return obj
    
    @classmethod
    async def get_all_obj(cls) -> list[any]:
        async with async_session() as session:
            query = select(cls.obj)
            result = await session.execute(query)

            return result.scalars().all()

    @classmethod
    async def update_obj(cls, id: int, data: dict) -> any:
        async with async_session() as session:
            query = await session.execute(select(cls.obj).where(cls.obj.id==id))
            obj = query.scalar()

            for key, value in data.items():
                setattr(obj, key, value)

            await session.commit()
            await session.refresh(obj)

            return obj

    @classmethod
    async def delete_obj(cls, id: int) -> None:
        async with async_session() as session:
            query = delete(cls.obj).where(cls.obj.id==id)
            await session.execute(query)
            await session.commit()
