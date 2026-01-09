# Quickstart Guide for Todo Application

## Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL (or access to Neon PostgreSQL database)
- Docker (optional, for containerized setup)

## Setup Instructions

### 1. Clone and Navigate to Project
```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Backend Setup
```bash
cd backend
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
# Edit .env with your database connection details
```

### 4. Database Setup
```bash
# Run database migrations
alembic upgrade head
```

### 5. Frontend Setup
```bash
cd frontend
npm install
```

### 6. Running the Application

#### Option A: Separate Services
```bash
# Terminal 1: Start backend
cd backend
uvicorn src.main:app --reload

# Terminal 2: Start frontend
cd frontend
npm run dev
```

#### Option B: Using Docker
```bash
docker-compose up --build
```

## API Endpoints

### Todo Operations
- `GET /todos` - Retrieve all todos
- `POST /todos` - Create a new todo
- `GET /todos/{id}` - Retrieve a specific todo
- `PUT /todos/{id}` - Update a specific todo
- `DELETE /todos/{id}` - Delete a specific todo
- `PATCH /todos/{id}/toggle` - Toggle completion status

### Query Parameters
- `?completed=true/false` - Filter by completion status
- `?priority=low/medium/high` - Filter by priority
- `?category={category}` - Filter by category
- `?sort_by=priority/due_date/created_at` - Sort results

## Frontend Pages

- `/` - Main dashboard showing all todos with filtering and sorting options
- `/add` - Page for adding new todos (may be modal on main page)

## Development Commands

### Backend
```bash
# Run tests
pytest

# Run with auto-reload
uvicorn src.main:app --reload

# Generate database migration
alembic revision --autogenerate -m "migration message"
```

### Frontend
```bash
# Run development server
npm run dev

# Run tests
npm run test

# Build for production
npm run build
```

## Troubleshooting

1. **Database Connection Issues**: Verify your PostgreSQL connection string in `.env`
2. **Frontend Cannot Connect to Backend**: Ensure backend is running and check CORS settings
3. **Migration Errors**: Run `alembic stamp head` if migrations are out of sync