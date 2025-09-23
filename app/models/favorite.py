from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime
from datetime import datetime
from .user import User
from .property import Property

class Favorite(Base):
    """Favorite model for user saved properties."""
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    property_id: Mapped[int] = mapped_column(ForeignKey("propertys.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)

    user: Mapped["User"] = relationship(back_populates="favorites")
    property: Mapped["Property"] = relationship(back_populates="favorites")