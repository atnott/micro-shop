from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.repositories import UserRepository
from core.services import UserService


def get_user_service(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> UserService:
    repo = UserRepository(session=session)
    return UserService(repository=repo)
