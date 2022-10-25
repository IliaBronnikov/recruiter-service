from typing import Optional

from pydantic import BaseModel


class StatusBase(BaseModel):
    name: Optional[str] = None


class StatusCreate(StatusBase):
    pass


class StatusUpdate(StatusBase):
    pass


class StatusInDBBase(StatusBase):
    id: int
    name: str

    class Config:
        orm_mode = True


class Status(StatusInDBBase):
    pass
