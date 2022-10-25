from typing import Dict, List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.status import Status
from app.schemas.status import StatusCreate, StatusUpdate


class CRUDStatus(CRUDBase[Status, StatusCreate, StatusUpdate]):
    def get_status_names(self, db: Session) -> Dict:
        names = db.query(self.model)
        return {name.id: name.name for name in names.all()}


status = CRUDStatus(Status)
