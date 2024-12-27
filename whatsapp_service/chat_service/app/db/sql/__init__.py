# import databases
# import sqlalchemy
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from .config import settings  # Correct the import for settings

# # Database connection URL (you can switch to PostgreSQL/MySQL by changing the URL)
# DATABASE_URL = settings.DATABASE_URL  # Assuming settings.DATABASE_URL contains the correct connection URL

# # Database setup
# database = databases.Database(DATABASE_URL)  # Use `databases` for async database interaction
# metadata = sqlalchemy.MetaData()

# # Create the base class for models
# Base = declarative_base(metadata=metadata)

# # Create a synchronous engine for transactions
# engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# # Create session
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Dependency to get the DB session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
