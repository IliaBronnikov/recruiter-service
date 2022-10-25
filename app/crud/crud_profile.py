from typing import List

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Vacancy, Status
from app.models.profile import Profile, profile_vacancy
from app.schemas.profile import ProfileCreate, ProfileUpdate


class CRUDProfile(CRUDBase[Profile, ProfileCreate, ProfileUpdate]):
    def get_multi_by_status(
        self, db: Session, *, status_id: int, skip: int = 0, limit: int = 100
    ) -> List[Profile]:
        return (
            db.query(self.model).filter(Profile.status_id == status_id).offset(skip).limit(limit).all()
        )

    def get_multi_by_vacancy(
        self, db: Session, *, vacancy_id: int, skip: int = 0, limit: int = 100
    ) -> List[Profile]:

        vacancy = db.query(Vacancy).filter(Vacancy.id == vacancy_id).first()
        if not vacancy:
            raise HTTPException(status_code=404, detail="Vacancy not found")

        return (
            db.query(self.model)
            .join(profile_vacancy, self.model.id == profile_vacancy.c.profile_id)
            .filter(profile_vacancy.c.vacancy_id == vacancy_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def update(self, db: Session, *, db_obj: Profile, obj_in: ProfileUpdate) -> Profile:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        status = db.query(Status).filter(Status.id == obj_in.status_id).first()
        if not status:
            raise HTTPException(status_code=404, detail="Status not found")

        if vacancy := db.query(Vacancy).filter(Vacancy.id == obj_in.vacancy_id).first():
            db_obj.vacancies.append(vacancy)
        else:
            raise HTTPException(status_code=404, detail="Vacancy not found")

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return db_obj

    def remove_vacancy(self, db: Session, *, profile_id: int, vacancy_id: int) -> Profile:
        profile = self.get(db=db, id=profile_id)
        if vacancy := db.query(Vacancy).filter(Vacancy.id == vacancy_id).first():
            profile.vacancies.remove(vacancy)

        db.commit()
        return profile


profile = CRUDProfile(Profile)
