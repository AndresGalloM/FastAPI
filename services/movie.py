from models.movie import Movie
from config.database import Session

class MovieServices:
    def __init__(self):
        self.session = Session()

    def get_movies(self, parameter):
        if parameter:
            movies = self.session.query(Movie).filter(Movie.categories.like(f'%"{parameter}"%')).all()
        else:
            movies = self.session.query(Movie).all()
        
        return movies

    def get_movie(self, id):
        return self.session.query(Movie).filter(Movie.id == id).first()
