import os
import time
from logging.config import fileConfig
from model import Base
from sqlalchemy import engine_from_config, create_engine
from sqlalchemy import pool
from sqlalchemy.exc import OperationalError

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.
# def get_url():
#     return os.getenv("DATABSE_URL", "postgresql://myuser:mypassword@db:5432/weatherplatform")


postgres_url = os.getenv("DATABASE_URL", config.get_main_option("sqlalchemy.url"))
config.set_main_option("sqlalchemy.url", postgres_url)

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    database_url = os.getenv(
        "DATABASE_URL", 
        "postgresql://myuser:mypassword@localhost:5432/weatherplatform"
    )

    retries = 5
    while retries > 0:
        try:
            # Create a temporary engine to test the actual live connection
            test_engine = create_engine(database_url)
            with test_engine.connect() as conn:
                pass
            break  # Connection successful! Exit the retry loop.
        except OperationalError:
            retries -= 1
            print(f"Database not ready yet. Waiting... ({retries} retries left)")
            time.sleep(3)
    if retries == 0:
        raise RuntimeError("Could not connect to the database. Migration aborted.")
    
    configuration = context.config.get_section(context.config.config_ini_section) or {}
    configuration["sqlalchemy.url"] = database_url
        
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
