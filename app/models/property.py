import enum
from .base import Base
from .photos import Photos
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, ForeignKey, JSON, Text, DateTime
from datetime import datetime
from typing import Optional, List
from sqlalchemy.types import Enum as SQLEnum

class PropertyTypenEnum(enum.Enum):
    apartment = "apartment"
    room = "room"
    warehouse = "warehouse"
    commercial = "commercial"

class Property(Base):
    """Property model for real estate listings."""
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[Optional[Text]] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    location: Mapped[str] = mapped_column(String(100), nullable=False)
    rooms: Mapped[Optional[int]] = mapped_column(Integer, nullable=False)
    area: Mapped[float] = mapped_column(Float, nullable=False)
    type: Mapped[PropertyTypenEnum] = mapped_column(SQLEnum(PropertyTypenEnum), nullable=False, default=PropertyTypenEnum.apartment)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    rent_duration: Mapped[Optional[int]] = mapped_column(Integer)
    deposit: Mapped[Optional[float]] = mapped_column(Float)
    is_premium: Mapped[bool] = mapped_column(default=False)
    views: Mapped[int] = mapped_column(Integer, default=0)
    photos: Mapped[list["Photos"]] = relationship(back_populates="property")
    # amenities: Mapped[list["Amenity"]] = relationship(back_populates="property")
    # category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)
