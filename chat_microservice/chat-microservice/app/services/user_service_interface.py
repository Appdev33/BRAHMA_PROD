from abc import ABC, abstractmethod
from app.schemas.user_schema import UserCreate, UserResponse

class UserServiceInterface(ABC):
    @abstractmethod
    def create_user(self, user_data: UserCreate) -> UserResponse:
        pass
