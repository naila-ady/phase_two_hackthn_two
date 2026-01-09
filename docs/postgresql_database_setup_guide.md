# PostgreSQL Database Setup Guide for Todo Application

## Overview
This guide contains all commands needed to create, run, check, and extend the PostgreSQL database for the Todo application.

## Prerequisites
- PostgreSQL 16 installed
- Access to PostgreSQL command line tools (psql)

## Database Creation Commands

### 1. Connect to PostgreSQL
```bash
"C:\Program Files\PostgreSQL\16\bin\psql.exe" -h localhost -p 5432 -U postgres -d postgres
```

### 2. Create the Database
In the PostgreSQL prompt, run:
```sql
CREATE DATABASE todos_db;
GRANT ALL PRIVILEGES ON DATABASE todos_db TO postgres;
\q
```

## Application Setup Commands

### 3. Create Environment File
```bash
# Navigate to backend directory
cd C:\hck_ll_phase_II\phase_two_hackthn_two\backend

# Create .env file with database credentials
echo DATABASE_URL=postgresql://postgres:naila1adnan2@localhost:5432/todos_db > .env
```

### 4. Run Database Migrations
```bash
cd C:\hck_ll_phase_II\phase_two_hackthn_two\backend
alembic upgrade head
```

## Database Check Commands

### 5. Verify Database and Tables Exist
```bash
# Check if database exists
"C:\Program Files\PostgreSQL\16\bin\psql.exe" -h localhost -p 5432 -U postgres -c "\l | grep todos_db"

# Connect to the todos_db and list tables
"C:\Program Files\PostgreSQL\16\bin\psql.exe" -h localhost -p 5432 -U postgres -d todos_db -c "\dt"

# Check if todos table has data
"C:\Program Files\PostgreSQL\16\bin\psql.exe" -h localhost -p 5432 -U postgres -d todos_db -c "SELECT * FROM todos;"
```

### 6. Manual Database Inspection
Connect to PostgreSQL and run these commands:
```sql
-- Connect to the todos_db database
\c todos_db;

-- List all tables
\dt;

-- View all todos
SELECT * FROM todos;

-- View table structure
\d todos;

-- Count total todos
SELECT COUNT(*) FROM todos;

-- Exit
\q
```

## Running the Application

### 7. Start the Backend Server
```bash
cd C:\hck_ll_phase_II\phase_two_hackthn_two\backend
python -m src.main
```

### 8. Start the Frontend Server
```bash
cd C:\hck_ll_phase_II\phase_two_hackthn_two\frontend
npm run dev
```

## Extension Commands

### 9. Adding Additional Features to Database
```sql
-- Connect to database
"C:\Program Files\PostgreSQL\16\bin\psql.exe" -h localhost -p 5432 -U postgres -d todos_db

-- Example: Add a new column to todos table
ALTER TABLE todos ADD COLUMN tags TEXT[];

-- Example: Create an index for better performance
CREATE INDEX idx_todos_priority ON todos(priority);

-- Example: Add a new table for categories
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    color VARCHAR(7) DEFAULT '#000000',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Exit
\q
```

### 10. Database Backup and Restore
```bash
# Backup the database
"C:\Program Files\PostgreSQL\16\bin\pg_dump.exe" -h localhost -U postgres -d todos_db > backup_todos_$(date +%Y%m%d_%H%M%S).sql

# Restore the database
"C:\Program Files\PostgreSQL\16\bin\psql.exe" -h localhost -U postgres -d todos_db < backup_file.sql
```

## Troubleshooting Commands

### 11. Common Issues Resolution
```bash
# Check if PostgreSQL service is running
sc query postgresql-x64-16

# Check which port PostgreSQL is running on
"C:\Program Files\PostgreSQL\16\bin\psql.exe" -h localhost -p 5432 -U postgres -c "SHOW port;"

# Reset user password if needed
"C:\Program Files\PostgreSQL\16\bin\psql.exe" -h localhost -p 5432 -U postgres -d postgres -c "ALTER USER postgres PASSWORD 'newpassword';"

# Check database connections
"C:\Program Files\PostgreSQL\16\bin\psql.exe" -h localhost -p 5432 -U postgres -d postgres -c "SELECT pid, usename, application_name, state FROM pg_stat_activity;"
```

## Quick Reference Commands

### 12. Essential Commands Summary
| Action | Command |
|--------|---------|
| Connect to DB | `"C:\Program Files\PostgreSQL\16\bin\psql.exe" -h localhost -p 5432 -U postgres -d todos_db` |
| List tables | `\dt` |
| View data | `SELECT * FROM todos;` |
| Table structure | `\d todos` |
| Exit psql | `\q` |
| Run migrations | `alembic upgrade head` |
| Check if DB exists | `\l` |

## Security Notes
- Store database credentials in .env file, not in code
- Change default passwords in production
- Limit database user permissions appropriately
- Use connection pooling in production environments