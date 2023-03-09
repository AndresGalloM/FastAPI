from fastapi import FastAPI
from config.database import Session, engine, Base
from models.movie import Movie

app = FastAPI()

Base.metadata.create_all(bind=engine)

