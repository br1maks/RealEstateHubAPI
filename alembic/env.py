import asyncio
from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config
from alembic import context

# Загрузка конфигурации Alembic
config = context.config

# Настройка логирования из файла конфигурации, если он указан
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Импорт метаданных моделей и настроек
from app.models.base import Base
from app.core.config import settings

target_metadata = Base.metadata

# Установка URL базы данных из настроек приложения
config.set_main_option("sqlalchemy.url", settings.db.url)

def run_migrations_offline() -> None:
    """Выполнение миграций в оффлайн-режиме."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection: Connection) -> None:
    """Выполнение миграций с использованием существующего соединения."""
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_async_migrations() -> None:
    """Асинхронное выполнение миграций."""
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()

def run_migrations_online() -> None:
    """Запуск миграций в онлайн-режиме."""
    asyncio.run(run_async_migrations())

# Выбор режима выполнения миграций
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()