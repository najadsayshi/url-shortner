from fastapi import FastAPI
from app.routes import router
from app.db import engine
from sqlmodel import SQLModel

app = FastAPI()

SQLModel.metadata.create_all(engine)

app.include_router(router)