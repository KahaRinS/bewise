from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from settings import AppConfig


def get_apps_router():
    router = APIRouter()
    return router


def get_application() -> FastAPI:
    application = FastAPI(
        title=AppConfig.PROJECT_NAME,
        debug=AppConfig.DEBUG,
        version=AppConfig.VERSION,
        connections=[],
    )
    application.include_router(get_apps_router())

    application.add_middleware(
        CORSMiddleware,
        **AppConfig.CORS,
    )
    return application


app = get_application()
