from pydantic import BaseModel
from sqlalchemy import Column, Float, ForeignKey, Integer, String

from app.database import Base
from app.models.unit_model import Unit
from sqlalchemy.orm import relationship


class InventoryDb(Base):
    __tablename__ = 'inventorys'

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, index=True)
    name = Column(String, index=True, unique=True)
    desc = Column(String)
    qty = Column(Float)
    unit_id = Column(Integer, ForeignKey('units.id'))
    price = Column(Float)
    Freight = Column(Float)

    unit = relationship("UnitDb", back_populates="inventorys")


class InventoryBase(BaseModel):
    sku: str
    name: str
    desc: str
    qty: float
    unit: Unit
    price: float
    Freight: float


class InventoryCreate(InventoryBase):
    pass


class Inventory(InventoryBase):
    id: int

    class Config:
        orm_mode = True
