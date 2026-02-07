from fastapi import FastAPI
from src.api.todo_router import router as todo_router
from src.api.auth_router import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from src.database import engine
from src.models.todo_model import Todo
from src.models.auth_model import User
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Todo API",
    description="A simple todo application API",
    version="1.0.0"
)

# Add CORS middleware
# In production, specify exact origins rather than allowing all
import os
from dotenv import load_dotenv

load_dotenv()

# Get allowed origins from environment variables
allowed_origins = os.getenv("ALLOWED_ORIGINS", "").split(",")
if not allowed_origins or allowed_origins == [""]:
    # Default to allowing all in development, but in production specify exact origins
    if os.getenv("DEBUG", "True").lower() == "true":
        allowed_origins = ["*"]
    else:
        # In production, allow common origins including Vercel deployments
        allowed_origins = [
            "https://nkamdar-todo-task-tracker.hf.space",
            "https://phase-two-hackthn-two.vercel.app",  # Your Vercel domain
            # Add other domains as needed
        ]
else:
    # Clean up any empty strings from the split
    allowed_origins = [origin.strip() for origin in allowed_origins if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
)

# Create database tables
@app.on_event("startup")
def on_startup():
    # For PostgreSQL, it's better to use Alembic for schema management
    # But we'll keep this for initial setup
    try:
        Todo.metadata.create_all(bind=engine)
        User.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Error creating tables: {e}")

# Include the routers
app.include_router(todo_router, prefix="/api/v1", tags=["todos"])
app.include_router(auth_router, prefix="/api/v1", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)