from .property import Property
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey, Float, DateTime
from typing import  Optional, List


class Amenity(Base):
    """Amenity model for property features (e.g., furniture, parking)."""
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    propertys: Mapped[List["Property"]] = relationship(
        secondary="property_amenity_assoc", back_populates="amenitys"
    )