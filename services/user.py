from config.database import Session
from models.user import User

class UserServices:
    def __init__(self):
        self.session = Session()

    def get_user_by_id(self, id: int):
        return self.session.query(User).filter(User.id == id).first()