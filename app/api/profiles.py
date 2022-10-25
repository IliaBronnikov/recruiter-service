from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db.session import get_db
from app.schemas import Profile


router = APIRouter()


@router.post("/", response_model=schemas.Profile, summary='Create a profile')
def create_profile(
    *,
    db: Session = Depends(get_db),
    profile_in: schemas.ProfileCreate,
) -> Profile:
    profile = crud.profile.create(db=db, obj_in=profile_in)
    return profile


@router.delete(
    "/vacancies/remove", response_model=schemas.Profile, summary='Remove the profile from vacancy'
)
def remove_profile_from_vacancy(
    *, db: Session = Depends(get_db), profile_id: int, vacancy_id: int
) -> Profile:
    profile = crud.profile.get(db=db, id=profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    vacancy = crud.vacancy.get(db=db, id=vacancy_id)
    if not vacancy:
        raise HTTPException(status_code=404, detail="Vacancy not found")

    profile = crud.profile.remove_vacancy(
        db=db, db_obj=profile, profile_id=profile_id, vacancy_id=vacancy_id
    )
    return profile


@router.get(
    '/vacancies/{vacancy_id}',
    response_model=List[schemas.Profile],
    summary='Get list of profiles by vacancy',
)
def get_profiles_by_vacancy(
    *,
    db: Session = Depends(get_db),
    vacancy_id: int = Path(..., description="ИД вакансии", example=2),
    skip: int = 0,
    limit: int = 100,
) -> Profile:
    profiles = crud.profile.get_multi_by_vacancy(db=db, skip=skip, limit=limit, vacancy_id=vacancy_id)
    print(profiles)
    return profiles


@router.get('/{profile_id}', response_model=schemas.Profile, summary='Get a profile')
def get_profile(
    *, db: Session = Depends(get_db), profile_id: int = Path(..., description="ИД профиля", example=2)
) -> Profile:
    profile = crud.profile.get(db=db, id=profile_id)

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


@router.get('/', response_model=List[schemas.Profile], summary='Get list of profiles')
def get_profiles(
    *,
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Profile:
    profiles = crud.profile.get_multi(db=db, skip=skip, limit=limit)

    return profiles


@router.get(
    '/statuses/{status_id}',
    response_model=List[schemas.Profile],
    summary='Get list of profiles by status',
)
def get_profiles_by_status(
    *,
    db: Session = Depends(get_db),
    status_id: int = Path(..., description="ИД статуса", example=2),
    skip: int = 0,
    limit: int = 100,
) -> Profile:
    profiles = crud.profile.get_multi_by_status(db=db, skip=skip, limit=limit, status_id=status_id)

    return profiles


@router.put("/{profile_id}", response_model=schemas.Profile, summary='Update a profile')
def update_profile(
    *,
    db: Session = Depends(get_db),
    profile_id: int = Path(..., description="ИД профиля", example=2),
    profile_in: schemas.ProfileUpdate,
) -> Profile:
    profile = crud.profile.get(db=db, id=profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    profile = crud.profile.update(db=db, db_obj=profile, obj_in=profile_in)

    return profile


@router.delete("/{profile_id}", response_model=schemas.Profile, summary='Delete a profile')
def delete_profile(
    *,
    db: Session = Depends(get_db),
    profile_id: int = Path(..., description="ИД профиля", example=2),
) -> Profile:
    profile = crud.profile.get(db=db, id=profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    profile = crud.profile.remove(db=db, id=profile_id)
    return profile
