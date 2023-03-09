from fastapi import APIRouter, Path, status, HTTPException
from config.database import Session
from typing import List, Dict, Union
from models.movie import Movie
from schemas.movie import Movie as MovieSchema 


router = APIRouter(
    prefix='/movie',
    tags=['movie']
)


@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    # response_model=Union[MovieSchema, Dict],
    description='Operation to create a new movie'
)
def create_movie(movie: MovieSchema):
    try:
        movie.categories = str(movie.categories)
        conexion_db = Session()
        new_movie = Movie(**movie.dict())
        conexion_db.add(new_movie)
        conexion_db.commit()
        
        return movie
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Error creating movie: {ex.__cause__}'
        )

