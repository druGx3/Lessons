from pydantic import BaseModel
from uuid import UUID
from datetime import date

class TaskResponse(BaseModel):
    id: UUID
    name: str
    plan: int
    complete: int
    date: date
    progress: int
    status: str

class TaskCreate(BaseModel):
    name: str
    plan: int
    complete: int
    date: date

class TaskUpdate(BaseModel):
    complete: int
