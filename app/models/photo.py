from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .property import Property

class Photo(Base):
    """Photos model for property images/videos."""
    property_id: Mapped[int] = mapped_column(ForeignKey("propertys.id"), nullable=False)
    url: Mapped[str] = mapped_column(String(255), nullable=False)
    is_primary: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)

    property: Mapped["Property"] = relationship(back_populates="photos_list")