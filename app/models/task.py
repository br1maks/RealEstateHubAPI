from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from typing import Optional
from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey, Text
from .user import User

class Task(Base):
    """Task model for admin moderation and user tasks."""
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="pending")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)

    user: Mapped["User"] = relationship(back_populates="tasks")