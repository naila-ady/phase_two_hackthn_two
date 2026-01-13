# Usage Guide for Hugging Face Deployment Skill

## Prerequisites

- Python 3.7+ installed
- Git installed and configured
- A Hugging Face account
- A Hugging Face Space created (or ready to create)

## Step-by-Step Process

### 1. Prepare Your Project
Ensure your FastAPI project has:
- A main.py file with a FastAPI app instance
- A requirements.txt file
- A src/ directory with your application code
- Proper structure for deployment

### 2. Apply the Skill
1. Copy the `prepare_hf_space.py` script to your project root
2. Run the script:
   ```
   python prepare_hf_space.py
   ```
3. The script will:
   - Copy necessary files to `todo_task_tracker` directory
   - Update Dockerfile for Hugging Face compatibility
   - Update README.md for Hugging Face Spaces
   - Provide deployment instructions

### 3. Deploy to GitHub (if applicable)
```
git add .
git commit -m "Prepare for Hugging Face deployment"
git push origin main
```

### 4. Deploy to Hugging Face Spaces
1. Navigate to your Hugging Face Space repository:
   ```
   cd /path/to/your/hf/space/repository
   ```

2. Copy the prepared files from `todo_task_tracker`:
   ```
   cp -r /path/to/todo_task_tracker/* .
   ```

3. Commit and push to Hugging Face:
   ```
   git add .
   git commit -m "Update for deployment"
   git push origin main
   ```

### 5. Monitor the Deployment
- Check your Hugging Face Space URL
- Monitor build logs in the Hugging Face dashboard
- Wait for the build to complete successfully

## Common Issues and Solutions

### Docker Build Failures
- Issue: `invalid containerPort: #`
- Solution: Ensure no inline comments after EXPOSE command in Dockerfile

### Runtime Errors
- Issue: `Option '--port' requires an argument`
- Solution: Use `${PORT:-7860}` syntax in Dockerfile CMD

### CORS Issues
- Issue: Cross-origin requests blocked
- Solution: Ensure ALLOWED_ORIGINS is set correctly in environment

## Customization

You can customize the script for different project structures:
- Modify the `items_to_copy` list to include different files/directories
- Adjust file paths in the script as needed
- Update the README.md template for your specific application

## Verification

After deployment, verify functionality by:
- Visiting your Space URL (should show "Welcome to the Todo API")
- Testing API endpoints (e.g., `/api/v1/todos` should return `[]`)
- Checking logs for any errors