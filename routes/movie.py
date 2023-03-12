import json
from fastapi import APIRouter, Path, Query, status
from fastapi.responses import JSONResponse
from config.database import Session
from typing import List, Dict, Union
from models.movie import Movie
from schemas.movie import Movie as MovieSchema 


router = APIRouter(
    prefix='/api/v1/movie',
    tags=['movie']
)

@router.get('', response_model=Union[List, Dict])
async def get_movie_by_category(category: str = Query(None, max_length=20, min_length=3)):
    if category:
        movies = Session().query(Movie).filter(Movie.categories.like(f'%"{category}"%')).all()
    else:
        movies = Session().query(Movie).all()
    
    if movies:
        return MovieSchema.convert_movies(movies)

    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={'error': {'message': 'No movies found'}}
    )

@router.get('/{id}', response_model=Dict)
async def one_movie(id: int = Path(..., gt=0)):
    movie = Session().query(Movie).filter(Movie.id == id).first()

    if movie:
        return MovieSchema.convert_movie(movie)

    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={'error': {'message': 'The movie does not exist'}}
    )

@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=Union[MovieSchema, Dict],
    description='Operation to create a new movie'
)
async def create_movie(movie: MovieSchema):
    try:
        movie.categories = json.dumps(movie.categories)
        session = Session()
        session.add(Movie(**movie.dict()))
        session.commit()

        return MovieSchema.convert_movie(movie)
    except Exception as ex:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={'error': {'message': f'Error creating movie: {ex.__cause__}'}}
        )

@router.put('/{id}', response_model=Dict)
def update_movie(movie: MovieSchema, id: int = Path(..., gt=0)):
    session = Session()

    movie.categories = json.dumps(movie.categories)
    movie.id = id
    updated = session.query(Movie).filter(Movie.id == id).update(movie.dict())  
    
    if not updated:
        session.close()
        raise JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={'error': {'message': 'Movie no found'}}
        )
    
    session.commit()
        
    return MovieSchema.convert_movie(movie)

@router.delete('/{id}')
def delete_movie(id: int = Path(..., gt=0)):
    session = Session()
    eliminated = session.query(Movie).filter(Movie.id == id).delete()
    session.commit()

    if not eliminated:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={'error': {'message': 'The movie does not exist'}}
        )
    
    return JSONResponse(
        content={'message': 'The movie was successfully removed.'},
        status_code=status.HTTP_201_CREATED
    )
