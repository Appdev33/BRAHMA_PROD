# app/main.py
from fastapi import FastAPI
from api.routes.user_routes import router as user_router
from config.base_settings import BaseSettingsConfig
from app_logging.log_handler import setup_logger
# from fastapi.middleware.cors import CORSMiddleware
from db.init_db import initialize_db  # Import the DB initialization function (used for development)
# REDIS CACHE INTEGRATION
# import aioredis
from utils.redis_cache import get_redis_pool

from exceptions.handlers import (
    email_already_taken_exception_handler, 
    user_already_exists_exception_handler, 
    user_not_found_exception_handler
)
from exceptions.user_exceptions import (
    EmailAlreadyTakenError, 
    UserAlreadyExistsException, 
    UserNotFoundException
)

app = FastAPI(
    title="User Service API",
    description="An extensible and modular FastAPI-based service for user management.",
    version="1.0.0"
)

# Middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Restrict in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

settings = BaseSettingsConfig()
logger = setup_logger()
redis = None  # Global variable for Redis client instance

# Register Routes
app.include_router(user_router, prefix="/api/users", tags=["Users"])

app.add_exception_handler(EmailAlreadyTakenError, email_already_taken_exception_handler)
app.add_exception_handler(UserAlreadyExistsException, user_already_exists_exception_handler)
app.add_exception_handler(UserNotFoundException, user_not_found_exception_handler)


# # Initialize the database (for dev purposes only)
# @app.on_event("startup")
# async def on_startup():
#     """Run during startup to initialize the database."""
#     try:
#         initialize_db()  # Synchronously initialize the database tables
#         logger.info(f"Starting {settings.APP_NAME} in {settings.DEBUG} mode")
#         logger.info("Database initialized successfully.")
#     except Exception as e:
#         logger.info(f"Error initializing the database: {e}")
#         # Optionally, handle errors like database connection failure

@app.on_event("startup")
async def on_startup():
    """
    Initialize resources (e.g., database and Redis) during application startup.
    Ensures proper error handling and logging for initialization.
    """
    global redis
    try:
        # Ensure the database is initialized asynchronously
        await initialize_db()  # Ensure you're awaiting the async function
        logger.info(f"Starting {settings.APP_NAME} in {settings.DEBUG} mode")
        logger.info("Database initialized successfully.")

        # Initialize Redis
        logger.info("Initializing Redis...")
        redis = await get_redis_pool() 
        logger.info("Redis initialized successfully.")
    except Exception as e:
        logger.error(f"Error initializing the database and redis: {e}")
        # Optionally, handle errors like database connection failure

# @app.on_event("shutdown")
# async def on_shutdown():
#     """Shutdown event to clean up resources gracefully."""
#     logger.info("Shutting down application.")
    
#     # Gracefully close the Redis connection pool
#     redis_pool = await get_redis_pool()
#     redis_pool.close()  # Close the Redis pool connection
#     await redis_pool.wait_closed()  # Wait for the pool to be fully closed
#     logger.info("Redis connection pool has been closed.")


@app.on_event("shutdown")
async def on_shutdown():
    """
    Cleanup resources (e.g., database and Redis) during application shutdown.
    """
    global redis
    try:
        # Close Redis connection if it exists
        if redis:
            logger.info("Closing Redis connection...")
            await redis.close()
            logger.info("Redis connection closed.")

        # Additional cleanup logic can be added here
        logger.info("Application shutdown completed successfully.")
    except Exception as e:
        logger.error("Error during shutdown cleanup.", exc_info=True)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

