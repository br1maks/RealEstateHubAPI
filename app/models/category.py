
from .base import Base
from .property import Property
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text
from typing import  Optional, List

class Category(Base):
    """Category model for property types."""
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    propertys: Mapped[List["Property"]] = relationship(back_populates="category")