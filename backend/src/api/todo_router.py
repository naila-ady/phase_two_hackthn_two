from fastapi import APIRouter, HTTPException, Depends, Query
from sqlmodel import Session
from typing import List, Optional
from src.models.todo_model import (
    TodoCreate, TodoUpdate, TodoResponse
)
from src.services.todo_service import TodoService
from src.database import engine
import os
from src.dependencies.auth_deps import get_current_user, get_session
import uuid

# Create the router
router = APIRouter()

@router.post("/todos", response_model=TodoResponse, status_code=201)
def create_todo(todo: TodoCreate, current_user: dict = Depends(get_current_user), session: Session = Depends(get_session)):
    try:
        # Extract user_id from the current user
        user_id = uuid.UUID(current_user["id"])
        return TodoService.create_todo(session, todo, user_id=user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/todos", response_model=List[TodoResponse])
def read_todos(
    completed: Optional[bool] = Query(None, description="Filter by completion status"),
    priority: Optional[str] = Query(None, description="Filter by priority level"),
    category: Optional[str] = Query(None, description="Filter by category"),
    sort_by: Optional[str] = Query(None, description="Sort by field: priority, due_date, created_at"),
    order: Optional[str] = Query("asc", description="Sort order: asc or desc"),
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Extract user_id from the current user
    user_id = uuid.UUID(current_user["id"])
    return TodoService.get_todos(session, completed, priority, category, sort_by, order, user_id=user_id)

@router.get("/todos/{todo_id}", response_model=TodoResponse)
def read_todo(todo_id: str, current_user: dict = Depends(get_current_user), session: Session = Depends(get_session)):
    # Validate UUID format
    try:
        uuid_obj = uuid.UUID(todo_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")

    # Extract user_id from the current user
    user_id = uuid.UUID(current_user["id"])
    todo = TodoService.get_todo_by_id(session, uuid_obj)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: str, todo: TodoUpdate, current_user: dict = Depends(get_current_user), session: Session = Depends(get_session)):
    # Validate UUID format
    try:
        uuid_obj = uuid.UUID(todo_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")

    # Extract user_id from the current user
    user_id = uuid.UUID(current_user["id"])
    updated_todo = TodoService.update_todo(session, uuid_obj, todo, user_id=user_id)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo

@router.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: str, current_user: dict = Depends(get_current_user), session: Session = Depends(get_session)):
    # Validate UUID format
    try:
        uuid_obj = uuid.UUID(todo_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")

    # Extract user_id from the current user
    user_id = uuid.UUID(current_user["id"])
    success = TodoService.delete_todo(session, uuid_obj, user_id=user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return

@router.patch("/todos/{todo_id}/toggle", response_model=TodoResponse)
def toggle_todo_completion(todo_id: str, current_user: dict = Depends(get_current_user), session: Session = Depends(get_session)):
    # Validate UUID format
    try:
        uuid_obj = uuid.UUID(todo_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")

    # Extract user_id from the current user
    user_id = uuid.UUID(current_user["id"])
    todo = TodoService.toggle_todo_completion(session, uuid_obj, user_id=user_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo