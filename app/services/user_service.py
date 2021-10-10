from app.models.user import User
from app.services.repo.user_repo import UserRepoInterface

class UserService:
    def __init__(self, user_repo):
        if not isinstance(user_repo, UserRepoInterface):
            raise ValueError("expected subclass of UserRepoInterface")
        self.user_repo = user_repo

    def create_user(self, user):
        self.user_repo.create_user(user)

    def get_all(self):
        return self.user_repo.get_all()
