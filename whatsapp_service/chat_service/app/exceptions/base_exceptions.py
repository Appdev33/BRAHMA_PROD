from fastapi import HTTPException

class DatabaseError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class EmailAlreadyTakenError(Exception):
    def __init__(self, email: str):
        self.email = email
        self.message = f"Email {email} is already taken."
        super().__init__(self.message)

class UserNotFoundException(HTTPException):
    def __init__(self, user_id: str):
        super().__init__(status_code=404, detail=f"User with ID {user_id} not found")
