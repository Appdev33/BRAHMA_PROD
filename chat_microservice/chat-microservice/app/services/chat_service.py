from app.repositories.message_repository import MessageRepository
from app.models.message import Message
from app.schemas.message_schema import MessageCreate

class ChatService:
    def __init__(self, message_repo: MessageRepository):
        self.message_repo = message_repo

    async def create_message(self, message_data: MessageCreate):
        message = Message(sender_id=message_data.sender_id, receiver_id=message_data.receiver_id, content=message_data.content)
        return await self.message_repo.create(message)

    async def get_message_by_id(self, message_id: str):
        return await self.message_repo.get_by_id(message_id)

    async def get_all_messages(self):
        return await self.message_repo.get_all()



# from motor.motor_asyncio import AsyncIOMotorClient
# from app.models.message import Message  # Adjust according to your model
# from app.schemas.message_schema import MessageCreate, MessageResponse

# class ChatService:
#     def __init__(self, mongodb):
#         self.mongodb = mongodb

#     async def create_message(self, message_data: MessageCreate) -> MessageResponse:
#         message = Message(content=message_data.content, user_id=message_data.user_id)
#         await self.mongodb.messages.insert_one(message.serialize())
#         return MessageResponse(id=message.id, content=message.content, user_id=message.user_id)


# from app.models.message import Message
# from app.schemas.message_schema import MessageCreate, MessageResponse
# from app.repositories.message_repository import MessageRepository
# from app.services.chat_service_interface import ChatServiceInterface

# class ChatService(ChatServiceInterface):
#     def __init__(self):
#         self.repository = MessageRepository()

#     def create_message(self, message_data: MessageCreate) -> MessageResponse:
#         message = Message(
#             sender_id=message_data.sender_id,
#             receiver_id=message_data.receiver_id,
#             content=message_data.content
#         )
#         self.repository.create(message)
#         return MessageResponse(
#             id=message.id,
#             sender_id=message.sender_id,
#             receiver_id=message.receiver_id,
#             content=message.content,
#             timestamp=message.timestamp,
#             read=message.read
#         )
