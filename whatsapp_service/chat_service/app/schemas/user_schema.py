from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserRequestDTO(BaseModel):
    name: str
    email: EmailStr


class UserResponseDTO(BaseModel):
    id: str  
    name: str
    email: str
    created_at: datetime | None  # Can be a datetime string or formatted string
    updated_at: datetime | None  # Can be a datetime string or formatted string

    class Config:
        orm_mode = True  # This allows the Pydantic model to work seamlessly with SQLAlchemy models

