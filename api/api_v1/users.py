from typing import Annotated
from fastapi import APIRouter, Depends

from core.dependencies import get_user_service
from core.schemas.user import UserCreate, UserRead
from core.services import UserService

router = APIRouter(
    tags=['Users'],
)

@router.get('')
async def get_users(
    service: Annotated[UserService, Depends(get_user_service)]
):
    return await service.get_all_users()

@router.post('')
async def create_user(
    service: Annotated[UserService, Depends(get_user_service)],
    user: UserCreate,
) -> UserRead:
    return await service.create_user(user)
