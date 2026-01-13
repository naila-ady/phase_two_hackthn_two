# Hugging Face Deployment Skill

This skill provides a complete solution for deploying FastAPI applications to Hugging Face Spaces.

## What This Skill Does

1. **Prepares your application** for Hugging Face deployment by organizing files correctly
2. **Secures your application** by configuring proper CORS and environment settings
3. **Creates deployment documentation** with step-by-step instructions
4. **Handles common deployment issues** like port configuration and Docker syntax

## Files Included

- `prepare_hf_space.py` - Main script to prepare files for Hugging Face
- `SKILLS.md` - Complete documentation of the process
- `DEPLOYMENT.md` - General deployment guide
- `DEPLOYMENT_STEPS.md` - Step-by-step instructions
- `DEPLOYMENT_COMMANDS.txt` - Exact commands to run

## Usage

1. Place the `prepare_hf_space.py` script in your project root
2. Run: `python prepare_hf_space.py`
3. Follow the deployment instructions in the output
4. Push the prepared files to your Hugging Face Space repository

## Key Benefits

- **Security First**: Fixes common security issues (CORS misconfiguration)
- **Hugging Face Optimized**: Proper Docker configuration for Hugging Face Spaces
- **Environment Aware**: Handles environment variables correctly
- **Error Resilient**: Addresses common deployment pitfalls

## Requirements

- Python 3.7+
- Git
- Access to Hugging Face Spaces