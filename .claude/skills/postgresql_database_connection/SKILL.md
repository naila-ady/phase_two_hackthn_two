# PostgreSQL Database Connection Setup Skill

This skill provides a quick way to set up and connect to a PostgreSQL database, whether using NeonDB cloud service or a local PostgreSQL installation.

## Overview
This skill helps quickly configure your application to use PostgreSQL instead of SQLite, supporting both cloud (NeonDB) and local PostgreSQL installations.

## Connection Types

### A. Local PostgreSQL Connection

#### Prerequisites
- PostgreSQL must be installed and running locally
- PostgreSQL should be accessible on port 5432 (default)
- You should have admin access to PostgreSQL

#### Steps for Local PostgreSQL Setup

1. **Create PostgreSQL Database**
   Connect to PostgreSQL and create the required database:
   ```bash
   psql -h localhost -p 5432 -U postgres -d postgres
   ```

   In the PostgreSQL prompt, run:
   ```sql
   CREATE DATABASE todos_db;
   CREATE USER todos_user WITH PASSWORD 'strong_password';
   GRANT ALL PRIVILEGES ON DATABASE todos_db TO todos_user;
   \q
   ```

2. **Configure Environment Variables**
   Create a .env file in the backend directory with database credentials:
   ```bash
   cd backend
   echo DATABASE_URL=postgresql://todos_user:strong_password@localhost:5432/todos_db > .env
   ```

3. **Alternative: Using Default PostgreSQL User**
   ```bash
   echo DATABASE_URL=postgresql://postgres:your_password@localhost:5432/todos_db >> .env
   ```

### B. NeonDB Connection

1. **Get Your NeonDB Connection Details**
   From your NeonDB dashboard, copy the connection string:
   ```
   postgresql://neondb_owner:password@ep-cool-sky-123456.us-east-2.aws.neon.tech/neondb?sslmode=require
   ```

2. **Configure Environment Variables**
   ```bash
   cd backend
   echo DATABASE_URL=postgresql://neondb_owner:your_password@ep-cool-sky-123456.us-east-2.aws.neon.tech/neondb?sslmode=require > .env
   ```

## Files to Update

### 1. Database Configuration (`src/database.py`)
```python
from sqlmodel import create_engine
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is required")

# Create the engine
engine = create_engine(DATABASE_URL, echo=True)

def get_engine():
    return engine
```

