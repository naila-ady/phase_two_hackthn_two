# Hugging Face Deployment Skill

## Overview
This skill automates the process of preparing and deploying a FastAPI application to Hugging Face Spaces using Docker.

## Purpose
To streamline the deployment of Python web applications to Hugging Face Spaces, including:
- Preparing necessary files for deployment
- Configuring security settings
- Handling environment variables
- Creating proper Docker configuration
- Providing deployment documentation

## Files Created/Modified

### 1. prepare_hf_space.py
```python
#!/usr/bin/env python3
"""
Script to prepare the Hugging Face Space repository for deployment.
This script copies the necessary backend files to your Hugging Face Space repository.
"""

import os
import shutil
import sys
from pathlib import Path

def copy_backend_to_hf_space(backend_dir, hf_space_dir):
    """
    Copy backend files to Hugging Face Space directory
    """
    print(f"Copying backend files from '{backend_dir}' to '{hf_space_dir}'...")

    # Create the destination directory if it doesn't exist
    Path(hf_space_dir).mkdir(parents=True, exist_ok=True)

    # Files and directories to copy from backend
    items_to_copy = ['src', 'app.py', 'Dockerfile', 'requirements.txt']

    for item in items_to_copy:
        src_path = Path(backend_dir) / item
        dest_path = Path(hf_space_dir) / item

        if src_path.exists():
            if src_path.is_dir():
                # Remove destination directory if it exists
                if dest_path.exists():
                    shutil.rmtree(dest_path)
                shutil.copytree(src_path, dest_path)
                print(f"Copied directory: {item}")
            else:
                shutil.copy2(src_path, dest_path)
                print(f"Copied file: {item}")
        else:
            print(f"Warning: {src_path} does not exist")

    # Update the Dockerfile to expose the correct port for Hugging Face
    dockerfile_path = Path(hf_space_dir) / "Dockerfile"
    if dockerfile_path.exists():
        with open(dockerfile_path, 'r', encoding='utf-8') as f:
            dockerfile_content = f.read()

        # Hugging Face Spaces typically let the system assign port via $PORT env var
        # Replace EXPOSE 7860 with EXPOSE $PORT for better compatibility
        dockerfile_content = dockerfile_content.replace(
            "EXPOSE 7860",
            "EXPOSE $PORT"
        )

        # Also update the CMD to handle the PORT environment variable properly
        dockerfile_content = dockerfile_content.replace(
            'CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port $PORT"]',
            'CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-7860}"]'
        )

        with open(dockerfile_path, 'w', encoding='utf-8') as f:
            f.write(dockerfile_content)
        print("Updated Dockerfile for Hugging Face compatibility")

    # Create/update README.md in the Hugging Face Space
    readme_path = Path(hf_space_dir) / "README.md"
    readme_content = """---
title: Todo Task Tracker
emoji: 🏢
colorFrom: gray
colorTo: green
sdk: docker
pinned: false
short_description: A todo application built by using SSD
---

# Todo Task Tracker

This is a full-featured todo application built with FastAPI and SQLModel.

## Features
- Create, read, update, and delete todos
- Filter and sort todos by various criteria
- Track completion status and priorities

## Built With
- FastAPI
- SQLModel
- SQLite (for simplicity)
- Next.js (frontend)

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
"""

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print("Updated README.md for Hugging Face Space")

    print(f"\nSuccessfully prepared Hugging Face Space files in '{hf_space_dir}'")
    print("\nIMPORTANT: The 'todo_task_tracker' directory is NOT your Hugging Face Space repository.")
    print("It contains the prepared files that need to be copied to your actual Hugging Face Space repository.")
    print("\nTo deploy to Hugging Face Spaces:")
    print("1. Navigate to your ACTUAL Hugging Face Space repository (cloned from Hugging Face)")
    print("2. Copy all files from 'todo_task_tracker' to your Hugging Face Space repository")
    print("3. Add and commit these files: git add . && git commit -m 'Update for deployment'")
    print("4. Push to Hugging Face: git push")
    print("\nThe space should automatically rebuild and deploy!")

if __name__ == "__main__":
    backend_dir = "./backend"
    hf_space_dir = "./todo_task_tracker"

    # Allow command line arguments to specify directories
    if len(sys.argv) > 1:
        backend_dir = sys.argv[1]
    if len(sys.argv) > 2:
        hf_space_dir = sys.argv[2]

    copy_backend_to_hf_space(backend_dir, hf_space_dir)
```

### 2. Security Updates to main.py
The following security improvement was made to `backend/src/main.py`:
```python
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
```

### 3. Updated .env file
```bash
# Environment variables for the project
# Add your environment-specific variables here

# Database URL (update with your actual database connection)
# Database URL for PostgreSQL/NeonDB
DATABASE_URL="postgresql://user:password@host:port/database_name"

# Secret key for the application (use a strong, random key in production)
SECRET_KEY="your-super-secret-key-change-this-in-production"

# Debug mode (set to True for development, False for production)
DEBUG=False

# Port for the application to run on
PORT=8000

# Allowed origins for CORS (comma-separated list)
# For production, specify exact origins like: http://yourdomain.com,https://yourdomain.com
ALLOWED_ORIGINS="*"
```

### 4. Updated app.py for Hugging Face
```python
# This file is required by Hugging Face Spaces to run the application
import os
from src.main import app  # Import the FastAPI app instance

# Hugging Face Spaces looks for a variable named 'app' at the module level
# The 'app' variable in src.main is already a FastAPI instance
# This file serves as the entry point for Hugging Face Spaces
```

### 5. Updated Dockerfile for Hugging Face
```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose port (Hugging Face Spaces will use PORT environment variable)
EXPOSE $PORT

# Set environment variables
ENV PYTHONPATH=/app/src

# Run the application with uvicorn
CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-7860}"]
```

## Deployment Process

### 1. Preparation Phase
- Run `python prepare_hf_space.py` to prepare files for Hugging Face deployment
- This copies necessary files to the `todo_task_tracker` directory
- Updates Dockerfile for Hugging Face compatibility
- Creates proper README.md for Hugging Face Spaces

### 2. Security Hardening
- Restricts CORS to specific origins in production
- Sets DEBUG to False for production
- Adds secret key requirement
- Configures proper environment variable handling

### 3. GitHub Push
- Push main project to GitHub with all configuration changes
- Includes updated documentation and deployment guides

### 4. Hugging Face Deployment
- Navigate to actual Hugging Face Space repository
- Copy files from `todo_task_tracker` directory
- Commit and push to Hugging Face
- Monitor build process until completion

## Troubleshooting Common Issues

### Docker Build Errors
- Ensure EXPOSE command doesn't have inline comments
- Verify all dependencies are in requirements.txt

### Runtime Errors
- Use `${PORT:-7860}` syntax to provide default port if environment variable is unset
- Ensure uvicorn command receives proper port argument

### CORS Issues
- Verify ALLOWED_ORIGINS environment variable is set appropriately
- Check that CORS middleware is properly configured

## Reusability
This skill can be applied to any FastAPI application that needs to be deployed to Hugging Face Spaces. Simply:
1. Place the `prepare_hf_space.py` script in your project
2. Adjust paths in the script if needed
3. Run the script to prepare your files
4. Follow the deployment process outlined above

## Key Learnings
- Hugging Face Spaces repository is separate from GitHub repository
- Dockerfile must be properly configured for Hugging Face environment
- Environment variables must be handled correctly
- Security settings need to be production-ready
- CORS configuration should be restrictive in production