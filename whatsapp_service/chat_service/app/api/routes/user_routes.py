# api/routes/user_routes.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user_schema import UserRequestDTO, UserResponseDTO
from services.user_service import UserService
from db.sql.config import get_db

router = APIRouter()

# Dependency Injection
def get_user_service(db: Session = Depends(get_db)) -> UserService:
    from repositories.user_repository import UserRepository
    return UserService(UserRepository(db))


@router.post("/", response_model=UserResponseDTO, status_code=201)
async def create_user(user_request: UserRequestDTO, user_service: UserService = Depends(get_user_service)):
    return user_service.create_user(user_request)


@router.get("/{id}", response_model=UserResponseDTO)
async def get_user_by_id(id: int, user_service: UserService = Depends(get_user_service)):
    return user_service.get_user_by_id(id)


@router.get("/", response_model=list[UserResponseDTO])
async def get_all_users(user_service: UserService = Depends(get_user_service)):
    return user_service.get_all_users()


@router.delete("/{id}", status_code=204)
async def delete_user(id: int, user_service: UserService = Depends(get_user_service)):
    user_service.delete_user(id)
    return None
