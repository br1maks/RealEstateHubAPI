import enum
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, ForeignKey, JSON, Text, DateTime
from datetime import datetime
from typing import Optional, List
from sqlalchemy.types import Enum as SQLEnum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .deal import Deal
    from .favorite import Favorite
    from .view import View
    from .amenity import Amenity
    from .category import Category
    from .photo import Photo


class PropertyTypeEnum(enum.Enum):
    apartment = "apartment"
    room = "room"
    warehouse = "warehouse"
    commercial = "commercial"

class Property(Base):
    """Property model for real estate listings."""
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    location: Mapped[str] = mapped_column(String(100), nullable=False)
    rooms: Mapped[Optional[int]] = mapped_column(Integer)
    area: Mapped[float] = mapped_column(Float, nullable=False)
    type: Mapped[PropertyTypeEnum] = mapped_column(SQLEnum(PropertyTypeEnum), nullable=False,
                                                   default=PropertyTypeEnum.apartment)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categorys.id"), nullable=False)
    is_premium: Mapped[bool] = mapped_column(default=False)
    photos: Mapped[Optional[List[str]]] = mapped_column(Text)
    views: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    rent_duration: Mapped[Optional[int]] = mapped_column(Integer)
    deposit: Mapped[Optional[float]] = mapped_column(Float)

    # One-to-many
    owner: Mapped["User"] = relationship(back_populates="propertys")
    deals: Mapped[List["Deal"]] = relationship(back_populates="property")
    photos_list: Mapped[List["Photo"]] = relationship(back_populates="property")
    favorites: Mapped[List["Favorite"]] = relationship(back_populates="property")
    views_list: Mapped[List["View"]] = relationship(back_populates="property")
    # Many-to-many
    amenitys: Mapped[List["Amenity"]] = relationship(secondary="property_amenity_assoc",
                                                      back_populates="propertys")
    # One-to-many
    category: Mapped["Category"] = relationship(back_populates="propertys")