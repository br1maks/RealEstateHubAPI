from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime, Text
from datetime import datetime
from sqlalchemy.types import Enum as SQLEnum
from .user import User
import enum

class NotificationTypeEnum(enum.Enum):
    """Enum for notification types."""
    new_deal = "new_deal"
    status_update = "status_update"
    review = "review"

class Notification(Base):
    """Notification model for real-time alerts."""
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    type: Mapped[NotificationTypeEnum] = mapped_column(SQLEnum(NotificationTypeEnum), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    read: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)

    user: Mapped["User"] = relationship(back_populates="notifications")