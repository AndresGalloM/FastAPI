import json
from models.movie import Movie
from schemas.movie import Movie as MovieSchema
from config.database import Session

class MovieServices:
    def __init__(self):
        self.session = Session()

    def get_movies(self, parameter: str):
        if parameter:
            movies = self.session.query(Movie).filter(Movie.categories.like(f'%"{parameter}"%')).all()
        else:
            movies = self.session.query(Movie).all()
        
        return movies

    def get_movie(self, id: int):
        return self.session.query(Movie).filter(Movie.id == id).first()

    def create_movie(self, movie: MovieSchema):
        movie.categories = json.dumps(movie.categories)
        self.session.add(Movie(**movie.dict()))
        self.session.commit()

    def update_movie(self, id: int, movie: MovieSchema):
        movie.categories = json.dumps(movie.categories)
        movie.id = id
        updated = self.session.query(Movie).filter(Movie.id == id).update(movie.dict())

        if not updated:
            self.session.close()
            return False

        self.session.commit()

        return True

    def delete_movie(self, id: int):
        eliminated = self.session.query(Movie).filter(Movie.id == id).delete()
        self.session.commit()

        return eliminated
    