from sqlmodel import create_engine
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is required")

# Create the engine
engine = create_engine(DATABASE_URL, echo=True)

def get_engine():
    return engine