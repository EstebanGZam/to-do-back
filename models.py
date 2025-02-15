from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime

class Task(BaseModel):
    id: Optional[int] = None
    title: str
    type: Literal["personal", "professional"]
    completed: bool = False
    created_at: datetime = datetime.now()

class TaskCreate(BaseModel):
    title: str
    type: Literal["personal", "professional"]
    completed: bool = False

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    type: Optional[Literal["personal", "professional"]] = None
    completed: Optional[bool] = None