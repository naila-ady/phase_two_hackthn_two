# NeonDB/PostgreSQL Connection Setup Skill

This skill provides a quick way to set up and connect to a NeonDB/PostgreSQL database, replacing SQLite in your application.

## Overview
This skill helps quickly configure your application to use PostgreSQL/NeonDB instead of SQLite with all necessary code changes and configuration.

## Files to Update

### 1. Database Configuration (`src/database.py`)
```python
from sqlmodel import create_engine
import os

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is required")

# Create the engine
engine = create_engine(DATABASE_URL, echo=True)

def get_engine():
    return engine
```

### 2. Environment Variables (`.env`)
```
# Database URL for PostgreSQL/NeonDB
DATABASE_URL="postgresql://username:password@hostname:port/database_name"

# Example for NeonDB:
# DATABASE_URL="postgresql://neondb_owner:your_password@ep-cool-sky-123456.us-east-2.aws.neon.tech/neondb?sslmode=require"
```

### 3. Requirements (`requirements.txt`)
```
# Add PostgreSQL driver
psycopg2-binary==2.9.9
```

### 4. Alembic Configuration (`alembic.ini`)
```
sqlalchemy.url =  ${DATABASE_URL}
```

### 5. Main Application Startup (`src/main.py`)
```python
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
```

## Quick Steps to Replace SQLite with PostgreSQL/NeonDB

1. **Install PostgreSQL Driver**
   ```bash
   pip install psycopg2-binary
   ```

2. **Update your .env file** with PostgreSQL connection string:
   ```
   DATABASE_URL="postgresql://username:password@hostname:port/database_name"
   ```

3. **Update database.py** to remove SQLite fallback

4. **Update requirements.txt** to include psycopg2-binary

5. **Test the connection**:
   ```python
   import os
   from dotenv import load_dotenv
   load_dotenv()
   from src.database import engine
   print('Database engine created successfully')
   ```

## Connecting to NeonDB in pgAdmin

To connect your NeonDB database to pgAdmin, use these connection details:

| Field | Value |
|-------|--------|
| Host | `ep-cool-sky-123456.us-east-2.aws.neon.tech` |
| Database | `neondb` |
| Username | `neondb_owner` |
| Password | Your NeonDB password |
| Port | `5432` |

Steps:
1. Open pgAdmin
2. Right-click on "Servers" → "Create" → "Server"
3. In the "General" tab, give the server a name (e.g., "NeonDB")
4. In the "Connection" tab:
   - Host: Enter your NeonDB hostname (e.g., `ep-cool-sky-123456.us-east-2.aws.neon.tech`)
   - Port: 5432
   - Maintenance database: neondb
   - Username: neondb_owner
   - Password: Your NeonDB password
5. Click "Save"

## NeonDB Connection String Format

```
postgresql://username:password@hostname:port/database_name?sslmode=require
```

Example:
```
postgresql://neondb_owner:your_password@ep-cool-sky-123456.us-east-2.aws.neon.tech/neondb?sslmode=require
```

## Troubleshooting

1. **Connection Issues**: Ensure SSL mode is set to `require` in your connection string
2. **Authentication Errors**: Verify your username, password, and database name
3. **Driver Issues**: Make sure psycopg2-binary is installed

## Common NeonDB Connection Parameters

- SSL Mode: `require` (recommended for NeonDB)
- Channel Binding: `require` (may be needed depending on your setup)
- Pool size: Configure based on your application needs

## Example NeonDB Connection String with Additional Parameters

```
postgresql://neondb_owner:password@ep-cool-sky-123456.us-east-2.aws.neon.tech/neondb?sslmode=require&connect_timeout=10
```

This skill provides a complete solution for quickly setting up PostgreSQL/NeonDB connections in your application, replacing SQLite with minimal configuration changes.