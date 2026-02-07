from fastapi import APIRouter, HTTPException, Depends, status
from sqlmodel import Session
from typing import Optional
from src.models.auth_model import UserCreate, UserPublic, Token, LoginRequest
from src.services.auth_service import AuthService
from src.database import engine
from src.utils.auth_utils import create_access_token, verify_token
from datetime import timedelta

# Create the router
router = APIRouter()


def get_session():
    with Session(engine) as session:
        yield session


@router.post("/auth/register", response_model=UserPublic, status_code=201)
def register(user: UserCreate, session: Session = Depends(get_session)):
    """Register a new user."""
    try:
        return AuthService.create_user(session, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/auth/login", response_model=Token)
def login(login_request: LoginRequest, session: Session = Depends(get_session)):
    """Authenticate user and return access token."""
    user = AuthService.authenticate_user(
        session, login_request.email, login_request.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create access token
    access_token_expires = timedelta(minutes=30)  # 30 minutes expiry
    access_token = create_access_token(
        data={"sub": str(user.id), "email": user.email},
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/auth/verify-token", response_model=UserPublic)
def verify_user_token(token: str, session: Session = Depends(get_session)):
    """Verify a token and return user information."""
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = AuthService.get_user_by_id(session, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user