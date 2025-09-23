
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from typing import Optional
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .property import Property

class View(Base):
    """"View model for property view statistics."""
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))
    property_id: Mapped[int] = mapped_column(ForeignKey("propertys.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)

    user: Mapped["User"] = relationship(back_populates="views")
    property: Mapped["Property"] = relationship(back_populates="views_list")
