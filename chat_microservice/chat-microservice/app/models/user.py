from bson import ObjectId
from datetime import datetime

class User:
    def __init__(self, username: str, email: str):
        self.id = ObjectId()
        self.username = username
        self.email = email
        self.created_at = datetime.utcnow()

    def serialize(self) -> dict:
        return {
            "id": str(self.id),
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at.isoformat()
        }



# from abc import ABC, abstractmethod
# from pydantic import BaseModel
# from typing import Optional
# from bson import ObjectId


# class AbstractUser(ABC):
#     @abstractmethod
#     def get_role(self) -> str:
#         """Return the role of the user (e.g., 'admin', 'regular')."""
#         pass

#     @abstractmethod
#     def serialize(self) -> dict:
#         """Serialize the user data."""
#         pass


# # Concrete RegularUser class inheriting from AbstractUser
# class RegularUser(BaseModel, AbstractUser):
#     id: Optional[ObjectId] = None
#     username: str
#     email: str

#     def get_role(self) -> str:
#         return "regular"

#     def serialize(self) -> dict:
#         return {
#             "id": str(self.id),
#             "username": self.username,
#             "email": self.email,
#             "role": self.get_role()
#         }


# # # Concrete AdminUser class inheriting from AbstractUser
# # class AdminUser(BaseModel, AbstractUser):
# #     id: Optional[ObjectId] = None
# #     username: str
# #     email: str
# #     permissions: list  # Extra permissions for admin users

# #     def get_role(self) -> str:
# #         return "admin"

# #     def serialize(self) -> dict:
# #         return {
# #             "id": str(self.id),
# #             "username": self.username,
# #             "email": self.email,
# #             "permissions": self.permissions,
# #             "role": self.get_role()
# #         }
