from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from typing import Optional
from datetime import datetime
from sqlalchemy import String, DateTime, Float
from sqlalchemy.types import Enum as SQLEnum
import enum

class RoleEnum(enum.Enum):
    buyer = "buyer"
    seller = "seller"
    admin = "admin"

class User(Base):
    """User model for authentication, roles, and property management."""

    username: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False,)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(SQLEnum(RoleEnum), nullable=False, default=RoleEnum.buyer, index=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    phone: Mapped[Optional[str]] = mapped_column(String(20))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_verified: Mapped[bool] = mapped_column(default=False)
    rating: Mapped[Optional[float]] = mapped_column(Float, default=0.0)