### 2. Environment Variables (`.env` and `.env.example`)
```
# Database URL for PostgreSQL
DATABASE_URL="postgresql://username:password@hostname:port/database_name"
SECRET_KEY="your_secret_key"
JWT_SECRET_KEY="your_jwt_secret_key"
DEBUG=True
PORT=8000

# Examples:
# Local PostgreSQL: postgresql://todos_user:password@localhost:5432/todos_db
# NeonDB: postgresql://neondb_owner:password@ep-cool-sky-123456.region.aws.neon.tech/neondb?sslmode=require
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
# Load environment variables
import os
from dotenv import load_dotenv
load_dotenv()

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

### 6. Environment Variable Loading
To ensure your environment variables are loaded properly, make sure to call `load_dotenv()` in both your database configuration and main application files.

## Quick Setup Steps

### For Local PostgreSQL:

1. **Install PostgreSQL** (if not already installed)
   - Download from https://www.postgresql.org/download/
   - Follow installation instructions
   - Remember your superuser password

2. **Install PostgreSQL Driver**
   ```bash
   pip install psycopg2-binary
   ```

3. **Create Database and User**
   ```bash
   psql -h localhost -p 5432 -U postgres -d postgres
   ```
   ```sql
   CREATE DATABASE todos_db;
   CREATE USER todos_user WITH PASSWORD 'strong_password';
   GRANT ALL PRIVILEGES ON DATABASE todos_db TO todos_user;
   \q
   ```

4. **Update your .env file**:
   ```
   DATABASE_URL="postgresql://todos_user:strong_password@localhost:5432/todos_db"
   SECRET_KEY="your_generated_secret_key"
   JWT_SECRET_KEY="your_generated_jwt_secret_key"
   DEBUG=True
   PORT=8000
   ```

5. **Run database migrations**:
   ```bash
   alembic upgrade head
   ```

6. **Run the application**:
   ```bash
   cd backend
   python -m src.main
   ```

### For NeonDB:

1. **Install PostgreSQL Driver**
   ```bash
   pip install psycopg2-binary
   ```

2. **Get your NeonDB connection string** from the dashboard

3. **Update your .env file**:
   ```
   DATABASE_URL="postgresql://username:password@hostname.region.aws.neon.tech/database?sslmode=require"
   SECRET_KEY="your_generated_secret_key"
   JWT_SECRET_KEY="your_generated_jwt_secret_key"
   DEBUG=True
   PORT=8000
   ```

4. **Run database migrations**:
   ```bash
   alembic upgrade head
   ```

5. **Run the application**:
   ```bash
   cd backend
   python -m src.main
   ```

## Connecting to PostgreSQL in pgAdmin

### For Local PostgreSQL:
| Field | Value |
|-------|--------|
| Host | `localhost` or `127.0.0.1` |
| Database | `todos_db` |
| Username | `todos_user` or `postgres` |
| Password | Your PostgreSQL password |
| Port | `5432` |

### For NeonDB:
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
3. In the "General" tab, give the server a name (e.g., "Local PostgreSQL" or "NeonDB")
4. In the "Connection" tab:
   - Host: Enter your hostname (e.g., `localhost` for local, or NeonDB hostname)
   - Port: 5432
   - Maintenance database: your database name
   - Username: your database username
   - Password: Your database password
5. Click "Save"

## Common PostgreSQL Connection Strings

### Local PostgreSQL
```
postgresql://username:password@localhost:5432/database_name
postgresql://todos_user:password@127.0.0.1:5432/todos_db
```

### NeonDB
```
postgresql://neondb_owner:password@ep-cool-sky-123456.us-east-2.aws.neon.tech/neondb?sslmode=require
```

### With Additional Parameters
```
postgresql://username:password@hostname:port/database_name?sslmode=require&connect_timeout=10
postgresql://username:password@localhost:5432/database_name?application_name=TodoApp
```

## Troubleshooting

1. **Connection Issues**:
   - For local: Ensure PostgreSQL service is running
   - For NeonDB: Ensure SSL mode is set to `require`

2. **Authentication Errors**:
   - Verify your username, password, and database name
   - Check that the user has proper permissions

3. **Environment Variable Issues**:
   - Make sure to call `load_dotenv()` in your Python files
   - Verify your `.env` file is in the correct directory
   - Check that the file is named `.env` (no extension)

4. **Driver Issues**:
   - Make sure psycopg2-binary is installed
   - On Windows, you might need Microsoft C++ Build Tools

5. **Port Issues**:
   - Check if PostgreSQL is running on the default port (5432)
   - Verify firewall settings

## Testing Connection

Test the connection quickly:
```python
import os
from dotenv import load_dotenv
load_dotenv()
from src.database import engine
print('Database engine created successfully')
print('Engine URL:', str(engine.url))
```

## Quick Command for Both Setups

### Local PostgreSQL:
```bash
# Create database
psql -h localhost -p 5432 -U postgres -c "CREATE DATABASE todos_db; CREATE USER todos_user WITH PASSWORD 'password'; GRANT ALL PRIVILEGES ON DATABASE todos_db TO todos_user;"

# Set environment
echo DATABASE_URL=postgresql://todos_user:password@localhost:5432/todos_db > .env

# Install driver
pip install psycopg2-binary
```

### NeonDB:
```bash
# Set environment (replace with your actual connection string)
echo DATABASE_URL=postgresql://neondb_owner:password@ep-cool-sky-123456.us-east-2.aws.neon.tech/neondb?sslmode=require > .env

# Install driver
pip install psycopg2-binary
```

This skill provides a complete solution for quickly setting up PostgreSQL connections in your application, whether using local PostgreSQL or NeonDB cloud service.