# from black.linegen import should_split_funcdef_with_rhs
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, async_scoped_session
# from asyncio import current_task
#
#
# from app.models.base import Base
# from app.core.config import settings
#
# class DataBaseHelper:
#     """Helper class for managing asynchronous database connections and sessions."""
#     def __init__(self, test_mode: bool = True):
#         url = settings.db.test_url if test_mode else settings.db.url
#         self.engine = create_async_engine(url=url, echo=settings.db.echo)
#         self.session_factory = async_sessionmaker(
#             bind=self.engine,
#             autoflush=False,
#             autocommit=False,
#             expire_on_commit=False,
#         )
#
#     def get_scoped_session(self):
#         """Returns a scoped session bound to the current async task."""
#         session = async_scoped_session(
#             session_factory=self.session_factory,
#             scopefunc = current_task,
#         )
#         return session
#
#     async def session_dependency(self) -> AsyncSession:
#         """Provides an async session as a dependency for FastAPI."""
#
#         session = self.get_scoped_session()
#         async with session() as sess:
#             yield sess
#         await session.remove()
#
#     async def create_tables(self):
#         """Creates all tables based on models."""
#         async with self.engine.begin() as conn:
#             await conn.run_sync(Base.metadata.create_all)
#
# db_helper = DataBaseHelper()

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, async_scoped_session
from asyncio import current_task
from app.core.config import settings

class DatabaseHelper:
    def __init__(self):
        self.engine = create_async_engine(settings.db.url, echo=settings.db.echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        session = self.get_scoped_session()
        async with session() as sess:
            yield sess
        await session.remove()

    async def scoped_session_dependency(self) -> AsyncSession:
        session = self.get_scoped_session()
        yield session
        await session.close()

db_helper = DatabaseHelper()
