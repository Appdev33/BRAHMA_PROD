# db_init.py
from db.sql.config import Base, engine  # Import Base and engine from your config file

def initialize_db():
    """Create all database tables."""
    print("Creating tables in the database...")
    # Create all tables in the database (only for development or setup)
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")

if __name__ == "__main__":
    initialize_db()
