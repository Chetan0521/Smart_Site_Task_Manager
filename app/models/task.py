import uuid
from sqlalchemy import Column, String, Text, DateTime, JSON
from sqlalchemy.sql import func

from app.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    title = Column(String, nullable=False)
    description = Column(Text)

    category = Column(String)
    priority = Column(String)
    status = Column(String, default="pending")

    assigned_to = Column(String)
    due_date = Column(DateTime, nullable=True)

    extracted_entities = Column(JSON)
    suggested_actions = Column(JSON)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
