from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
import uuid
import hashlib
import secrets


def hash_password(password: str) -> str:
    """Hash a password with a salt."""
    salt = secrets.token_hex(32)
    pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
    return f"{salt}:{pwdhash.hex()}"


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hashed password."""
    salt, pwdhash = hashed_password.split(':')
    computed_hash = hashlib.pbkdf2_hmac('sha256', plain_password.encode('utf-8'), salt.encode('utf-8'), 100000)
    return computed_hash.hex() == pwdhash


class UserBase(SQLModel):
    email: str = Field(unique=True, nullable=False)
    name: str = Field(nullable=False)


class User(UserBase, table=True):
    __tablename__ = "users"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str = Field(nullable=False)
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class UserCreate(UserBase):
    password: str


class UserUpdate(SQLModel):
    name: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None


class UserPublic(UserBase):
    id: uuid.UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(SQLModel):
    user_id: uuid.UUID
    email: str


class LoginRequest(SQLModel):
    email: str
    password: str