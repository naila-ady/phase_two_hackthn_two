from fastapi import FastAPI
from src.api.todo_router import router as todo_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title="Todo API",
    description="A simple todo application API",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the todo router
app.include_router(todo_router, prefix="/api/v1", tags=["todos"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)