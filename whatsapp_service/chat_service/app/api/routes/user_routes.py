# # api/routes/user_routes.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.user_schema import UserRequestDTO, UserResponseDTO
from services.user_service import UserService
from db.sql.config import get_db
from exceptions.user_exceptions import EmailAlreadyTakenError, UserAlreadyExistsException, UserNotFoundException
from exceptions.handlers import email_already_taken_exception_handler, user_already_exists_exception_handler, user_not_found_exception_handler
from fastapi import HTTPException
# import logging.config
# from config.logging_config import get_logging_config
from app_logging.log_handler import setup_logger

# Apply the logging configuration
# logging.config.dictConfig(get_logging_config())


# Initialize logger
# logger = logging.getLogger("Controller Chat Application")
logger = setup_logger()
router = APIRouter()

# Dependency Injection
def get_user_service(db: Session = Depends(get_db)) -> UserService:
    from repositories.user_repository import UserRepository
    return UserService(UserRepository(db))


@router.post("/", response_model=UserResponseDTO, status_code=201)
def create_user(user_request: UserRequestDTO, user_service: UserService = Depends(get_user_service)):
    try:
        return user_service.create_user(user_request)
    except EmailAlreadyTakenError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message
        )
    except UserAlreadyExistsException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message
        )
    except UserNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error Checking"
        )


# @router.get("/{id}", response_model=UserResponseDTO)
# def get_user_by_id(id: int, user_service: UserService = Depends(get_user_service)):
#     try:
#         logger.info(f"Successfully retrieved {user_service.get_user_by_id(id).name} ")
#         return user_service.get_user_by_id(id)
#     except UserNotFoundException as e:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=e.message
#         )
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail="Internal Server Error"
#         )
    
#ASYNC OPERATION TO SCALE API AND CONCURRENCY
# Route to get user by id
@router.get("/{id}", response_model=UserResponseDTO)
async def get_user_by_id(id: int, user_service: UserService = Depends(get_user_service)):
    try:
        user = await user_service.get_user_by_id(id)
        logger.info(f"Successfully retrieved user with id {id}")
        return user
    except UserNotFoundException as e:
        logger.error(f"User not found: {e.message}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message
        )
    except Exception as e:
        logger.error(f"Error while retrieving user: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


@router.get("/", response_model=list[UserResponseDTO])
async def get_all_users(user_service: UserService = Depends(get_user_service)):
    logger.info("Start processing request to get all users")
    try:
        logger.info("Fetching user data...") 
        users = user_service.get_all_users()  # No need for await here
        logger.info(f"Successfully retrieved {len(users)} users")
        return users
    except Exception as e:
        logger.error(f"An error occurred while fetching users: {e}", exc_info=True)
        raise



@router.delete("/{id}", status_code=204)
def delete_user(id: int, user_service: UserService = Depends(get_user_service)):
    try:
        # Attempt to delete the user
        user_service.delete_user(id)
        
        # Log successful deletion
        # logger.info(f"User with ID {id} deleted successfully.")

        # Returning None and 204 No Content for successful deletion (no body in response)
        return {"message": f"User with ID {id} deleted successfully."}
    except UserNotFoundException as e:
        # Handle case where user is not found
        # logger.warning(f"Attempted to delete non-existent user with ID {id}.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message  # Custom message for user not found
        )
    except Exception as e:
        # Log unexpected errors and raise a generic internal server error
        # logger.error(f"Error occurred while deleting user with ID {id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error occurred while deleting user."
        )

