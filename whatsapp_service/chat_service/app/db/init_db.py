from db.sql.config import Base, engine
from sqlalchemy import inspect

def initialize_db():
    """Create all database tables only if they don't exist."""
    print("Checking if tables need to be created...")
    
    # Check if tables already exist in the database
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()

    # Only create tables if they don't already exist
    if not existing_tables:
        print("No tables found, creating tables...")
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully.")
    else:
        print("Tables already exist. No action needed.")

if __name__ == "__main__":
    initialize_db()
