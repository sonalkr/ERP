from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from fastapi import FastAPI
from pydantic import BaseModel

from app.database import Base
from app.models.ledger_model import Ledger
from app.models.user_model import User
from datetime import datetime

# Define the voucher table schema


class VoucherDb(Base):
    __tablename__ = "vouchers"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    dc_no = Column(String)
    ledger_id = Column(Integer, ForeignKey('ledgers.id'))
    qty = Column(Float)
    rate = Column(Float)
    amount = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id'))
    invoice_no = Column(String)  # Added invoice_no field
    created_on = Column(DateTime, default=datetime.utcnow)

    ledger = relationship("LedgerDb", back_populates="vouchers")
    user = relationship("UserDb", back_populates="vouchers")


class VoucherBase(BaseModel):
    date: datetime
    created_on: datetime
    dc_no: str
    ledger: Ledger
    qty: float
    rate: float
    amount: float

    invoice_no: str  # Added invoice_no field
    user: User


class VoucherCreate(VoucherBase):
    pass


class Voucher(VoucherBase):
    id: int

    class Config:
        orm_mode = True
