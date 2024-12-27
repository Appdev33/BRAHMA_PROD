# app/exceptions/custom_exceptions.py

from fastapi import HTTPException

# Custom exception for User not found
class UserNotFoundException(HTTPException):
    def __init__(self, user_id: str):
        detail = f"User with ID {user_id} not found."
        super().__init__(status_code=404, detail=detail)
