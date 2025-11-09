from sqlalchemy import Column, Integer, String, Enum
from app.core.database import Base
import enum
from passlib.hash import argon2

class UserRole(enum.Enum):
    driver = "driver"
    dispatcher = "dispatcher"
    admin = "admin"


def hash_password(password: str) -> str:
    return argon2.hash(password)
user_input_password = "default_password"
hashed_pw = hash_password(user_input_password)

def verify_password(password: str, hashed: str) -> bool:
    return argon2.verify(password, hashed)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    hashed_pw = hash_password(user_input_password)
    role = Column(Enum(UserRole), default=UserRole.driver, nullable=False)
