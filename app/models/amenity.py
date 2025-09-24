
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey, Float, DateTime
from typing import  Optional, List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .property_amenity_assoc import PropertyAmenity
    from .property import Property

class Amenity(Base):
    """Amenity model for property features (e.g., furniture, parking)."""
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    amenity_assocs: Mapped[List["PropertyAmenity"]] = relationship(back_populates="amenity")