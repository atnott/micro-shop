from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import session

from core.models import User

from typing import Sequence


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_all_users(self) -> Sequence[User]:
        stmt = select(User).order_by(User.id)
        result = await self.session.scalars(stmt)
        return result.all()
