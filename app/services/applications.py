import json

from fastapi import Depends

from app.repositories import ApplicationsRepository
from app.repositories.kafka import AIOWebProducer, get_producer
from helpers import get_session
from web.api.applications.schemas import AddApplicationResponse


class ApplicationService:
    def __init__(self, db, kafka_producer: AIOWebProducer):
        self.applications_repository = ApplicationsRepository(db)
        self.kafka_producer = kafka_producer

    async def add_application(self, application_data):
        new_application = await self.applications_repository.create(application_data)
        application_data = AddApplicationResponse.model_validate(new_application)
        await self.send_message_to_topic(application_data)
        return application_data

    async def send_message_to_topic(self, application_data):
        application_data_dict = application_data.model_dump()
        application_data_dict['id'] = str(application_data_dict['id'])
        application_data_dict['created_at'] = str(application_data_dict['id'])

        mes = json.dumps(application_data_dict).encode("utf-8")
        await self.kafka_producer.send(mes)

    async def search_applications(self, **query):
        return await self.applications_repository.paginated_search(**query)


async def get_application_service(
    db=Depends(get_session),
) -> ApplicationService:
    return ApplicationService(db=db, kafka_producer=get_producer())
