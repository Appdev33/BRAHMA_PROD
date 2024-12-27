from repositories.user_repository import UserRepository
from schemas.user_schema import UserRequestDTO, UserResponseDTO
# from exceptions.custom_exceptions import UserNotFoundException
from typing import List
from models.sql.User import User
from exceptions.user_exceptions import EmailAlreadyTakenError, UserAlreadyExistsException, UserNotFoundException


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user_request: UserRequestDTO) -> UserResponseDTO:
        # Use repository to create user and return the DTO directly
        return self.user_repository.create_user(user_request)

    def get_user_by_id(self, user_id: int) -> UserResponseDTO:
        # Use repository to fetch user by ID
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise UserNotFoundException(f"User with ID {user_id} not found.")
        return user

    def get_all_users(self) -> List[UserResponseDTO]:
        # Use repository to fetch all users and return the list of DTOs
        return self.user_repository.get_all_users()

    def update_user(self, user_id: int, user_request: UserRequestDTO) -> UserResponseDTO:
        # Use repository to update user by ID and return the DTO directly
        updated_user = self.user_repository.update_user(user_id, user_request)
        if not updated_user:
            raise UserNotFoundException(f"User with ID {user_id} not found.")
        return updated_user

    def delete_user(self, user_id: int) -> bool:
        # Use repository to delete user by ID
        deleted_user = self.user_repository.delete_user(user_id)
        if not deleted_user:
            raise UserNotFoundException(f"User with ID {user_id} not found.")
        return True
