from motor.motor_asyncio import AsyncIOMotorDatabase
from app.models.message import Message
from app.repositories.base_repository import BaseRepository
from typing import List
from bson import ObjectId

class MessageRepository(BaseRepository[Message]):
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db["messages"]

    async def create(self, message: Message) -> Message:
        message_dict = message.serialize()
        await self.collection.insert_one(message_dict)
        return message

    async def get_all(self) -> List[Message]:
        cursor = self.collection.find()
        messages = await cursor.to_list(length=100)
        return [Message(**msg) for msg in messages]

    async def get_by_id(self, message_id: str) -> Message:
        message_data = await self.collection.find_one({"_id": ObjectId(message_id)})
        return Message(**message_data) if message_data else None



# from typing import List
# from app.models.message import Message
# from app.repositories.base_repository import BaseRepository

# class MessageRepository(BaseRepository[Message]):
#     def __init__(self):
#         self.messages: List[Message] = []

#     def create(self, message: Message) -> Message:
#         self.messages.append(message)
#         return message

#     def get_all(self) -> List[Message]:
#         return self.messages

#     def get_by_id(self, message_id: str) -> Message:
#         for message in self.messages:
#             if str(message.id) == message_id:
#                 return message
#         return None
