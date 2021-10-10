from app.services.repo.user_repo import UserRepoInterface
from app.models.user import User

class UserRepo(UserRepoInterface):
    def __init__(self):
        self.users = []
    
    def create_user(self, user):
        if not isinstance(user, User):
            raise ValueError("input is not User")
        self.users.append(user)

    def get_all(self):
        return self.users