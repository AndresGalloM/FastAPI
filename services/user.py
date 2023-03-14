from config.database import Session
from models.user import User

class UserServices:
    def __init__(self):
        self.session = Session()

    def get_user(self, user: str, password: str):
        return self.session.query(User).filter(
            User.name == user, User.password == password
        ).first()