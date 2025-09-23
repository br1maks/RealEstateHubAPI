from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from typing import Optional, List
from datetime import datetime
from sqlalchemy import String, DateTime, Float
from sqlalchemy.types import Enum as SQLEnum
import enum
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .profile import Profile
    from .property import Property
    from .deal import Deal
    from .notification import Notification
    from .review import Review
    from .message import Message
    from .task import Task
    from .favorite import Favorite
    from .view import View


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

    # oto
    profile: Mapped["Profile"] = relationship(back_populates="user", uselist=False)

    propertys: Mapped[List["Property"]] = relationship(back_populates="owner")
    deals: Mapped[List["Deal"]] = relationship(back_populates="buyer")
    notifications: Mapped[List["Notification"]] = relationship(back_populates="user")
    reviews: Mapped[List["Review"]] = relationship(back_populates="user")
    tasks: Mapped[List["Task"]] = relationship(back_populates="user")
    messages_sent: Mapped[List["Message"]] = relationship("Message", foreign_keys="Message.sender_id",
                                                          back_populates="sender")
    messages_received: Mapped[List["Message"]] = relationship("Message", foreign_keys="Message.recipient_id",
                                                              back_populates="recipient")
    favorites: Mapped[List["Favorite"]] = relationship(back_populates="user")
    views: Mapped[List["View"]] = relationship(back_populates="user")