# app/utils/db.py
from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi import Request

# Dependency function to get the MongoDB database from the FastAPI app
def get_db(request: Request) -> AsyncIOMotorDatabase:
    return request.app.mongodb
