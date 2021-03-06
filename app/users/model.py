"""
This module defines the actual database ORM model of the User resource.
It is the representation that is used to describe how the database schema
will look.
"""
from sqlalchemy import Column, Integer, String

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    public_id = Column(String(100), unique=True, nullable=False)
    email = Column(String(length=120), unique=True, nullable=False)
    password = Column(String(length=128), nullable=False)

    def __repr__(self):
        return (
            f"<{self.__class__.__name__} ("
            f"public_id={self.public_id}, "
            f"email={self.email}, "
        )
