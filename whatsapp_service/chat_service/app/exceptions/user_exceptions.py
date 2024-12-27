class EmailAlreadyTakenError(Exception):
    def __init__(self, email: str):
        self.email = email
        self.message = f"Email {email} is already taken."
        super().__init__(self.message)


class UserAlreadyExistsException(Exception):
    def __init__(self, email: str):
        self.email = email
        self.message = f"Email {email} is already taken."
        super().__init__(self.message)


class UserNotFoundException(Exception):
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.message = f"User with ID {user_id} not found."
        super().__init__(self.message)
