
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from typing import Optional
from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey, Text

class View(Base):
    """"View model for property view statistics."""
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))
    property_id: Mapped[int] = mapped_column(ForeignKey("properties.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)
