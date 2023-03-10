import json
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date


class Movie(BaseModel):
    id: Optional[int] = Field(None, gt=0)
    title: str = Field(..., min_length=5, max_length=50)
    overview: str = Field(..., min_length=1, max_length=500)
    categories: List
    year: date
    disabled: bool

    class Config:
        schema_extra = {
            'example': {
                'id': 0,
                'title': 'Harry potter',
                'overview': '.',
                'category': ['Action', 'Comedy'],
                'year': '2023-03-09',
                'disabled': False
            }
        }

    def convert_movie(movie):
        return {
            'id': movie.id,
            'title': movie.title,
            'overview': movie.overview,
            'categories': json.loads(movie.categories),
            'year': movie.year,
            'disabled': movie.disabled
        }

    def convert_movies(movies):
        list_movies = []

        for movie in movies:
            list_movies.append({
                'id': movie.id,
                'title': movie.title,
                'overview': movie.overview,
                'categories': json.loads(movie.categories),
                'year': movie.year,
                'disabled': movie.disabled
            })

        return list_movies
