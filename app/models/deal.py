import enum
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, Float, DateTime
from datetime import datetime
from sqlalchemy.types import Enum as SQLEnum
from typing import Optional, List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .property import Property
    from .review import Review
    from .message import Message

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

    property: Mapped["Property"] = relationship(back_populates="deals")
    buyer: Mapped["User"] = relationship(back_populates="deals")
    reviews: Mapped[List["Review"]] = relationship(back_populates="deal")
    messages: Mapped[List["Message"]] = relationship(back_populates="deal")