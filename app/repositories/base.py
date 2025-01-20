import contextvars
from typing import Type, TypeVar

from sqlalchemy import func
from sqlalchemy.dialects.postgresql.asyncpg import PGDialect_asyncpg
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

db_ctx = contextvars.ContextVar('connection')
dialect = PGDialect_asyncpg(paramstyle='pyformat')

T = TypeVar('T')


class EntityDBRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    entity: Type[T]

    async def create(self, payload: dict) -> T:

        new_entity = self.entity(**payload)
        self.db.add(new_entity)
        await self.db.commit()
        await self.db.refresh(new_entity)
        return new_entity

    async def paginated_search(
        self,
        page: int = 1,
        page_size: int = 10,
        user_name: str = None,
    ):
        query = select(self.entity)

        if user_name:
            query = query.filter(self.entity.user_name == user_name)

        if user_name:
            total_count_query = select(func.count()).select_from(self.entity).filter(self.entity.user_name == user_name)
        else:
            total_count_query = select(func.count()).select_from(self.entity)
        total_count_result = await self.db.execute(total_count_query)
        total_count = total_count_result.scalar()

        query = query.offset((page - 1) * page_size).limit(page_size)

        result = await self.db.execute(query)
        items = result.scalars().all()

        items_dict = [self.sqlalchemy_to_dict(item) for item in items]

        total_pages = (total_count // page_size) + (1 if total_count % page_size > 0 else 0)

        return {
            'items': items_dict,
            'total_count': total_count,
            'page': page,
            'page_size': page_size,
            'total_pages': total_pages,
        }

    @classmethod
    def sqlalchemy_to_dict(cls, instance):
        return {column.name: getattr(instance, column.name) for column in instance.__table__.columns}
