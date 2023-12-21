from sqlalchemy import Column, Enum, Integer, String
from pydantic import BaseModel

from app.database import Base
import enum


class UnitNameEnum(enum.Enum):
    BAG = "Bag"
    BDL = "Bundles"
    BAL = "Bale"
    BKL = "Buckles"
    BOU = "Billions Of Units"
    BOX = "Box"
    BTL = "Bottles"
    BUN = "Bunches"
    CAN = "Cans"
    CTN = "Cartons"
    DOZ = "Dozen"
    DRM = "Drum"
    GGR = "Great Gross"
    GRS = "Gross"
    NOS = "Numbers"
    PAC = "Packs"
    PCS = "Pieces"
    PRS = "Pairs"
    ROL = "Rolls"
    SET = "Sets"
    TBS = "Tablets"
    TGM = "Ten Gross"
    THD = "Thousands"
    TUB = "Tubes"
    UNT = "Units"
    CBM = "Cubic Meter"
    CCM = "Cubic Centimeter"
    KLR = "Kilo Liter"
    MLT = "Milliliter"
    UGS = "US Gallons"
    SQF = "Square Feet"
    SQM = "Square Meters"
    SQY = "Square Yards"
    GYD = "Gross Yards"
    KME = "Kilo Meter"
    MTR = "Meters"
    YDS = "Yards"
    CMS = "Centimeter"
    TON = "Tonnes"
    QTL = "Quintal"
    GMS = "Grams"
    KGS = "Kilo Grams"
    OTH = "Other"


class UnitDb(Base):
    __tablename__ = 'units'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    unit_name = Column(Enum(UnitNameEnum))


class UnitBase(BaseModel):
    name: str
    unit_name: UnitNameEnum


class UnitCreate(UnitBase):
    pass


class Unit(UnitBase):
    id: int

    class Config:
        orm_mode = True
