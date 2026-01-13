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
        with open(dockerfile_path, 'r') as f:
            dockerfile_content = f.read()

        # Hugging Face Spaces typically let the system assign port via $PORT env var
        # Replace EXPOSE 7860 with EXPOSE $PORT for better compatibility
        # NOTE: Dockerfile doesn't support inline comments after EXPOSE, so we just replace the port
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