from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Path, Query
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db.session import get_db
from app.schemas import Vacancy


router = APIRouter()


@router.post("/", response_model=schemas.Vacancy, summary='Create a vacancy')
def create_vacancy(
    *,
    db: Session = Depends(get_db),
    vacancy_in: schemas.VacancyCreate,
) -> Vacancy:
    vacancy = crud.vacancy.create(db=db, obj_in=vacancy_in)
    return vacancy


@router.get('/{vacancy_id}', response_model=schemas.Vacancy, summary='Get a vacancy')
def get_vacancy(
    *, db: Session = Depends(get_db), vacancy_id: int = Path(..., description="ИД вакансии", example=2)
) -> Vacancy:
    vacancy = crud.vacancy.get(db=db, id=vacancy_id)

    if not vacancy:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    return vacancy


@router.get('/', response_model=List[schemas.Vacancy], summary='Get list of vacancies')
def get_vacancies(
    *,
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Vacancy:
    vacancies = crud.vacancy.get_multi(db=db, skip=skip, limit=limit)

    return vacancies


@router.put("/{vacancy_id}", response_model=schemas.Vacancy, summary='Update a vacancy')
def update_vacancy(
    *,
    db: Session = Depends(get_db),
    vacancy_id: int = Path(..., description="ИД профиля", example=2),
    vacancy_in: schemas.VacancyUpdate,
) -> Vacancy:
    vacancy = crud.vacancy.get(db=db, id=vacancy_id)
    if not vacancy:
        raise HTTPException(status_code=404, detail="Vacancy not found")

    vacancy = crud.vacancy.update(db=db, db_obj=vacancy, obj_in=vacancy_in)
    return vacancy


@router.delete("/{vacancy_id}", response_model=schemas.Vacancy, summary='Delete a vacancy')
def delete_vacancy(
    *,
    db: Session = Depends(get_db),
    vacancy_id: int = Path(..., description="ИД вакансии", example=2),
) -> Vacancy:
    vacancy = crud.vacancy.get(db=db, id=vacancy_id)
    if not vacancy:
        raise HTTPException(status_code=404, detail="Vacancy not found")

    vacancy = crud.vacancy.remove(db=db, id=vacancy_id)
    return vacancy
