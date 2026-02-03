from pydantic import BaseModel
import uuid
from fastapi_users import schemas


class PostCreate(BaseModel):
    caption: str


class PostResponse(BaseModel):
    id: str
    user_id: str
    caption: str
    url: str
    file_type: str
    file_name: str
    created_at: str
    is_owner: bool
    email: str


class UserRead(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass