from db.sql.config import Base, engine
from sqlalchemy import inspect
from app_logging.log_handler import setup_logger

import asyncio

logger = setup_logger()

# def initialize_db():
#     """Create all database tables only if they don't exist."""
#     logger.info(f"Database driver: {engine.dialect.name} ({engine.dialect.driver})")

#     logger.info("Checking if tables need to be created...")
    
#     # Check if tables already exist in the database
#     inspector = inspect(engine)
#     existing_tables = inspector.get_table_names()

#     # Only create tables if they don't already exist
#     if not existing_tables:
#         logger.info("No tables found, creating tables...")
#         Base.metadata.create_all(bind=engine)
#         logger.info("Tables created successfully.")
#     else:
#         logger.info("Tables already exist. No action needed.")

# Database Initialization
async def initialize_db():
    """Create all database tables only if they don't exist."""
    try:
        logger.info(f"Database driver: {engine.dialect.name} ({engine.dialect.driver})")
        logger.info("Checking if tables need to be created...")

        async with engine.connect() as conn:
            inspector = await conn.run_sync(inspect)
            existing_tables = inspector.get_table_names()

            if not existing_tables:
                logger.info("No tables found, creating tables...")
                await conn.run_sync(Base.metadata.create_all)
                logger.info("Tables created successfully.")
            else:
                logger.info(f"Existing tables: {existing_tables}. No action needed.")
    except Exception as e:
        logger.error(f"Error initializing the database: {e}")
    finally:
        # Dispose of the engine to close connections
        await engine.dispose()

# Main Entry Point
if __name__ == "__main__":
    asyncio.run(initialize_db())

