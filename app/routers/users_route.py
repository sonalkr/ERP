from app.models.user_model import User, UserDb
from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserDb).filter(UserDb.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users")
def get_users(limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):
    users = db.query(UserDb).limit(limit).offset(offset).all()
    return users


@router.post("/users")
def create_user(user: User, db: Session = Depends(get_db)):
    user_db = UserDb(name=user.name, username=user.username,
                     email=user.email, password=user.password)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user


@router.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User, db: Session = Depends(get_db)):
    user = db.query(UserDb).filter(UserDb.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = updated_user.name
    user.username = updated_user.username
    user.email = updated_user.email
    user.password = updated_user.password
    db.commit()
    db.refresh(user)
    return user


@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserDb).filter(UserDb.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
