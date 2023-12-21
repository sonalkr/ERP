from fastapi import FastAPI
# from sqlalchemy import Engine

from app.database import Base, engine
from app.routers import users_route, ledger_route

app = FastAPI()


app.include_router(users_route.router)
app.include_router(ledger_route.router)

Base.metadata.create_all(bind=engine)
