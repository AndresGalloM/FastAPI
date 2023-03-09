from fastapi import APIRouter, Path, status, HTTPException
from config.database import Session
from typing import List
from models.movie import Movie


router = APIRouter(
    prefix='/movie',
    tags=['movie']
)


# @router.post('', status_code=status.HTTP_201_CREATED)
# def create_movie(movie: Movie):
#     conexion_db = Session()
#     Movie(**movie.dict())
    