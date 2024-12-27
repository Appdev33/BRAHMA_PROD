# app/main.py
from fastapi import FastAPI
from api.routes.user_routes import router as user_router
from db.init_db import initialize_db  # Import the DB initialization function (used for development)

app = FastAPI(
    title="User Service API",
    description="An extensible and modular FastAPI-based service for user management.",
    version="1.0.0"
)

# Register Routes
app.include_router(user_router, prefix="/api/users", tags=["Users"])

# Initialize the database (for dev purposes only)
@app.on_event("startup")
async def on_startup():
    # Initialize the database (create tables)
    initialize_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
