from fastapi import Depends

from app.repositories import ApplicationsRepository
from helpers import get_session


class ApplicationService:
    def __init__(self, db):
        self.applications_repository = ApplicationsRepository(db)

    async def add_application(self, application_data):
        new_application = await self.applications_repository.create(application_data)
        return new_application

    async def search_applications(self, **query):
        return await self.applications_repository.paginated_search(**query)


async def get_application_service(
    db=Depends(get_session),
) -> ApplicationService:
    return ApplicationService(db=db)
