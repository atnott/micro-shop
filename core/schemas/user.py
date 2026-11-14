from pydantic import BaseModel

class UserBaseSchema(BaseModel):
    name: str

class UserCreate(UserBaseSchema):
    pass

class UserRead(UserBaseSchema):
    id: int
