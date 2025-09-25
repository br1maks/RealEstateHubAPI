from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext
from sqlalchemy.util import deprecated
import logging
from app.database import db_helper
from app.models.user import User
from app.repository.user.user_schemas import UserCreate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

pwd_context = CryptContext(schemes=["bcrypt"])

async def create_user(user: UserCreate) -> User | None:
    async for session in db_helper.session_dependency():
        try:
            hashed_password = pwd_context.hash(user.password)
            new_user = User(
                username=user.username,
                email=user.email,
                hashed_password=hashed_password
            )
            session.add(new_user)
            await session.commit()
            await session.refresh()
            logger.info(f"Создан пользователь с ID: {new_user.id}")
            return new_user
        except IntegrityError as e:
            logger.error(f"Ошибка создания пользователя: {e}")
            await session.rollback()
            return None
        except Exception as e:
            logger.error(f"Неизвестная ошибка: {e}")
            await session.rollback()
            return None