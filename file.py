import asyncio
from app.database import db_helper
from app.models import Property, PropertyTypeEnum, Category

async def test_property_crud():
    async for session in db_helper.session_dependency():
        try:
            # Предварительно создаём категорию (если её нет)
            new_category = Category(name="Apartment Category")
            session.add(new_category)
            await session.commit()

            # Добавление объекта недвижимости с category_id
            new_property = Property(
                title="Test Apartment",
                price=100000.0,
                location="Test City",
                area=80.0,
                type=PropertyTypeEnum.apartment,
                owner_id=1,  # Предполагаем, что есть пользователь с ID 1
                category_id=new_category.id
            )
            session.add(new_property)
            await session.commit()
            print(f"Добавлен Property с ID: {new_property.id}")

            # Проверка
            added_property = await session.get(Property, new_property.id)
            print(f"Проверено: {added_property.title} (ID: {added_property.id})")

            # Удаление
            await session.delete(added_property)
            await session.delete(new_category)  # Удаляем категорию
            await session.commit()
            print(f"Удалён Property с ID: {new_property.id}")

            # Проверка удаления
            deleted_property = await session.get(Property, new_property.id)
            print(f"Проверка удаления: {deleted_property}")
        except Exception as e:
            await session.rollback()
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    asyncio.run(test_property_crud())