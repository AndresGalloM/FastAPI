from pydantic import BaseModel, Field
from typing import Optional, List

class Movie(BaseModel):
    id: Optional[int] = Field(None, gt=0)
    title: str = Field(..., min_length=5, max_length=50)
    overview: str = Field(..., min_length=1, max_length=100)
    category: List
    year: str = Field(..., min_length=10, max_length=10)
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
