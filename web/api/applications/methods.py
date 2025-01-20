from typing import Annotated

from fastapi import APIRouter, Depends, Query

from app.services import ApplicationService, get_application_service
from web.api.applications import schemas

router = APIRouter()


@router.get('/applications', response_model=schemas.GetApplicationsResponse)
async def get_applications(
    filter_query: Annotated[schemas.GetApplicationsRequest, Query()],
    service: ApplicationService = Depends(get_application_service),
):
    return await service.search_applications(**filter_query.model_dump())


@router.post('/applications', response_model=schemas.AddApplicationResponse)
async def add_application(
    application_info: schemas.AddApplicationRequest,
    service: ApplicationService = Depends(get_application_service),
):
    result = await service.add_application(application_info.model_dump())
    app_data = schemas.AddApplicationResponse.model_validate(result)
    return app_data
