from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, ForeignKey, DateTime
from datetime import datetime
from typing import Optional
from .user import User
from .deal import Deal

class Message(Base):
    """Message model for user chats."""
    sender_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    recipient_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    deal_id: Mapped[Optional[int]] = mapped_column(ForeignKey("deals.id"))
    message: Mapped[str] = mapped_column(Text, nullable=False)
    read: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)

    sender: Mapped["User"] = relationship(foreign_keys="Message.sender_id", back_populates="messages_sent")
    recipient: Mapped["User"] = relationship(foreign_keys="Message.recipient_id", back_populates="messages_received")
    deal: Mapped["Deal"] = relationship(back_populates="messages")