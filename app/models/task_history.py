import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text

from app.database import Base


class TaskHistory(Base):
    __tablename__ = "task_history"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    task_id = Column(String, nullable=False)

    field_name = Column(String, nullable=False)
    old_value = Column(Text)
    new_value = Column(Text)

    changed_at = Column(DateTime, default=datetime.utcnow)
