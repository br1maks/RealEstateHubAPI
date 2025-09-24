from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path
from typing import Optional

BASE_DIR = Path(__file__).parent.parent

class DbSettings(BaseModel):
    """Database connection settings."""
    url: str = f"sqlite+aiosqlite:///{BASE_DIR / 'db.sqlite3'}"
    echo: bool = True
    test_url: Optional[str] = f"sqlite+aiosqlite:///:memory:"

class AuthJWT(BaseModel):
    """JWT authentication settings."""
    secret_key: str = "secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7

class Settings(BaseSettings):
    """Application-wide settings loaded from env or defaults."""
    db: DbSettings = DbSettings()
    auth_jwt: AuthJWT = AuthJWT()

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"  # Поддержка вложенных ключей (e.g., db__url)

settings = Settings()
"разобраться с енв и что туда добавлять, расспросить норамльный ли код"