from fastapi import FastAPI
from app.routers import tasks
from app.database import Base, engine
from app.models.task import Task
from app.models.task_history import TaskHistory

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Site Task Manager API",
    description="Task management with auto-classification",
    version="1.0.0"
)

app.include_router(tasks.router, prefix="/api/tasks", tags=["Tasks"])

@app.get("/")
def root():
    return {"message": "Smart Site Task Manager API is running"}
