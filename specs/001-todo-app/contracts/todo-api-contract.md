# Todo API Contract

## Base URL
`http://localhost:8000/api/v1` (development)
`https://yourdomain.com/api/v1` (production)

## Authentication
None required for Phase II (as specified in requirements)

## Common Headers
- `Content-Type: application/json`
- `Accept: application/json`

## Error Format
All errors follow this structure:
```json
{
  "detail": "Error message",
  "status_code": 400
}
```

## Endpoints

### Create Todo
`POST /todos`

**Request Body:**
```json
{
  "title": "string (required)",
  "description": "string (optional)",
  "priority": "enum: low|medium|high (optional, default: medium)",
  "category": "string (optional)",
  "due_date": "ISO 8601 datetime string (optional)"
}
```

**Response (201 Created):**
```json
{
  "id": "UUID string",
  "title": "string",
  "description": "string",
  "completed": "boolean (default: false)",
  "priority": "enum: low|medium|high",
  "category": "string",
  "due_date": "ISO 8601 datetime string or null",
  "created_at": "ISO 8601 datetime string",
  "updated_at": "ISO 8601 datetime string"
}
```

**Validation Errors (400):**
- Missing required fields
- Invalid priority value
- Invalid date format

### Get All Todos
`GET /todos`

**Query Parameters:**
- `completed`: boolean (filter by completion status)
- `priority`: enum (filter by priority level)
- `category`: string (filter by category)
- `sort_by`: string (sort by field: priority, due_date, created_at)
- `order`: asc|desc (sort order, default: asc)

**Response (200):**
```json
[
  {
    "id": "UUID string",
    "title": "string",
    "description": "string",
    "completed": "boolean",
    "priority": "enum: low|medium|high",
    "category": "string",
    "due_date": "ISO 8601 datetime string or null",
    "created_at": "ISO 8601 datetime string",
    "updated_at": "ISO 8601 datetime string"
  }
]
```

### Get Todo by ID
`GET /todos/{id}`

**Path Parameter:**
- `id`: UUID string

**Response (200):**
```json
{
  "id": "UUID string",
  "title": "string",
  "description": "string",
  "completed": "boolean",
  "priority": "enum: low|medium|high",
  "category": "string",
  "due_date": "ISO 8601 datetime string or null",
  "created_at": "ISO 8601 datetime string",
  "updated_at": "ISO 8601 datetime string"
}
```

**Not Found (404):**
- Todo with given ID does not exist

### Update Todo
`PUT /todos/{id}`

**Path Parameter:**
- `id`: UUID string

**Request Body:**
```json
{
  "title": "string (required)",
  "description": "string (optional)",
  "completed": "boolean (optional)",
  "priority": "enum: low|medium|high (optional)",
  "category": "string (optional)",
  "due_date": "ISO 8601 datetime string (optional)"
}
```

**Response (200):**
```json
{
  "id": "UUID string",
  "title": "string",
  "description": "string",
  "completed": "boolean",
  "priority": "enum: low|medium|high",
  "category": "string",
  "due_date": "ISO 8601 datetime string or null",
  "created_at": "ISO 8601 datetime string",
  "updated_at": "ISO 8601 datetime string"
}
```

### Delete Todo
`DELETE /todos/{id}`

**Path Parameter:**
- `id`: UUID string

**Response (204 No Content)**

**Not Found (404):**
- Todo with given ID does not exist

### Toggle Todo Completion
`PATCH /todos/{id}/toggle`

**Path Parameter:**
- `id`: UUID string

**Response (200):**
```json
{
  "id": "UUID string",
  "title": "string",
  "description": "string",
  "completed": "boolean (opposite of previous value)",
  "priority": "enum: low|medium|high",
  "category": "string",
  "due_date": "ISO 8601 datetime string or null",
  "created_at": "ISO 8601 datetime string",
  "updated_at": "ISO 8601 datetime string"
}
```

**Not Found (404):**
- Todo with given ID does not exist