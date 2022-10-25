from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.db.base_class import Entity


class Status(Entity):
    __tablename__ = "status"

    name = Column(String, nullable=False, unique=True)
    profiles = relationship("Profile")
