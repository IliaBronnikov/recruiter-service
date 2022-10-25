from typing import Optional

from pydantic import BaseModel, Field


class VacancyBase(BaseModel):
    name: Optional[str] = Field(..., description="Название вакансии", example='Software development')
    description: Optional[str] = Field(
        description="Описание вакансии", example='Search 3+ years experience...'
    )


class VacancyCreate(VacancyBase):
    pass


class VacancyUpdate(VacancyBase):
    name: Optional[str] = Field(description="Название вакансии", example='Software development')


class VacancyInDBBase(VacancyBase):
    id: Optional[int] = Field(description="ИД профиля", example=1)

    class Config:
        orm_mode = True


class Vacancy(VacancyInDBBase):
    pass
