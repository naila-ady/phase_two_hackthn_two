from typing import List, Optional
from sqlmodel import Session, select
from src.models.todo_model import Todo, TodoCreate, TodoUpdate, TodoResponse
from datetime import datetime
import uuid

class TodoService:
    @staticmethod
    def create_todo(session: Session, todo: TodoCreate, user_id: Optional[uuid.UUID] = None) -> TodoResponse:
        # Validate the title is not empty
        if not todo.title or len(todo.title.strip()) == 0:
            raise ValueError("Title must not be empty")

        # Priority is validated by the enum, so no need for manual validation

        db_todo = Todo(
            title=todo.title,
            description=todo.description,
            completed=todo.completed,
            priority=todo.priority,
            category=todo.category,
            due_date=todo.due_date,
            user_id=user_id,  # Associate with user
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)
        return TodoResponse(
            title=db_todo.title,
            description=db_todo.description,
            completed=db_todo.completed,
            priority=db_todo.priority,
            category=db_todo.category,
            due_date=db_todo.due_date,
            id=db_todo.id,
            user_id=db_todo.user_id,
            created_at=db_todo.created_at,
            updated_at=db_todo.updated_at
        )

    @staticmethod
    def get_todo_by_id(session: Session, todo_id: uuid.UUID) -> Optional[TodoResponse]:
        statement = select(Todo).where(Todo.id == todo_id)
        db_todo = session.exec(statement).first()
        if db_todo:
            return TodoResponse(
                title=db_todo.title,
                description=db_todo.description,
                completed=db_todo.completed,
                priority=db_todo.priority,
                category=db_todo.category,
                due_date=db_todo.due_date,
                id=db_todo.id,
                user_id=db_todo.user_id,
                created_at=db_todo.created_at,
                updated_at=db_todo.updated_at
            )
        return None

    @staticmethod
    def get_todos(
        session: Session,
        completed: Optional[bool] = None,
        priority: Optional[str] = None,
        category: Optional[str] = None,
        sort_by: Optional[str] = None,
        order: Optional[str] = "asc",
        user_id: Optional[uuid.UUID] = None  # Filter by user
    ) -> List[TodoResponse]:
        statement = select(Todo)

        # Filter by user if provided
        if user_id is not None:
            statement = statement.where(Todo.user_id == user_id)

        if completed is not None:
            statement = statement.where(Todo.completed == completed)
        if priority is not None:
            statement = statement.where(Todo.priority == priority)
        if category is not None:
            statement = statement.where(Todo.category == category)

        # Apply sorting
        if sort_by == "priority":
            if order == "desc":
                statement = statement.order_by(Todo.priority.desc())
            else:
                statement = statement.order_by(Todo.priority.asc())
        elif sort_by == "due_date":
            if order == "desc":
                statement = statement.order_by(Todo.due_date.desc())
            else:
                statement = statement.order_by(Todo.due_date.asc())
        elif sort_by == "created_at":
            if order == "desc":
                statement = statement.order_by(Todo.created_at.desc())
            else:
                statement = statement.order_by(Todo.created_at.asc())
        else:
            # Default sorting by created_at descending
            statement = statement.order_by(Todo.created_at.desc())

        results = session.exec(statement).all()
        return [
            TodoResponse(
                title=todo.title,
                description=todo.description,
                completed=todo.completed,
                priority=todo.priority,
                category=todo.category,
                due_date=todo.due_date,
                id=todo.id,
                user_id=todo.user_id,
                created_at=todo.created_at,
                updated_at=todo.updated_at
            )
            for todo in results
        ]

    @staticmethod
    def update_todo(session: Session, todo_id: uuid.UUID, todo_update: TodoUpdate, user_id: Optional[uuid.UUID] = None) -> Optional[TodoResponse]:
        statement = select(Todo).where(Todo.id == todo_id)

        # If user_id is provided, ensure the todo belongs to the user
        if user_id is not None:
            statement = statement.where(Todo.user_id == user_id)

        db_todo = session.exec(statement).first()

        if not db_todo:
            return None

        # Update only the fields that are provided
        update_data = todo_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            if value is not None:
                # Validate title if it's being updated
                if field == "title" and value and len(value.strip()) == 0:
                    raise ValueError("Title must not be empty")
                # Validate priority if it's being updated
                if field == "priority" and value and value not in ["low", "medium", "high"]:
                    raise ValueError("Priority must be low, medium, or high")
                setattr(db_todo, field, value)

        # Update the updated_at timestamp
        db_todo.updated_at = datetime.utcnow()

        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)

        return TodoResponse(
            title=db_todo.title,
            description=db_todo.description,
            completed=db_todo.completed,
            priority=db_todo.priority,
            category=db_todo.category,
            due_date=db_todo.due_date,
            id=db_todo.id,
            user_id=db_todo.user_id,
            created_at=db_todo.created_at,
            updated_at=db_todo.updated_at
        )

    @staticmethod
    def delete_todo(session: Session, todo_id: uuid.UUID, user_id: Optional[uuid.UUID] = None) -> bool:
        statement = select(Todo).where(Todo.id == todo_id)

        # If user_id is provided, ensure the todo belongs to the user
        if user_id is not None:
            statement = statement.where(Todo.user_id == user_id)

        db_todo = session.exec(statement).first()

        if not db_todo:
            return False

        session.delete(db_todo)
        session.commit()
        return True

    @staticmethod
    def toggle_todo_completion(session: Session, todo_id: uuid.UUID, user_id: Optional[uuid.UUID] = None) -> Optional[TodoResponse]:
        statement = select(Todo).where(Todo.id == todo_id)

        # If user_id is provided, ensure the todo belongs to the user
        if user_id is not None:
            statement = statement.where(Todo.user_id == user_id)

        db_todo = session.exec(statement).first()

        if not db_todo:
            return None

        # Toggle the completion status
        db_todo.completed = not db_todo.completed
        db_todo.updated_at = datetime.utcnow()

        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)

        return TodoResponse(
            title=db_todo.title,
            description=db_todo.description,
            completed=db_todo.completed,
            priority=db_todo.priority,
            category=db_todo.category,
            due_date=db_todo.due_date,
            id=db_todo.id,
            user_id=db_todo.user_id,
            created_at=db_todo.created_at,
            updated_at=db_todo.updated_at
        )