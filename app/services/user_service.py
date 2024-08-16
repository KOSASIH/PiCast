from app.models.user import User
from app.utils.db_utils import session

class UserService:
    @staticmethod
    def get_all_users():
        return session.query(User).all()

    @staticmethod
    def get_user_by_id(user_id):
        return session.query(User).get(user_id)
