# Todo Application

A full-stack todo application built with Python FastAPI (backend) and Next.js (frontend), deployed on Hugging Face Spaces and Vercel respectively.

## 🚀 Live Demo

- **Frontend (Vercel)**: [https://phase-two-hackthn-two.vercel.app](https://phase-two-hackthn-two.vercel.app)
- **Backend API (Hugging Face Spaces)**: [https://nkamdar-todo-task-tracker.hf.space](https://nkamdar-todo-task-tracker.hf.space)
  - API Base URL: `https://nkamdar-todo-task-tracker.hf.space/api/v1`

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI (Python)
- **Database**: PostgreSQL
- **ORM**: SQLModel
- **Authentication**: JWT-based authentication
- **Deployment**: Hugging Face Spaces

### Frontend
- **Framework**: Next.js (React)
- **Styling**: Tailwind CSS
- **HTTP Client**: Axios
- **Deployment**: Vercel

## 📋 Features

- User authentication (signup/login)
- Create, read, update, and delete todos
- Secure API endpoints
- Responsive UI
- Real-time todo management

## 🏗️ Project Structure

```
├── backend/              # FastAPI backend
│   ├── src/
│   │   ├── api/          # API routes
│   │   ├── models/       # Database models
│   │   ├── services/     # Business logic
│   │   └── database.py   # Database configuration
│   ├── requirements.txt  # Python dependencies
│   └── main.py           # Application entry point
├── frontend/             # Next.js frontend
│   ├── src/
│   │   ├── app/          # App Router pages
│   │   ├── components/   # Reusable components
│   │   └── services/     # API service functions
│   ├── package.json      # Node.js dependencies
│   └── next.config.js    # Next.js configuration
└── todo_task_tracker/    # Prepared files for Hugging Face deployment
```

## 🔧 API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register a new user
- `POST /api/v1/auth/login` - Login user
- `POST /api/v1/auth/logout` - Logout user

### Todos
- `GET /api/v1/todos` - Get all todos
- `POST /api/v1/todos` - Create a new todo
- `GET /api/v1/todos/{id}` - Get a specific todo
- `PUT /api/v1/todos/{id}` - Update a specific todo
- `DELETE /api/v1/todos/{id}` - Delete a specific todo

## 🚀 Development Setup

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in `.env`:
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/todo_db
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ```

4. Run the backend server:
   ```bash
   uvicorn src.main:app --reload --port 8000
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up environment variables in `.env.local`:
   ```env
   NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api/v1
   ```

4. Run the development server:
   ```bash
   npm run dev
   ```

## 🌐 Environment Variables

### Backend (.env)
- `DATABASE_URL`: PostgreSQL database connection string
- `SECRET_KEY`: Secret key for JWT token signing
- `DEBUG`: Debug mode (True/False)
- `ALLOWED_ORIGINS`: Comma-separated list of allowed origins for CORS

### Frontend (.env.local)
- `NEXT_PUBLIC_API_BASE_URL`: Backend API base URL

## 🚢 Deployment

### Backend Deployment (Hugging Face Spaces)
1. Prepare the deployment files using `prepare_hf_space.py`
2. Copy the files from `todo_task_tracker/` to your Hugging Face Space repository
3. Push the changes to deploy

### Frontend Deployment (Vercel)
1. Push the frontend code to a GitHub repository
2. Connect the repository to Vercel
3. Configure environment variables in Vercel dashboard

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Issues & Support

If you encounter any issues or have questions, please open an issue in the repository.

---

Made with ❤️ using FastAPI, Next.js, and PostgreSQL