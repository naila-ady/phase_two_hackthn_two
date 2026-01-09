"""
Test script to validate data persistence in the database
"""
import asyncio
from sqlmodel import Session, select
from src.database import engine
from src.models.todo_model import Todo, Priority
from datetime import datetime

def test_data_persistence():
    print("Testing data persistence...")

    # Create a new todo
    new_todo = Todo(
        title="Test persistence",
        description="This is a test todo to validate persistence",
        priority=Priority.medium,
        category="test",
        due_date=datetime(2026, 12, 31)
    )

    # Insert the todo into the database
    with Session(engine) as session:
        session.add(new_todo)
        session.commit()
        session.refresh(new_todo)

        print(f"Created todo with ID: {new_todo.id}")
        print(f"Title: {new_todo.title}")
        print(f"Created at: {new_todo.created_at}")

    # Retrieve the todo from the database to verify it persists
    with Session(engine) as session:
        retrieved_todo = session.exec(select(Todo).where(Todo.id == new_todo.id)).first()

        if retrieved_todo:
            print(f"Successfully retrieved todo with ID: {retrieved_todo.id}")
            print(f"Title: {retrieved_todo.title}")
            print(f"Created at: {retrieved_todo.created_at}")
            print("✅ Data persistence validation successful!")
        else:
            print("❌ Failed to retrieve the todo - persistence not working")

    # Clean up the test data
    with Session(engine) as session:
        session.delete(new_todo)
        session.commit()
        print("Test data cleaned up.")

if __name__ == "__main__":
    test_data_persistence()