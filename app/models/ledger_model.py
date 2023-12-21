from app.models.user_model import User
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from app.database import Base


# Define the ledger table schema


class LedgerDb(Base):
    __tablename__ = 'ledgers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    amount = Column(Integer)
    desc = Column(String(255))
    note = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'),
                     primary_key=True, nullable=True)

    user = relationship("UserDb", back_populates="ledgers")

# Define the ledgerBase schema for request/response validation


class LedgerBase(BaseModel):
    name: str
    amount: int
    desc: str
    note: str
    user: User

# Define the ledgerCreate schema for creating a new ledger


class LedgerCreate(LedgerBase):
    pass

# Define the ledger schema for returning a ledger


class Ledger(LedgerBase):
    id: int

    class Config:
        orm_mode = True
