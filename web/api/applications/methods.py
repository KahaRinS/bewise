from typing import Annotated

from fastapi import APIRouter, Query
from starlette.responses import JSONResponse

from web.api.applications import schemas

router = APIRouter()


@router.get('/applications', response_model=schemas.GetApplicationsResponse)
async def get_applications(
    filter_query: Annotated[schemas.GetApplicationsRequest, Query()],
) -> JSONResponse:
    pass


@router.post('/applications', response_model=schemas.AddApplicationResponse)
async def login(
    application_info: schemas.AddApplicationRequest,
) -> JSONResponse:
    pass
