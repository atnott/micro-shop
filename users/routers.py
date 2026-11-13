from fastapi import APIRouter

from users.schemas import CreateUser
from users import service

router = APIRouter(prefix='/users')

@router.post('/')
def create_user(user: CreateUser) -> dict:
    return service.create_user(user)
