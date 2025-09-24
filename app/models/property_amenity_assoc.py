
from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base
from datetime import datetime

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .property import Property
    from .amenity import Amenity


class PropertyAmenity(Base):
    """Association class for Property-Amenity many-to-many relationship with additional fields."""
    property_id: Mapped[int] = mapped_column(Integer, ForeignKey("propertys.id"), primary_key=True)
    amenity_id: Mapped[int] = mapped_column(Integer, ForeignKey("amenitys.id"), primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)

    # property: Mapped["Property"] = relationship(back_populates="amenitys")
    # amenity: Mapped["Amenity"] = relationship(back_populates="propertys")
    property: Mapped["Property"] = relationship(back_populates="amenity_assocs")
    amenity: Mapped["Amenity"] = relationship(back_populates="amenity_assocs")
