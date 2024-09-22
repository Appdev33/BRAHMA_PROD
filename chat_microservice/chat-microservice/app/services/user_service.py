from app.repositories.user_repository import UserRepository
from app.models.user import User
from app.schemas.user_schema import UserCreate

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def create_user(self, user_data: UserCreate):
        user = User(username=user_data.username, email=user_data.email)
        return await self.user_repo.create(user)

    async def get_user_by_id(self, user_id: str):
        return await self.user_repo.get_by_id(user_id)
    
    async def get_all_users(self):
        return await self.user_repo.get_all()



# from motor.motor_asyncio import AsyncIOMotorClient
# from app.models.user import User
# from app.schemas.user_schema import UserCreate, UserResponse

# class UserService:
#     def __init__(self, mongodb):
#         self.mongodb = mongodb

#     async def create_user(self, user_data: UserCreate) -> UserResponse:
#         user = User(username=user_data.username, email=user_data.email)
#         await self.mongodb.users.insert_one(user.serialize())
#         return UserResponse(id=user.id, username=user.username, email=user.email)


# from app.models.user import User
# from app.schemas.user_schema import UserCreate, UserResponse
# from app.repositories.user_repository import UserRepository
# from app.services.user_service_interface import UserServiceInterface

# class UserService(UserServiceInterface):
#     def __init__(self):
#         self.repository = UserRepository()

#     def create_user(self, user_data: UserCreate) -> UserResponse:
#         user = User(username=user_data.username, email=user_data.email)
#         self.repository.create(user)
#         return UserResponse(id=user.id, username=user.username, email=user.email)
