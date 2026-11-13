from pydantic import BaseModel, Field

class CreateUser(BaseModel):
    name: str = Field(min_length=2, max_length=20)
    age: int = Field(ge=1, lt=130)

