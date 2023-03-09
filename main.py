from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from config.database import Session, engine, Base
from models.movie import Movie
from decouple import config

app = FastAPI(
    title='Movies API'
)

Base.metadata.create_all(bind=engine)

@app.get('/')
def home():
    return RedirectResponse(config('URL') + '/docs')