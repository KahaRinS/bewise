from app.models import Applications

from .base import EntityDBRepository


class ApplicationsRepository(EntityDBRepository):
    entity = Applications
