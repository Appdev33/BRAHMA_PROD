from motor.motor_asyncio import AsyncIOMotorDatabase
from app.models.user import User
from app.repositories.base_repository import BaseRepository
from typing import List
from bson import ObjectId

class UserRepository(BaseRepository[User]):
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db["users"]

    async def create(self, user: User) -> User:
        user_dict = user.serialize()
        await self.collection.insert_one(user_dict)
        return user

    async def get_all(self) -> List[User]:
        cursor = self.collection.find()
        users = await cursor.to_list(length=100)
        return [User(**user) for user in users]

    async def get_by_id(self, user_id: str) -> User:
        user_data = await self.collection.find_one({"_id": ObjectId(user_id)})
        return User(**user_data) if user_data else None


# from typing import List
# from app.models.user import User
# from app.repositories.base_repository import BaseRepository

# class UserRepository(BaseRepository[User]):
#     def __init__(self):
#         self.users: List[User] = []

#     def create(self, user: User) -> User:
#         self.users.append(user)
#         return user

#     def get_all(self) -> List[User]:
#         return self.users

#     def get_by_id(self, user_id: str) -> User:
#         for user in self.users:
#             if str(user.id) == user_id:
#                 return user
#         return None
