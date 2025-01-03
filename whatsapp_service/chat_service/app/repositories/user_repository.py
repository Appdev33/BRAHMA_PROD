
# from typing import Optional, List
# from models.sql import User


# class UserRepository:
#     def __init__(self):
#         self.users = {}  # In-memory storage for simplicity

#     def create_user(self, user: User) -> User:
#         self.users[user.id] = user
#         return user

#     def get_user_by_id(self, user_id: str) -> Optional[User]:
#         return self.users.get(user_id)

#     def get_all_users(self) -> List[User]:
#         return list(self.users.values())

#     def delete_user(self, user_id: str) -> bool:
#         if user_id in self.users:
#             del self.users[user_id]
#             return True
#         return False

# repositories/user_repository.py

from sqlalchemy.orm import Session
from models.sql.User import User
from schemas.user_schema import UserRequestDTO, UserResponseDTO
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from exceptions.user_exceptions import EmailAlreadyTakenError, UserAlreadyExistsException, UserNotFoundException
import time

# LIBRARY FOR ASYNC SESSION
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserRequestDTO) -> UserResponseDTO:
            # Check if the email already exists
            existing_user = self.db.query(User).filter(User.email == user.email).first()
            if existing_user:
                raise EmailAlreadyTakenError(user.email)  # Raise the custom exception

            # Create a new user in the database
            db_user = User(name=user.name, email=user.email, created_at=datetime.now(), updated_at=datetime.now())
            
            try:
                # Add the user to the session and commit to the database
                self.db.add(db_user)
                self.db.commit()
                self.db.refresh(db_user)  # Refresh to get the id and other DB fields
            except IntegrityError as e:
                self.db.rollback()  # Rollback in case of error
                raise ValueError(f"Error occurred: {str(e)}")

            # Return the user as a DTO
            return UserResponseDTO(
                id=str(db_user.id),  # Use db_user.id, which will have the generated ID after commit
                name=db_user.name,
                email=db_user.email,
                created_at=db_user.created_at.isoformat(),  
                updated_at=db_user.updated_at.isoformat(),  
            )



    # def get_user_by_id(self, user_id: int) -> UserResponseDTO | None:
    #     # Fetch user by ID
    #     db_user = self.db.query(User).filter(User.id == user_id).first()
    #     if db_user:
    #         return UserResponseDTO(
    #             id=str(db_user.id), 
    #             name=db_user.name,
    #             email=db_user.email,
    #             created_at=db_user.created_at,
    #             updated_at=db_user.updated_at,
    #         )
    #     return None

    #ASYCN QUERIES FOR ASYNC DB CHANGES
    
    async def get_user_by_id(self, user_id: int) -> UserResponseDTO | None:
        # Build and execute the async query
        stmt = select(User).where(User.id == user_id)
        result = await self.db.execute(stmt)  # Execute the query
        db_user = result.scalars().first()  # Extract the first result

        # Map the user to the response DTO if found
        if db_user:
            return UserResponseDTO(
                id=str(db_user.id),
                name=db_user.name,
                email=db_user.email,
                created_at=db_user.created_at,
                updated_at=db_user.updated_at,
            )
        return None

    def get_user_by_email(self, email: str) -> UserResponseDTO | None:
        # Fetch user by email
        db_user = self.db.query(User).filter(User.email == email).first()
        if db_user:
            return UserResponseDTO(
                id=str(db_user.id), 
                name=db_user.name,
                email=db_user.email,
                created_at=db_user.created_at,
                updated_at=db_user.updated_at,
            )
        return None

    def get_all_users(self) -> list[UserResponseDTO]:
        # Fetch all users and map them to DTOs
        # time.sleep(5)
        users = self.db.query(User).all()
        return [
            UserResponseDTO(
                id=str(user.id), 
                name=user.name,
                email=user.email,
                created_at=user.created_at,
                updated_at=user.updated_at,
            )
            for user in users
        ]

    def update_user(self, user_id: int, user_data: UserRequestDTO) -> UserResponseDTO | None:
        # Update user by ID
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user:
            db_user.name = user_data.name
            db_user.email = user_data.email
            db_user.updated_at = datetime.now()
            self.db.commit()
            self.db.refresh(db_user)
            return UserResponseDTO(
                id=db_user.id,
                name=db_user.name,
                email=db_user.email,
                created_at=db_user.created_at,
                updated_at=db_user.updated_at,
            )
        return None

    def delete_user(self, user_id: int) -> UserResponseDTO | None:
        # Delete user by ID
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
            return UserResponseDTO(
                id=str(db_user.id),
                name=db_user.name,
                email=db_user.email,
                created_at=db_user.created_at,
                updated_at=db_user.updated_at,
            )
        return None


