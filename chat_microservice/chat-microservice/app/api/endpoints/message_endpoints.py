from fastapi import APIRouter, Depends
from app.schemas.message_schema import MessageCreate, MessageResponse
from app.services.chat_service import ChatService
from app.repositories.message_repository import MessageRepository
from motor.motor_asyncio import AsyncIOMotorClient
from app.config.env_config import Settings

router = APIRouter()
settings = Settings()

# Dependency
async def get_database() -> AsyncIOMotorClient:
    client = AsyncIOMotorClient(settings.mongo_uri)
    return client.chat_db

@router.post("/", response_model=MessageResponse)
async def send_message(message: MessageCreate, db: AsyncIOMotorClient = Depends(get_database)):
    message_repo = MessageRepository(db)
    chat_service = ChatService(message_repo)
    message_id = await chat_service.send_text_message(message.sender_id, message.receiver_id, message.content)
    return {"id": str(message_id), **message.dict()}
