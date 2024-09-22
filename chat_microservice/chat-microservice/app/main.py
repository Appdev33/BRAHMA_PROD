import os
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from app.api.routes import router as api_router
from app.config.env_config import Settings
from app.utils.logger import logger

app = FastAPI()
settings = Settings()

@app.on_event("startup")
async def startup_db_client():
    try:
        app.mongodb_client = AsyncIOMotorClient(settings.mongodb_uri.get_secret_value())
        app.mongodb = app.mongodb_client[settings.mongodb_name]
        collections = await app.mongodb.list_collection_names()
        logger.info(f"Connected to MongoDB successfully. Collections: {collections}")
    except Exception as e:
        logger.error(f"Error connecting to MongoDB: {e}")


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()
    logger.info("MongoDB connection closed.")

# Include API routes
app.include_router(api_router)

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed.")
    return {"message": "Welcome to the Chat Microservice!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.host, port=settings.port)


# import os
# from fastapi import FastAPI
# from motor.motor_asyncio import AsyncIOMotorClient
# from app.api.routes import router as api_router
# from app.config.env_config import Settings
# from app.utils.logger import logger

# app = FastAPI()
# settings = Settings()

# @app.on_event("startup")
# async def startup_db_client():
#     try:
#         app.mongodb_client = AsyncIOMotorClient(settings.mongodb_uri.get_secret_value())
#         app.mongodb = app.mongodb_client[settings.mongodb_name]
#         collections = await app.mongodb.list_collection_names()
#         logger.info(f"Connected to MongoDB successfully. Collections: {collections}")
#     except Exception as e:
#         logger.error(f"Error connecting to MongoDB: {e}")


# @app.on_event("shutdown")
# async def shutdown_db_client():
#     app.mongodb_client.close()
#     logger.info("MongoDB connection closed.")

# # Include API routes
# app.include_router(api_router)

# @app.get("/")
# def read_root():
#     logger.info("Root endpoint accessed.")
#     return {"message": "Welcome to the Chat Microservice!"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host=settings.host, port=settings.port)

