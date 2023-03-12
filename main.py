from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from config.database import engine, Base
from models.movie import Movie
from decouple import config
from routes import movie
from middlewares import error_handler

app = FastAPI(title='Movies API')

# Routes
app.include_router(movie.router)

# Middelwares
app.add_middleware(error_handler.ErrorHandler)

Base.metadata.create_all(bind=engine)

@app.get('/', tags=['home'])
def home():
    return RedirectResponse(config('URL') + '/docs')
