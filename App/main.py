from fastapi import FastAPI, Depends
from App import models
from database import engine
from router import auth, inference


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
app.include_router(inference.router)