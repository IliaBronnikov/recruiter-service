from sqlalchemy import Column, ForeignKey, Integer, String, Table, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.base_class import Base, Entity


profile_vacancy = Table(
    'profile_vacancy',
    Base.metadata,
    Column('profile_id', ForeignKey("profiles.id"), primary_key=True),
    Column('vacancy_id', ForeignKey("vacancies.id"), primary_key=True),
    UniqueConstraint("profile_id", "vacancy_id", name="uix_profile_vacancy_id"),
)

class Profile(Entity):
    __tablename__ = "profiles"

    name = Column(String, nullable=False)
    email = Column(String, default=None, unique=True)
    status_id = Column(Integer, ForeignKey("status.id"))
    vacancies = relationship("Vacancy", secondary=profile_vacancy, back_populates="profiles")
