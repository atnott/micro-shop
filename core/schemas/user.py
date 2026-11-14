from pydantic import BaseModel, Field

class UserBaseSchema(BaseModel):
    # id: int
    name: str = Field(min_length=2, max_length=30)

class UserCreate(UserBaseSchema):
    pass

class UserRead(UserBaseSchema):
    id: int
