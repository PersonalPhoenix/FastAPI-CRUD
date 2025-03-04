from typing import (
    Optional,
)

from sqlalchemy import (
    delete,
    select,
)

from app.config import (
    settings,
)
from app.database import (
    async_session,
    test_async_session,
)


class BaseDAO:
    """DAO для реализации базовых методов."""

    obj = None
    session_maker = async_session

    @classmethod
    async def create_obj(cls, fields: dict) -> None:
        async with cls.session_maker() as session:
            new_obj = cls.obj(
                **fields,
            )
            session.add(new_obj)
            await session.commit()

    @classmethod
    async def create_objs(cls, data: list[dict]) -> None:
        async with cls.session_maker() as session:
            new_objs = (
                cls.obj(**fields.model_dump()) for fields in data
            )
            session.add_all(new_objs)
            await session.commit()

    @classmethod
    async def get_all_objs(
        cls, 
        limit: Optional[int] = None, 
        offset: Optional[int] = None,
    ) -> list[any]:
        async with cls.session_maker() as session:
            query = select(cls.obj)

            if limit:
                query.limit(limit=limit)

            if offset:
                query.offset(offset=offset)

            result = await session.execute(query)

            return result.scalars().all()

    @classmethod
    async def get_obj_by_ids(cls, ids: list[int]) -> any:
        async with cls.session_maker() as session:
            query = select(cls.obj).where(cls.obj.id.in_(ids))
            result = await session.execute(query)

            return result.scalars().all()

    @classmethod
    async def get_obj_by_id(cls, obj_id: int) -> any:
        async with cls.session_maker() as session:
            query = select(cls.obj).where(cls.obj.id==obj_id)
            result = await session.execute(query)
            obj = result.scalars().first()
    
            if not obj:
                raise ValueError(f"Объект с ID {obj_id} не найден")

            return obj

    @classmethod
    async def get_obj_by_filter(cls, **filters):
        async with cls.session_maker() as session:
            query = select(cls.obj)

            if filters:
                query.filter(**filters)

            result = await session.execute(query)

            return result.scalar()

    @classmethod
    async def update_obj_by_id(cls, obj_id: int, data: dict) -> any:
        async with cls.session_maker() as session:
            query = await session.execute(select(cls.obj).where(cls.obj.id==obj_id))
            obj = query.scalar()

            for key, value in data.items():
                setattr(obj, key, value)

            await session.refresh(obj)
            await session.commit()

            return obj

    @classmethod
    async def delete_obj_by_id(cls, obj_id: int) -> None:
        async with cls.session_maker() as session:
            query = delete(cls.obj).where(cls.obj.id==obj_id)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete_obj_by_ids(cls, ids: list[int]) -> None:
        async with cls.session_maker() as session:
            query = delete(cls.obj).where(cls.obj.id.in_(ids))
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete_all_obj(cls) -> None:
        async with cls.session_maker() as session:
            query = delete(cls.obj)
            await session.execute(query)
            await session.commit()
