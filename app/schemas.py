from pydantic import BaseModel, Field
from uuid import UUID

class UserIn(BaseModel):
    username: str
    age: int
    phone_number: str | None = Field(max_length=12, min_length=12)

class UserOut(UserIn):
    uuid: UUID
 