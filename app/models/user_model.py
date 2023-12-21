from pydantic import BaseModel
from sqlalchemy import Column, Engine, Integer, MetaData, String

from app.database import Base


class UserDb(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)


class UserBase(BaseModel):
    name: str
    username: str
    email: str
    password: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
