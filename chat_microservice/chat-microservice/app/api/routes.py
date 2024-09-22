from fastapi import APIRouter, Depends
from typing import List
from app.schemas.user_schema import UserCreate, UserResponse
from app.schemas.message_schema import MessageCreate, MessageResponse
from app.services.user_service import UserService
from app.services.chat_service import ChatService
from app.repositories.user_repository import UserRepository
from app.repositories.message_repository import MessageRepository
from app.utils.db import get_db  # Import the get_db function from the utility file

router = APIRouter()

# Initialize services
@router.post("/users", response_model=UserResponse)
async def create_user(user_data: UserCreate, db=Depends(get_db)):
    user_service = UserService(UserRepository(db))
    return await user_service.create_user(user_data)

@router.get("/users", response_model=List[UserResponse])
async def get_all_users(db=Depends(get_db)):
    user_service = UserService(UserRepository(db))
    return await user_service.get_all_users()

@router.post("/messages", response_model=MessageResponse)
async def create_message(message_data: MessageCreate, db=Depends(get_db)):
    chat_service = ChatService(MessageRepository(db))
    return await chat_service.create_message(message_data)

@router.get("/messages", response_model=List[MessageResponse])
async def get_all_messages(db=Depends(get_db)):
    chat_service = ChatService(MessageRepository(db))
    return await chat_service.get_all_messages()



# from fastapi import APIRouter, HTTPException
# from app.schemas.user_schema import UserCreate, UserResponse
# from app.schemas.message_schema import MessageCreate, MessageResponse
# from app.services.user_service import UserService
# from app.services.chat_service import ChatService

# router = APIRouter()
# user_service = UserService()
# chat_service = ChatService()

# @router.post("/users", response_model=UserResponse)
# async def create_user(user_data: UserCreate):
#     user = await user_service.create_user(user_data)
#     if user is None:
#         raise HTTPException(status_code=400, detail="User could not be created.")
#     return user

# @router.post("/messages", response_model=MessageResponse)
# async def create_message(message_data: MessageCreate):
#     message = await chat_service.create_message(message_data)
#     if message is None:
#         raise HTTPException(status_code=400, detail="Message could not be created.")
#     return message
