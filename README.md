# Todo App Backend

A FastAPI-based backend for the Todo application that provides REST API endpoints for task management.

## Features

- CRUD operations for tasks
- Clear completed tasks functionality
- Task categorization (personal/professional)
- In-memory database (for demonstration purposes)

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/EstebanGZam/to-do-back.git
cd to-do-back
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install fastapi uvicorn pydantic
```

4. Run the server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `POST /tasks` - Create a new task
- `GET /tasks` - List all tasks
- `GET /tasks/{task_id}` - Get a specific task
- `PUT /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task
- `DELETE /tasks/clear-completed` - Clear all completed tasks

## API Documentation

Once the server is running, you can access:

- Swagger UI documentation at `http://localhost:8000/docs`
- ReDoc documentation at `http://localhost:8000/redoc`

## Frontend Repository

The frontend for this Todo application can be found in the following repository:

[Frontend Repository](https://github.com/EstebanGZam/to-do-front)
