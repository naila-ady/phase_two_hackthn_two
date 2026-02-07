from sqlmodel import Session, select
from typing import Optional
from src.models.auth_model import User, UserCreate, UserPublic
from src.utils.auth_utils import get_password_hash, verify_password
from src.models.todo_model import Todo
from datetime import datetime
import uuid


class AuthService:
    @staticmethod
    def create_user(session: Session, user_create: UserCreate) -> UserPublic:
        """Create a new user with hashed password."""
        # Check if user already exists
        existing_user = session.exec(select(User).where(User.email == user_create.email)).first()
        if existing_user:
            raise ValueError("Email already registered")

        # Hash the password
        hashed_password = get_password_hash(user_create.password)

        # Create the user
        db_user = User(
            name=user_create.name,
            email=user_create.email,
            hashed_password=hashed_password,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        session.add(db_user)
        session.commit()
        session.refresh(db_user)

        return UserPublic(
            id=db_user.id,
            name=db_user.name,
            email=db_user.email,
            is_active=db_user.is_active,
            created_at=db_user.created_at,
            updated_at=db_user.updated_at
        )

    @staticmethod
    def authenticate_user(session: Session, email: str, password: str) -> Optional[UserPublic]:
        """Authenticate user with email and password."""
        user = session.exec(select(User).where(User.email == email)).first()

        if not user or not verify_password(password, user.hashed_password):
            return None

        # Return user data as UserPublic
        return UserPublic(
            id=user.id,
            name=user.name,
            email=user.email,
            is_active=user.is_active,
            created_at=user.created_at,
            updated_at=user.updated_at
        )

    @staticmethod
    def get_user_by_email(session: Session, email: str) -> Optional[UserPublic]:
        """Get a user by email."""
        user = session.exec(select(User).where(User.email == email)).first()

        if not user:
            return None

        return UserPublic(
            id=user.id,
            name=user.name,
            email=user.email,
            is_active=user.is_active,
            created_at=user.created_at,
            updated_at=user.updated_at
        )

    @staticmethod
    def get_user_by_id(session: Session, user_id: uuid.UUID) -> Optional[UserPublic]:
        """Get a user by ID."""
        user = session.exec(select(User).where(User.id == user_id)).first()

        if not user:
            return None

        return UserPublic(
            id=user.id,
            name=user.name,
            email=user.email,
            is_active=user.is_active,
            created_at=user.created_at,
            updated_at=user.updated_at
        )

    @staticmethod
    def deactivate_user(session: Session, user_id: uuid.UUID) -> bool:
        """Deactivate a user account."""
        user = session.exec(select(User).where(User.id == user_id)).first()

        if not user:
            return False

        user.is_active = False
        user.updated_at = datetime.utcnow()

        session.add(user)
        session.commit()
        session.refresh(user)

        return True