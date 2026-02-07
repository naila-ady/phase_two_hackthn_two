# JWT Secret Generator Skill

## Purpose
When a user requests to generate a secure JWT secret key, provide them with methods to create cryptographically secure secrets using Python's secrets module.

## Implementation Steps

1. **Provide Python one-liner command**:
   ```bash
   python -c "import secrets; print('JWT Secret:', secrets.token_urlsafe(32))"
   ```

2. **Offer different formats**:
   - URL-safe base64 format: `secrets.token_urlsafe(length)`
   - Hexadecimal format: `secrets.token_hex(length)`

3. **Recommend secure lengths**:
   - Development: 32 bytes
   - Production: 64 bytes or more

4. **Provide usage instructions**:
   - Add to .env file as `JWT_SECRET_KEY=your_generated_secret`
   - Never commit to version control
   - Use different secrets for different environments

## Example Commands

### Quick Generation
```bash
# 32-byte URL-safe secret (recommended for development)
python -c "import secrets; print('JWT Secret:', secrets.token_urlsafe(32))"

# 64-byte URL-safe secret (recommended for production)
python -c "import secrets; print('JWT Secret:', secrets.token_urlsafe(64))"

# 32-byte hex secret
python -c "import secrets; print('JWT Secret (hex):', secrets.token_hex(32))"

# 64-byte hex secret
python -c "import secrets; print('JWT Secret (hex):', secrets.token_hex(64))"
```

### Using the Provided Script
```bash
# Run the provided script with default settings
python generate_jwt_secret.py

# With custom length
python generate_jwt_secret.py --length 64

# With hex format
python generate_jwt_secret.py --hex --length 32
```

## Security Best Practices

1. **Never commit secrets to version control**
2. **Use environment variables for storing secrets**
3. **Rotate secrets periodically**
4. **Use longer secrets for production (64+ bytes)**
5. **Keep secrets in a secure location**
6. **Use different secrets for different environments**

## Environment Variable Setup

After generating the secret, add it to your `.env` file:
```
JWT_SECRET_KEY=your_generated_secret_here
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
```

## Backend Integration

Use the secret in your FastAPI backend:
```python
from datetime import datetime, timedelta
from jose import JWTError, jwt
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY")  # Your generated secret
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
```

## Validation

To verify your secret is properly formatted:
```python
import os
from dotenv import load_dotenv

load_dotenv()
secret = os.getenv("JWT_SECRET_KEY")

if not secret:
    print("Error: JWT_SECRET_KEY not found in environment")
elif len(secret) < 32:
    print(f"Warning: Secret is {len(secret)} characters - consider using at least 32 characters for security")
else:
    print(f"✓ Secret is properly configured with {len(secret)} characters")
```

## Common Issues and Solutions

**Issue**: "ModuleNotFoundError: No module named 'secrets'"
**Solution**: The 'secrets' module is built into Python 3.6+, ensure you're using Python 3.6 or higher

**Issue**: Secret appears in terminal history
**Solution**: Consider using a password manager or secure vault for production secrets

**Issue**: Need to regenerate secret
**Solution**: Simply run the generation command again and update your .env file