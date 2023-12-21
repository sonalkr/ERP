from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
from app.models.ledger_model import Ledger, LedgerCreate, LedgerDb

router = APIRouter()


@router.get("/ledgers/{ledger_id}")
def get_ledger(ledger_id: int, db: Session = Depends(get_db)):
    ledger = db.query(LedgerDb).filter(LedgerDb.id == ledger_id).first()
    if not ledger:
        raise HTTPException(status_code=404, detail="Ledger not found")
    return ledger


@router.get("/ledgers")
def get_ledgers(limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):
    ledgers = db.query(LedgerDb).limit(limit).offset(offset).all()
    return ledgers


@router.post("/ledgers")
def create_ledger(ledger: LedgerCreate, db: Session = Depends(get_db)):
    ledger_db = LedgerDb(name=ledger.name, amount=ledger.amount,
                         desc=ledger.desc, note=ledger.note)
    db.add(ledger_db)
    db.commit()
    db.refresh(ledger_db)
    return ledger


@router.put("/ledgers/{ledger_id}")
def update_ledger(ledger_id: int, updated_ledger: Ledger, db: Session = Depends(get_db)):
    ledger = db.query(LedgerDb).filter(LedgerDb.id == ledger_id).first()
    if not ledger:
        raise HTTPException(status_code=404, detail="Ledger not found")
    ledger.name = updated_ledger.name
    ledger.amount = updated_ledger.amount
    ledger.desc = updated_ledger.desc
    ledger.note = updated_ledger.note
    db.commit()
    db.refresh(ledger)
    return ledger


@router.delete("/ledgers/{ledger_id}")
def delete_ledger(ledger_id: int, db: Session = Depends(get_db)):
    ledger = db.query(LedgerDb).filter(LedgerDb.id == ledger_id).first()
    if not ledger:
        raise HTTPException(status_code=404, detail="Ledger not found")
    db.delete(ledger)
    db.commit()
    return {"message": "Ledger deleted successfully"}
