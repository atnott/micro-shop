from core.repositories.user import UserRepository

class UserService:

    def __init__(self, repository: UserRepository):
        self.repo = repository

    async def get_all_users(self):
        return await self.repo.get_all_users()
