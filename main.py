from fastapi import FastAPI, HTTPException
from typing import List
from models import Task, TaskCreate, TaskUpdate
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# Configurar CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # URL de tu aplicación React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Base de datos en memoria
tasks_db = []

@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    task_dict = task.dict()
    task_dict["id"] = len(tasks_db) + 1
    task_dict["created_at"] = datetime.now()
    tasks_db.append(task_dict)
    return task_dict

@app.get("/tasks", response_model=List[Task])
def list_tasks():
    return tasks_db

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = next((task for task in tasks_db if task["id"] == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: TaskUpdate):
    task_index = next((index for index, task in enumerate(tasks_db) if task["id"] == task_id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task = tasks_db[task_index]
    update_data = updated_task.dict(exclude_unset=True)
    tasks_db[task_index] = {**task, **update_data}
    return tasks_db[task_index]

@app.delete("/tasks/clear-completed")
def clear_completed_tasks():
    global tasks_db
    completed_tasks = [task for task in tasks_db if task["completed"]]
    tasks_db = [task for task in tasks_db if not task["completed"]]
    return completed_tasks

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    task_index = next((index for index, task in enumerate(tasks_db) if task["id"] == task_id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    deleted_task = tasks_db.pop(task_index)
    return deleted_task
