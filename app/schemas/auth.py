from pydantic import BaseModel, EmailStr
from enum import Enum

class RoleEnum(str, Enum):
    driver = "driver"
    dispatcher = "dispatcher"
    admin = "admin"

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: RoleEnum

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: RoleEnum
class Login(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
