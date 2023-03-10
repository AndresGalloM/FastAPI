import json
from fastapi import APIRouter, Path, status, HTTPException
from fastapi.encoders import jsonable_encoder
from config.database import Session
from typing import List, Dict, Union
from models.movie import Movie
from schemas.movie import Movie as MovieSchema 


router = APIRouter(
    prefix='/api/v1/movie',
    tags=['movie']
)

@router.get('', response_model=List)
def all_movies():
    movies = Session().query(Movie).all()

    if movies:
        return MovieSchema.convert_movies(movies)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Error getting the movies'
    )

@router.get('/{id}', response_model=Dict)
def one_movie(id: int = Path(..., gt=0)):
    movie = Session().query(Movie).filter(Movie.id == id).first()

    if movie:
        return MovieSchema.convert_movie(movie)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='The movie does not exist'
    )

@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    # response_model=Union[MovieSchema, Dict],
    description='Operation to create a new movie'
)
def create_movie(movie: MovieSchema):
    try:
        movie.categories = json.dumps(movie.categories)
        session = Session()
        new_movie = Movie(**movie.dict())
        session.add(new_movie)
        session.commit()
        
        return MovieSchema.convert_movie(movie)
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Error creating movie: {ex.__cause__}'
        )

