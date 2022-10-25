from fastapi import APIRouter, FastAPI

from app.api.profiles import router as profiles_router
from app.api.statuses import router as status_router
from app.api.vacancies import router as vacancies_router
from app.settings import get_settings


settings = get_settings()


def create_router() -> APIRouter:
    root_api_router = APIRouter()

    root_api_router.include_router(router=vacancies_router, prefix='/vacancies', tags=['Vacancy'])
    root_api_router.include_router(router=profiles_router, prefix='/profiles', tags=['Profile'])
    root_api_router.include_router(router=status_router, prefix='/statuses', tags=['Status'])

    return root_api_router


app = FastAPI(
    title=settings.PROJECT_NAME
)

app.include_router(create_router())
