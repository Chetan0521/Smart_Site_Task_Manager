from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.task import Task
from app.models.task_history import TaskHistory
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.services.classification import classify_task

router = APIRouter()


# =========================
# CREATE TASK (POST)
# =========================
@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    classification = classify_task(task.title, task.description)

    new_task = Task(
        title=task.title,
        description=task.description,
        assigned_to=task.assigned_to,
        due_date=task.due_date,
        category=classification["category"],
        priority=classification["priority"],
        extracted_entities=classification["extracted_entities"],
        suggested_actions=classification["suggested_actions"],
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


# =========================
# GET TASKS (READ)
# =========================
@router.get("/", response_model=List[TaskResponse])
def get_tasks(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50),
    status: Optional[str] = None,
    priority: Optional[str] = None,
    category: Optional[str] = None,
    sort: str = "created_at",
    db: Session = Depends(get_db),
):
    query = db.query(Task)

    if status:
        query = query.filter(Task.status == status)

    if priority:
        query = query.filter(Task.priority == priority)

    if category:
        query = query.filter(Task.category == category)

    if sort == "created_at":
        query = query.order_by(Task.created_at.desc())

    offset = (page - 1) * limit
    tasks = query.offset(offset).limit(limit).all()

    return tasks


# =========================
# UPDATE TASK + HISTORY (PATCH)
# =========================
@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: str,
    updates: TaskUpdate,
    db: Session = Depends(get_db),
):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    update_data = updates.dict(exclude_unset=True)

    for field, new_value in update_data.items():
        old_value = getattr(task, field)

        if old_value != new_value:
            history = TaskHistory(
                task_id=task.id,
                field_name=field,
                old_value=str(old_value),
                new_value=str(new_value),
            )
            db.add(history)
            setattr(task, field, new_value)

    db.commit()
    db.refresh(task)

    return task
