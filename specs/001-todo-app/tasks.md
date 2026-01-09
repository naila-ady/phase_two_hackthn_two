# Implementation Tasks: Todo Application

**Branch**: `001-todo-app` | **Date**: 2026-01-06 | **Plan**: [plan.md](./plan.md)
**Input**: Feature specification from `/specs/001-todo-app/spec.md` and implementation plan

## Phase II Tasks – Evolution of Todo (No Duration)

### Phase 1 – Backend Foundation (CRUD)

#### Task 1.1: Generate FastAPI Scaffold
- **Depends on**: Nothing
- **What to do**: Generate the FastAPI project structure with clear separation for app entry, routes, and models
- **Acceptance Criterion**: FastAPI app runs successfully and project structure is present
- **Output**: Backend project folder structure
- **Status**: [X] completed

#### Task 1.2: Create SQLModel Todo Entity
- **Depends on**: Task 1.1
- **What to do**: Define the Todo SQLModel with all required fields and correct data types
- **Acceptance Criterion**: Todo model exists with id, title, description, completed, priority, category, due_date, created_at, updated_at
- **Output**: Todo model file
- **Status**: [X] completed

#### Task 1.3: Implement Create Todo API
- **Depends on**: Task 1.2
- **What to do**: Implement endpoint to create a new Todo
- **Acceptance Criterion**: POST /todos creates a Todo and returns it with a generated ID
- **Output**: Create Todo API route
- **Status**: [X] completed

#### Task 1.4: Implement Read Todos API
- **Depends on**: Task 1.2
- **What to do**: Implement endpoint to fetch all Todos with optional filters
- **Acceptance Criterion**: GET /todos returns Todos and supports filtering/sorting parameters
- **Output**: Read Todos API route
- **Status**: [X] completed

#### Task 1.5: Implement Update Todo API
- **Depends on**: Task 1.2
- **What to do**: Implement endpoint to update an existing Todo
- **Acceptance Criterion**: PUT /todos/{id} updates provided fields only
- **Output**: Update Todo API route
- **Status**: [X] completed

#### Task 1.6: Implement Delete Todo API
- **Depends on**: Task 1.2
- **What to do**: Implement endpoint to delete a Todo
- **Acceptance Criterion**: DELETE /todos/{id} removes the Todo permanently
- **Output**: Delete Todo API route
- **Status**: [X] completed

#### Task 1.7: Implement Toggle Completion API
- **Depends on**: Task 1.2
- **What to do**: Implement endpoint to toggle completion status
- **Acceptance Criterion**: PATCH /todos/{id}/complete flips completed state correctly
- **Output**: Toggle completion API route
- **Status**: [X] completed

### ✅ CHECKPOINT 1 – Backend Foundation
- **Status**: [X] completed
- **Verification**: All CRUD endpoints exist and function correctly
- **Verification**: API can be tested end-to-end
- **Action**: Human review → Approve → Commit → Proceed

### Phase 2 – Database Integration

#### Task 2.1: Connect Backend to Neon PostgreSQL
- **Depends on**: Phase 1 complete
- **What to do**: Configure database connection using environment variables
- **Acceptance Criterion**: Backend connects successfully to Neon database
- **Output**: Database connection configuration
- **Status**: [X] completed

#### Task 2.2: Auto-Generate Database Tables
- **Depends on**: Task 2.1
- **What to do**: Generate database tables from SQLModel definitions
- **Acceptance Criterion**: Todo table exists in database
- **Output**: Verified database schema
- **Status**: [X] completed

#### Task 2.3: Configure Alembic Migrations
- **Depends on**: Task 2.2
- **What to do**: Set up Alembic for schema migrations
- **Acceptance Criterion**: Migration can be generated and applied successfully
- **Output**: Alembic migration files
- **Status**: [X] completed

#### Task 2.4: Validate Data Persistence
- **Depends on**: Task 2.3
- **What to do**: Restart backend and verify Todos persist
- **Acceptance Criterion**: Data remains intact after restart
- **Output**: Persistence verification result
- **Status**: [X] completed

### ✅ CHECKPOINT 2 – Database Integration
- **Status**: [X] completed
- **Verification**: Data persists correctly
- **Verification**: Migrations work
- **Action**: Human review → Approve → Commit → Proceed

### Phase 3 – Frontend Foundation

#### Task 3.1: Generate Next.js Scaffold
- **Depends on**: Phase 2 complete
- **What to do**: Generate Next.js project structure
- **Acceptance Criterion**: Next.js app runs locally
- **Output**: Frontend project scaffold
- **Status**: [X] completed

#### Task 3.2: Create Todo List Page
- **Depends on**: Task 3.1
- **What to do**: Display list of Todos fetched from backend
- **Acceptance Criterion**: Todos render correctly in UI
- **Output**: Todo list page
- **Status**: [X] completed

#### Task 3.3: Implement Add Todo Form
- **Depends on**: Task 3.2
- **What to do**: Add form to create new Todos
- **Acceptance Criterion**: New Todo appears after submission
- **Output**: Add Todo UI component
- **Status**: [X] completed

#### Task 3.4: Sync UI With Backend
- **Depends on**: Task 3.3
- **What to do**: Ensure UI refreshes after CRUD actions
- **Acceptance Criterion**: UI always reflects backend state
- **Output**: Integrated data-fetching logic
- **Status**: [X] completed

### ✅ CHECKPOINT 3 – Frontend Foundation
- **Status**: [X] completed
- **Verification**: UI fully connected to backend
- **Verification**: CRUD works via UI
- **Action**: Human review → Approve → Commit → Proceed

### Phase 4 – Feature Completion

#### Task 4.1: Edit Todo in UI
- **Depends on**: Phase 3 complete
- **What to do**: Allow editing Todo fields
- **Acceptance Criterion**: Edited Todo persists and updates UI
- **Output**: Edit Todo feature
- **Status**: [X] completed

#### Task 4.2: Delete Todo in UI
- **Depends on**: Task 4.1
- **What to do**: Allow deleting Todos
- **Acceptance Criterion**: Deleted Todo disappears from UI and DB
- **Output**: Delete feature
- **Status**: [X] completed

#### Task 4.3: Toggle Completion in UI
- **Depends on**: Task 4.1
- **What to do**: Toggle completed state from UI
- **Acceptance Criterion**: Completion state updates correctly
- **Output**: Completion toggle UI
- **Status**: [X] completed

#### Task 4.4: Filter Todos
- **Depends on**: Task 4.3
- **What to do**: Filter Todos by status, priority, category
- **Acceptance Criterion**: Filtered results match backend data
- **Output**: Filter UI and logic
- **Status**: [X] completed

#### Task 4.5: Sort Todos
- **Depends on**: Task 4.4
- **What to do**: Sort Todos by due date, priority, or title
- **Acceptance Criterion**: Sorting works correctly
- **Output**: Sort functionality
- **Status**: [X] completed

### ✅ CHECKPOINT 4 – Feature Completion
- **Status**: [X] completed
- **Verification**: All Phase II features work correctly
- **Action**: Human review → Approve → Commit → Proceed