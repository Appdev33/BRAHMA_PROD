# from datetime import datetime
# from typing import Dict, Optional
# from sqlalchemy import Column, Integer, String, DateTime
# from sqlalchemy.orm import declarative_base

# Base = declarative_base()

# class User(Base):
#     """User model implementing SQLBaseModel for user-specific logic."""
#     __tablename__ = 'users'  # Define the table name for the model

#     id = Column(Integer, primary_key=True, index=True)  # Primary key column
#     name = Column(String, nullable=False)  # Add a `name` column to the User model
#     email = Column(String, unique=True, index=True, nullable=False)
#     created_at = Column(DateTime, default=datetime.now)
#     updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

#     def __init__(self, name: str, email: str, created_at: Optional[datetime] = None, updated_at: Optional[datetime] = None):
#         self.name = name  # Assign the `name` argument to the name attribute
#         self.email = email
#         self.created_at = created_at or datetime.now()
#         self.updated_at = updated_at or datetime.now()

#     def set_timestamps(self, is_update: bool = False):
#         """Set creation or updated timestamp based on the operation."""
#         if is_update:
#             self.updated_at = datetime.now()
#         else:
#             self.created_at = datetime.now()
#             self.updated_at = datetime.now()

#     def to_dict(self) -> Dict[str, str | int]:
#         """Convert the User object to a dictionary."""
#         return {
#             "id": self.id,
#             "name": self.name,  # Include `name` in the dictionary representation
#             "email": self.email,
#             "created_at": self.created_at.isoformat(),
#             "updated_at": self.updated_at.isoformat(),
#         }

#     @classmethod
#     def from_dict(cls, data: Dict[str, str | int]) -> "User":
#         """Create a User object from a dictionary."""
#         return cls(
#             name=data.get("name", ""),
#             email=data.get("email", ""),
#             created_at=datetime.fromisoformat(data["created_at"]) if "created_at" in data else None,
#             updated_at=datetime.fromisoformat(data["updated_at"]) if "updated_at" in data else None,
#         )

#     def __repr__(self):
#         return (
#             f"<User(id={self.id}, name={self.name}, email={self.email}, "
#             f"created_at={self.created_at}, updated_at={self.updated_at})>"
#         )

# from sqlalchemy import Column, Integer, String, DateTime
# from db.sql.config import Base  # Make sure you import Base from the right module
# from datetime import datetime

# class User(Base):
#     __tablename__ = 'users'  # Table name in the database

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(255), nullable=False)
#     email = Column(String(255), nullable=False, unique=True)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

from sqlalchemy import Column, Integer, String, DateTime
from db.sql.config import Base  # Make sure you import Base from the right module
from datetime import datetime

class User(Base):
    __tablename__ = 'users'  # Table name in the database

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)  # `name` column with a max length of 255 characters
    email = Column(String(255), nullable=False, unique=True)  # `email` column, unique constraint applied
    created_at = Column(DateTime, default=datetime.utcnow)  # `created_at` defaults to UTC time
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # `updated_at` auto-updates on record change

    def __repr__(self):
        return (
            f"<User(id={self.id}, name={self.name}, email={self.email}, "
            f"created_at={self.created_at}, updated_at={self.updated_at})>"
        )

    def to_dict(self) -> dict:
        """Convert the User object to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,  # Include `name` in the dictionary representation
            "email": self.email,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        """Create a User object from a dictionary."""
        return cls(
            name=data.get("name", ""),
            email=data.get("email", ""),
            created_at=datetime.fromisoformat(data["created_at"]) if "created_at" in data else None,
            updated_at=datetime.fromisoformat(data["updated_at"]) if "updated_at" in data else None,
        )

