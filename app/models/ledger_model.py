from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from app.database import Base


# Define the ledger table schema
class ledgerDb(Base):
    __tablename__ = 'ledger'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    amount = Column(Integer)
    desc = Column(String(255))
    note = Column(String(255))

# Define the ledgerBase schema for request/response validation


class ledgerBase(BaseModel):
    name: str
    amount: int
    desc: str
    note: str

# Define the ledgerCreate schema for creating a new ledger


class ledgerCreate(ledgerBase):
    pass

# Define the ledger schema for returning a ledger


class ledger(ledgerBase):
    id: int

    class Config:
        orm_mode = True
