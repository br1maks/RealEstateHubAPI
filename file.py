import asyncio
from app.database import db_helper
from app.models import User

async def user_crud():
    async for session in db_helper.session_dependency():
        try:
            # Добавление пользователя с username и hashed_password
            new_user = User(username="testuser", email="test@example.com", hashed_password="testpass123")
            session.add(new_user)
            await session.commit()
            print(f"Добавлен User с ID: {new_user.id}")

            # Проверка
            added_user = await session.get(User, new_user.id)
            print(f"Проверено: {added_user.username} (ID: {added_user.id})")

            # Удаление
            await session.delete(added_user)
            await session.commit()
            print(f"Удалён User с ID: {new_user.id}")

            # Проверка удаления
            deleted_user = await session.get(User, new_user.id)
            print(f"Проверка удаления: {deleted_user}")
        except Exception as e:
            await session.rollback()
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    asyncio.run(user_crud())