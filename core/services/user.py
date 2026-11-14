from core.models import User
from core.repositories.user import UserRepository
from core.schemas.user import UserCreate

class UserService:

    def __init__(self, repository: UserRepository):
        self.repo = repository

    async def get_all_users(self) -> list[User]:
        return await self.repo.get_all_users()

    async def create_user(self, user: UserCreate) -> User:
        return await self.repo.create_user(user)
