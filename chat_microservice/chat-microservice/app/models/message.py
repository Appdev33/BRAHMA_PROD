from bson import ObjectId
from datetime import datetime

class Message:
    def __init__(self, sender_id: ObjectId, receiver_id: ObjectId, content: str):
        self.id = ObjectId()
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content
        self.timestamp = datetime.utcnow()
        self.read = False

    def serialize(self) -> dict:
        return {
            "id": str(self.id),
            "sender_id": str(self.sender_id),
            "receiver_id": str(self.receiver_id),
            "content": self.content,
            "timestamp": self.timestamp.isoformat(),
            "read": self.read
        }


# from abc import ABC, abstractmethod
# from bson import ObjectId
# from datetime import datetime

# # Custom ObjectIdStr class for validation
# class ObjectIdStr(str):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError('Invalid ObjectId')
#         return ObjectId(v)

# # Abstract Message class
# class AbstractMessage(ABC):
#     @abstractmethod
#     def get_type(self) -> str:
#         """Return the type of the message (e.g., 'text', 'media')."""
#         pass

#     @abstractmethod
#     def serialize(self) -> dict:
#         """Return the serialized data of the message."""
#         pass

# # Concrete TextMessage class inheriting from AbstractMessage
# class TextMessage(AbstractMessage):
#     id: ObjectIdStr = None
#     sender_id: ObjectIdStr
#     receiver_id: ObjectIdStr
#     content: str
#     timestamp: datetime = None
#     read: bool = False

#     def get_type(self) -> str:
#         return "text"

#     def serialize(self) -> dict:
#         return {
#             "id": str(self.id) if self.id else None,
#             "sender_id": str(self.sender_id),
#             "receiver_id": str(self.receiver_id),
#             "content": self.content,
#             "timestamp": self.timestamp.isoformat() if self.timestamp else None,
#             "read": self.read,
#             "type": self.get_type()
#         }
