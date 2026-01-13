from fastapi import FastAPI
from src.api.todo_router import router as todo_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from src.database import engine
from src.models.todo_model import Todo

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
    allowed_origins = ["*"] if os.getenv("DEBUG", "True").lower() == "true" else []

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
    Todo.metadata.create_all(bind=engine)

# Include the todo router
app.include_router(todo_router, prefix="/api/v1", tags=["todos"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)