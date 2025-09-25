from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum
from datetime import datetime

class RoleEnum(str, Enum):
    """Перечисление ролей пользователя."""
    buyer = "buyer"
    seller = "seller"
    admin = "admin"

class UserCreate(BaseModel):
    """Схема для создания нового пользователя (регистрация)."""
    username: str = Field(..., min_length=3, max_length=40, description="Имя пользователя")
    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(..., min_length=8, max_length=255, description="Пароль")

    class Config:
        json_schema_extra = {
            "example": {
                "username": "testuser",
                "email": "test@example.com",
                "password": "securepass123"
            }
        }

class UserUpdate(BaseModel):
    """Схема для обновления данных пользователя."""
    username: Optional[str] = Field(None, min_length=3, max_length=50, description="Новое имя пользователя")
    phone: Optional[str] = Field(None, min_length=10, max_length=20, description="Номер телефона")

    class Config:
        json_schema_extra = {
            "example": {
                "username": "newtestuser",
                "phone": "+1234567890"
            }
        }
class UserRead(BaseModel):
    """Схема для чтения данных пользователя (выходные данные)."""
    id: int
    username: str
    email: EmailStr
    role: RoleEnum
    is_active: bool
    is_verified: bool
    rating: Optional[float] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  
        json_schema_extra = {
            "example": {
                "id": 1,
                "username": "testuser",
                "email": "test@example.com",
                "role": "buyer",
                "is_active": True,
                "is_verified": False,
                "rating": 4.5,
                "created_at": "2025-09-25T15:00:00Z",
                "updated_at": "2025-09-25T15:00:00Z"
            }
        }

class UserLogin(BaseModel):
    """Схема для входа пользователя."""
    email: EmailStr = Field(..., description="Электронная почта для входа")
    password: str = Field(..., min_length=8, max_length=255, description="Пароль для входа")

    class Config:
        json_schema_extra = {
            "example": {
                "email": "test@example.com",
                "password": "securepass123"
            }
        }