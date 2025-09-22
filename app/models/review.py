from typing import Optional
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, DateTime, Text, Integer, CheckConstraint
from datetime import datetime

class Review(Base):
    deal_id: Mapped[int] = mapped_column(ForeignKey("deals.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    rating: Mapped[int] = mapped_column(Integer, CheckConstraint("rating >= 1 AND rating <= 5"), nullable=False)
    comment: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)