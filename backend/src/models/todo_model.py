from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
import uuid

class TodoBase(SQLModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    priority: str = "medium"
    category: Optional[str] = None
    due_date: Optional[datetime] = None

class Todo(TodoBase, table=True):
    __tablename__ = "todos"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class TodoCreate(TodoBase):
    pass

class TodoUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[str] = None
    category: Optional[str] = None
    due_date: Optional[datetime] = None

class TodoResponse(TodoBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime