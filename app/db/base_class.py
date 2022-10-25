from sqlalchemy import Column,Integer
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class Base:
    pass


class Entity(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    # can add later

    # created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    # updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
