from abc import ABC, abstractmethod
from app.schemas.message_schema import MessageCreate, MessageResponse

class ChatServiceInterface(ABC):
    @abstractmethod
    def create_message(self, message_data: MessageCreate) -> MessageResponse:
        pass
