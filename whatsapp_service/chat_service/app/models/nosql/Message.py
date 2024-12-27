# models/nosql/message.py
from datetime import datetime
from interfaces.NoSqlModel import NoSqlModel

class Message(NoSqlModel):
    """Represents a message stored in NoSQL (e.g., MongoDB)."""
    
    def __init__(self, message_id: str, sender_id: int, receiver_id: int, content: str, content_type: str, created_at: datetime = None):
        self._message_id = message_id
        self._sender_id = sender_id
        self._receiver_id = receiver_id
        self._content = content
        self._content_type = content_type
        self._created_at = created_at or datetime.now()

    @property
    def id(self) -> str:
        return self._message_id

    @id.setter
    def id(self, value: str):
        self._message_id = value

    @property
    def sender_id(self) -> int:
        return self._sender_id

    @sender_id.setter
    def sender_id(self, value: int):
        self._sender_id = value

    @property
    def receiver_id(self) -> int:
        return self._receiver_id

    @receiver_id.setter
    def receiver_id(self, value: int):
        self._receiver_id = value
    
    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, value: str):
        self._content = value

    @property
    def content_type(self) -> str:
        return self._content_type

    @content_type.setter
    def content_type(self, value: str):
        self._content_type = value

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @created_at.setter
    def created_at(self, value: datetime):
        self._created_at = value

    def to_dict(self):
        return {
            "id": self.id,
            "sender_id": self.sender_id,
            "receiver_id": self.receiver_id,
            "content": self.content,
            "content_type": self.content_type,
            "created_at": self.created_at
        }


message = Message(
    message_id="12345", 
    sender_id=1, 
    receiver_id=2, 
    content="Hello, this is a test message!", 
    content_type="text"
)

# Print the created message object
print(message)