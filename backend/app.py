# This file is required by Hugging Face Spaces to run the application
import os
from src.main import app  # Import the FastAPI app instance

# Hugging Face Spaces looks for a variable named 'app' at the module level
# The 'app' variable in src.main is already a FastAPI instance
# This file serves as the entry point for Hugging Face Spaces