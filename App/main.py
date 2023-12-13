from fastapi import FastAPI, Depends
from App import models
from database import engine
from router import auth


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(auth.router)