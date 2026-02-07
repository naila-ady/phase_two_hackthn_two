# Deployment Guide

This guide explains how to deploy the Todo application to both GitHub (frontend) and Hugging Face Spaces (backend).

## GitHub Deployment (Frontend)

The frontend is built with Next.js and can be deployed to Vercel (recommended) or other platforms.

### Prerequisites
- A GitHub account
- A Vercel account (for frontend deployment)

### Steps
1. Push your frontend code to a GitHub repository
2. Connect your GitHub repository to Vercel
3. Vercel will automatically detect it's a Next.js project and build/deploy it
4. Configure environment variables in Vercel dashboard:
   - `NEXT_PUBLIC_API_URL`: The URL of your backend API

## Hugging Face Spaces Deployment (Backend)

### Prerequisites
- A Hugging Face account
- Git installed locally
- A separate Hugging Face Space repository (cloned from your Hugging Face Space)
- The `todo_task_tracker` directory contains the prepared files for deployment

### Important Note
The `todo_task_tracker` directory in your main project is NOT the same as your Hugging Face Space repository.
It's a prepared set of files that need to be copied to your actual Hugging Face Space repository.

### Steps

1. **Prepare your Hugging Face Space repository**:
   ```bash
   python prepare_hf_space.py
   ```

2. **Navigate to your Hugging Face Space repository** (the cloned repo from Hugging Face):
   ```bash
   cd path/to/your/hf-space-repo
   ```

3. **Copy the prepared files**:
   Copy all files from `todo_task_tracker/` to your Hugging Face Space repository directory.

4. **Commit and push the changes**:
   ```bash
   git add .
   git commit -m "Update for deployment"
   git push
   ```

5. **Wait for the Space to build** (this may take a few minutes)

### Files Required for Hugging Face Deployment
- `app.py`: Entry point for the FastAPI application
- `Dockerfile`: Container configuration for Hugging Face Spaces
- `requirements.txt`: Python dependencies
- `src/`: Source code directory
- `README.md`: Space configuration and description

### Environment Variables for Production
- `DATABASE_URL`: Database connection string (e.g., `postgresql://user:pass@host:port/dbname`)
- `SECRET_KEY`: Secret key for security (use a strong, random key in production)
- `DEBUG`: Set to `False` for production
- `ALLOWED_ORIGINS`: Comma-separated list of allowed origins (e.g., `http://localhost:3000,https://yourdomain.com`)

## Production Considerations

### Security
- Set `DEBUG=False` in production
- Use a strong, unique `SECRET_KEY`
- Specify exact `ALLOWED_ORIGINS` instead of allowing all origins
- Use HTTPS in production
- Regularly update dependencies

### Database
- For production, consider using PostgreSQL instead of SQLite
- Ensure proper backup strategies
- Use connection pooling for better performance

### Performance
- Enable caching where appropriate
- Optimize database queries
- Use a CDN for static assets

## Troubleshooting

### Hugging Face Spaces
- If the build fails, check the build logs in the Space settings
- Ensure all dependencies are listed in `requirements.txt`
- Verify that the Dockerfile exposes the correct port
- Make sure the application can start with the CMD instruction

### CORS Issues
- If you're experiencing CORS issues, verify that `ALLOWED_ORIGINS` includes your frontend URL
- In development, you might need to temporarily allow all origins

### Database Issues
- For SQLite, ensure the database file path is writable
- For PostgreSQL, verify connection parameters and credentials