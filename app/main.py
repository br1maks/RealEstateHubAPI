import asyncio
from app.database import db_helper
from app.models import Amenity

async def test_amenity_crud():
    async for session in db_helper.session_dependency():
        try:
            new_amenity=Amenity(name="wi-fi")
            # session.add(new_amenity)
            # await session.commit()
            print(f"Добавлен Amenity с ID: {new_amenity.id}")

            added_amenity = await session.get(Amenity, new_amenity.id)
            print(f"Проверено: {added_amenity.name} (ID: {added_amenity.id})")

            await session.delete(added_amenity)
            await session.commit()

            deleted_amenity = await session.get(Amenity, new_amenity.id)
            print(f"Удалено: {deleted_amenity.name} (ID: {deleted_amenity.id})")
        except Exception as e:
            await session.rollback()
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    asyncio.run(test_amenity_crud())