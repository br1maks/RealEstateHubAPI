from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, ForeignKey, DateTime
from datetime import datetime
from typing import Optional

class Message(Base):
    """Message model for user chats."""
    sender_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    recipient_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    deal_id: Mapped[Optional[int]] = mapped_column(ForeignKey("deals.id"))
    message: Mapped[str] = mapped_column(Text, nullable=False)
    read: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)