# PostgreSQL Database Connection Skill

## Purpose
This skill automates the setup and connection to a PostgreSQL database for the Todo application.

## Pre-requisites
- PostgreSQL 16 must be installed and running
- PostgreSQL must be accessible on port 5432
- User must have administrative access to PostgreSQL

## Steps

### 1. Create PostgreSQL Database
Connect to PostgreSQL and create the required database:
```bash
"C:\Program Files\PostgreSQL\16\bin\psql.exe" -h localhost -p 5432 -U postgres -d postgres
```

In the PostgreSQL prompt, run:
```sql
CREATE DATABASE todos_db;
GRANT ALL PRIVILEGES ON DATABASE todos_db TO postgres;
\q
```

### 2. Configure Environment Variables
Create a .env file in the backend directory with database credentials:
```bash
cd C:\hck_ll_phase_II\phase_two_hackthn_two\backend
echo DATABASE_URL=postgresql://postgres:naila1adnan2@localhost:5432/todos_db > .env
```

### 3. Update Database Configuration
Ensure the application is configured to use PostgreSQL:
- In `backend/src/database.py`, verify the DATABASE_URL uses environment variable
- The default should fall back to PostgreSQL when environment variable is set

### 4. Run Database Migrations
Apply the database schema to create tables:
```bash
cd C:\hck_ll_phase_II\phase_two_hackthn_two\backend
alembic upgrade head
```

### 5. Verify Database Setup
Check that the database and tables were created properly:
```bash
"C:\Program Files\PostgreSQL\16\bin\psql.exe" -h localhost -p 5432 -U postgres -d todos_db -c "\dt"
```

### 6. Test Connection
Start the backend to verify connection works:
```bash
cd C:\hck_ll_phase_II\phase_two_hackthn_two\backend
python -m src.main
```

## Expected Outcome
- PostgreSQL database `todos_db` exists
- Tables are created according to the application schema
- Application can connect to PostgreSQL database
- Environment variables are properly configured
- Database migrations are applied successfully

## Troubleshooting
- If database creation fails, verify PostgreSQL service is running
- If migrations fail, ensure Alembic is properly configured
- If connection fails, verify the password in .env file matches PostgreSQL user password
- If port 5432 is unavailable, check if PostgreSQL is running on a different port

## One sentence to remember forever

- PostgreSQL stores data. psql types. pgAdmin clicks.