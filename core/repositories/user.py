from sqlalchemy import insert, select

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import session

from core.models import User

from typing import Sequence

from core.schemas.user import UserCreate


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_all_users(self) -> Sequence[User]:
        stmt = select(User).order_by(User.id)
        result = await self.session.scalars(stmt)
        return result.all()

    async def create_user(self, user: UserCreate) -> User:
        user = User(**user.model_dump())
        self.session.add(user)
        await self.session.commit()
        return user
