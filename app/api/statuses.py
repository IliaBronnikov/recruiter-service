from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db.session import get_db
from app.schemas import Status


router = APIRouter()


@router.post("/", response_model=schemas.Status, summary='Create a status')
def create_status(
    *,
    db: Session = Depends(get_db),
    status_in: schemas.StatusCreate,
) -> Status:
    status_names = crud.status.get_status_names(db=db)
    if status_in.name in status_names.values():
        raise HTTPException(status_code=400, detail="Status already exist")

    status = crud.status.create(db=db, obj_in=status_in)
    return status


@router.get('/{status_id}', response_model=schemas.Status, summary='Get a status')
def get_status(
    *, db: Session = Depends(get_db), status_id: int = Path(..., description="ИД статуса", example=2)
) -> Status:
    status = crud.status.get(db=db, id=status_id)

    if not status:
        raise HTTPException(status_code=404, detail="Status not found")
    return status


@router.get('/', response_model=List[schemas.Status], summary='Get list of statuses')
def get_statuses(
    *,
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Status:
    statuses = crud.status.get_multi(db=db, skip=skip, limit=limit)

    return statuses


@router.put("/{status_id}", response_model=schemas.Status, summary='Update a status')
def update_status(
    *,
    db: Session = Depends(get_db),
    status_id: int = Path(..., description="ИД статуса", example=2),
    status_in: schemas.StatusUpdate,
) -> Status:
    status = crud.status.get(db=db, id=status_id)
    if not status:
        raise HTTPException(status_code=404, detail="Status not found")

    status_names = crud.status.get_status_names(db=db)
    if status_in.name in status_names.values() and not status_names[status_id] == status_in.name:
        raise HTTPException(status_code=400, detail="Status already exist")

    status = crud.status.update(db=db, db_obj=status, obj_in=status_in)
    return status


@router.delete("/{status_id}", response_model=schemas.Status, summary='Delete a status')
def delete_status(
    *,
    db: Session = Depends(get_db),
    status_id: int = Path(..., description="ИД статуса", example=2),
) -> Status:
    status = crud.status.get(db=db, id=status_id)
    if not status:
        raise HTTPException(status_code=404, detail="Status not found")

    status = crud.status.remove(db=db, id=status_id)
    return status
