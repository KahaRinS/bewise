from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class ApplicationInfo(BaseModel):
    id: int = Field(...)
    created_at: datetime = Field(..., description='Дата и время создания заявки')
    user_name: str = Field(..., max_length=100, description='Имя пользователя')
    description: str = Field(default=None, max_length=300, description='Описание заявки')


class AddApplicationRequest(ApplicationInfo):
    id: Optional[int] = Field(None, exclude=True)
    created_at: Optional[str] = Field(None, exclude=True)


class AddApplicationResponse(ApplicationInfo):
    """AddApplicationResponse"""


class GetApplicationsRequest(BaseModel):
    user_name: Optional[str] = Field(None, description='Фильтр по имени пользователя')
    page: int = Field(1, ge=1, description='Номер страницы для пагинации')
    size: int = Field(10, ge=1, le=100, description='Количество записей на странице')


class GetApplicationsResponse(BaseModel):
    total: int = Field(..., description='Общее количество записей')
    page: int = Field(..., description='Текущая страница')
    size: int = Field(..., description='Количество записей на странице')
    items: List[ApplicationInfo] = Field(..., description='Список записей на текущей странице')
