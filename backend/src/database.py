from sqlmodel import create_engine
import os

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todos.db")

# Create the engine
engine = create_engine(DATABASE_URL, echo=True)

def get_engine():
    return engine