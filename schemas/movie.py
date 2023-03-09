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
