from typing import Optional

from pydantic import BaseModel, Field


class ProfileBase(BaseModel):
    name: Optional[str] = Field(..., description="Имя профиля", example='Илья')
    email: Optional[str] = Field(..., description="Почта профиля", example='someone@example.ru')
    status_id: Optional[int] = Field(description="Статус профиля", example=1)


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(ProfileBase):
    name: Optional[str] = Field(description="Имя профиля", example='Илья')
    email: Optional[str] = Field(description="Почта профиля", example='someone@example.ru')
    vacancy_id: Optional[str] = Field(description="Имя профиля", example='Илья')


class ProfileInDBBase(ProfileBase):
    id: Optional[int] = Field(description="ИД профиля", example=1)

    class Config:
        orm_mode = True


class Profile(ProfileInDBBase):
    pass
