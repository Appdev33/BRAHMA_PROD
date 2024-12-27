# app/main.py
from fastapi import FastAPI
from api.routes.user_routes import router as user_router
from db.init_db import initialize_db  # Import the DB initialization function (used for development)
from exceptions.handlers import (
    email_already_taken_exception_handler, 
    user_already_exists_exception_handler, 
    user_not_found_exception_handler
)
from exceptions.user_exceptions import (
    EmailAlreadyTakenError, 
    UserAlreadyExistsException, 
    UserNotFoundException
)

app = FastAPI(
    title="User Service API",
    description="An extensible and modular FastAPI-based service for user management.",
    version="1.0.0"
)

# Register Routes
app.include_router(user_router, prefix="/api/users", tags=["Users"])

app.add_exception_handler(EmailAlreadyTakenError, email_already_taken_exception_handler)
app.add_exception_handler(UserAlreadyExistsException, user_already_exists_exception_handler)
app.add_exception_handler(UserNotFoundException, user_not_found_exception_handler)


# Initialize the database (for dev purposes only)
@app.on_event("startup")
async def on_startup():
    """Run during startup to initialize the database."""
    try:
        initialize_db()  # Synchronously initialize the database tables
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing the database: {e}")
        # Optionally, handle errors like database connection failure

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
