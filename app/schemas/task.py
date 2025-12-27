from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, List


class TaskCreate(BaseModel):
    title: str
    description: str
    assigned_to: str
    due_date: Optional[datetime] = None


class TaskUpdate(BaseModel):
    status: Optional[str] = None
    priority: Optional[str] = None
    assigned_to: Optional[str] = None


class TaskResponse(BaseModel):
    id: str
    title: str
    description: str
    category: str
    priority: str
    status: str
    assigned_to: str
    due_date: Optional[datetime]
    extracted_entities: Dict
    suggested_actions: List[str]
    created_at: datetime

    class Config:
        from_attributes = True
