from sqlalchemy.orm import Session
# from app_logging.log_handler import setup_logger
# from exceptions.user_exceptions import EmailAlreadyTakenError
from scripts.faker_data_generator import generate_fake_users




# logger = setup_logger()

def populate_users(num_users: int):
    """Populate the database with fake users using the UserService."""
    db = Session
    

    fake_users = generate_fake_users(num_users)
    
    for fake_user in fake_users:
        try:
            # Use the UserService to create the user
            db.add(fake_user)
            # logger.info(f"Successfully added user {fake_user.email}")    
        except Exception as e:
            # logger.warning(f"Email {e.message} is already taken. Skipping this user.")
            pass
        except Exception as e:
            pass
            # logger.error(f"Error occurred while adding user {fake_user.email}: {str(e)}")

    # logger.info(f"Finished populating {num_users} users.")

if __name__ == "__main__":
    # Populate the database with fake users (e.g., 100 users)
    populate_users(100)
