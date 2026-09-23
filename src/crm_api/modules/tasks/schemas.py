from pydantic import BaseModel, Field
from datetime import datetime

class TaskCreate(BaseModel):
    title : str = Field(min_length=1, max_length=255)
    
class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=255)
    done: bool | None = None

class TaskOut(BaseModel):
    id: int
    title: str
    done: bool
    created_at: datetime