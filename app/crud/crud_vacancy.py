from app.crud.base import CRUDBase
from app.models.vacancy import Vacancy
from app.schemas.vacancy import VacancyCreate, VacancyUpdate


class CRUDVacancy(CRUDBase[Vacancy, VacancyCreate, VacancyUpdate]):
    ...


vacancy = CRUDVacancy(Vacancy)
