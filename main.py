from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from config.database import Session, engine, Base
from models.movie import Movie
from decouple import config
from routes import movie

app = FastAPI(title='Movies API')
app.include_router(movie.router)

Base.metadata.create_all(bind=engine)

@app.get('/', tags=['home'])
def home():
    return RedirectResponse(config('URL') + '/docs')