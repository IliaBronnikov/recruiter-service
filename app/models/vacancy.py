from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.db.base_class import Entity
from app.models.profile import profile_vacancy


class Vacancy(Entity):
    __tablename__ = "vacancies"

    name = Column(String, nullable=False, unique=True)
    description = Column(String)
    profiles = relationship("Profile", secondary=profile_vacancy, back_populates="vacancies")
