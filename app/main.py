import asyncio
from app.database import db_helper
from app.models.base import Base

async def main():
    await db_helper.create_tables()
    async for sess in db_helper.session_dependency():
        print('Session OK')
        await sess.close()
        break

if __name__ == "__main__":
    asyncio.run(main())