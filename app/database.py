from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.sqlite"  # Use your own database URL
# SQLALCHEMY_DATABASE_URL = "./test.db"  # Use your own database URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():

    db = SessionLocal()
    # Base.metadata.create_all(bind=Engine)
    db.commit()
    # db.execute('PRAGMA foreign_keys = ON;')

    try:
        yield db
    finally:
        db.close()
