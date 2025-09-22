import enum
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey, Float, DateTime
from datetime import datetime
from sqlalchemy.types import Enum as SQLEnum
from typing import Optional

class DealStatusEnum(enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    closed = "closed"
    rejected = "rejected"

class Deal(Base):
    """Deal model for rent and sale transactions with flexible terms."""
    property_id: Mapped[int] = mapped_column(ForeignKey("propertys.id"), nullable=False)
    buyer_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    status: Mapped[DealStatusEnum] = mapped_column(SQLEnum(DealStatusEnum), nullable=False, default=DealStatusEnum.pending)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    rent_duration: Mapped[Optional[int]] = mapped_column(Integer)
    deposit: Mapped[Optional[int]] = mapped_column(Float)