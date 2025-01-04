# # api/routes/user_routes.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.user_schema import UserRequestDTO, UserResponseDTO
from services.user_service import UserService
from db.sql.config import get_db
from exceptions.user_exceptions import EmailAlreadyTakenError, UserAlreadyExistsException, UserNotFoundException
from exceptions.handlers import email_already_taken_exception_handler, user_already_exists_exception_handler, user_not_found_exception_handler
from fastapi import HTTPException
from app_logging.log_handler import setup_logger
# import redis for caching purposes
from utils.redis_cache import RedisCache  # For caching




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
    
# #ASYNC OPERATION TO SCALE API AND CONCURRENCY
# # Route to get user by id
# @router.get("/{id}", response_model=UserResponseDTO)
# async def get_user_by_id(id: int, user_service: UserService = Depends(get_user_service)):
#     try:
#         user = await user_service.get_user_by_id(id)
#         logger.info(f"Successfully retrieved user with id {id}")
#         return user
#     except UserNotFoundException as e:
#         logger.error(f"User not found: {e.message}")
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=e.message
#         )
#     except Exception as e:
#         logger.error(f"Error while retrieving user: {str(e)}")
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail="Internal Server Error"
#         )

#ASYNC OPERATION TO SCALE WITH CACHING ON REDIS
# @router.get("/{id}", response_model=UserResponseDTO)
# async def get_user_by_id(id: int, user_service: UserService = Depends(get_user_service)):
#     try:
#         # Check if user data exists in Redis
#         cache_key = f"user:{id}"
#         cached_user = await RedisCache.get(cache_key)

#         if cached_user:
#             logger.info(f"Cache hit for user ID {id}")
#             return UserResponseDTO.parse_raw(cached_user)

#         logger.info(f"Cache miss for user ID {id}. Fetching from DB...")
#         user = user_service.get_user_by_id(id)

#         # Cache the user data for future requests
#         await RedisCache.set(cache_key, user.json(), ex=300)  # Cache expires in 5 minutes

#         return user
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

# Dependency for RedisCache
async def redis_cache(redis: RedisCache = Depends(RedisCache)):
    return redis

@router.get("/{id}", response_model=UserResponseDTO)
async def get_user_by_id(id: int, user_service: UserService = Depends(get_user_service)):
    print("################################")
    try:
        # Check Redis first
        cached_user = await RedisCache.get(f"user:{id}", UserResponseDTO)
        print("################################"+str(type(user)))
        if cached_user:
            logger.info(f"User with id {id} retrieved from Redis cache.")
            return cached_user  # Return cached data
        
        # If user is not in Redis, fetch from database
        user = await user_service.get_user_by_id(id)
        print("################################"+str(type(user)))
        
        # Cache the result in Redis with a timeout of 60 seconds
        await RedisCache.set(f"user:{id}", user, ttl=60)
        logger.info(f"User with id {id} retrieved from the database and cached.")
        
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


# THIS IS USED FOR LATER WHEN UPDATE OPERATION USED FOR CACHE Invalidate
# @router.put("/{id}", response_model=UserResponseDTO)
# async def update_user(id: int, user_update: UserUpdateDTO, user_service: UserService = Depends(get_user_service)):
#     try:
#         updated_user = user_service.update_user(id, user_update)

#         # Invalidate cache for the specific user and all users
#         cache_key = f"user:{id}"
#         all_users_key = "all_users"

#         await redis.delete(cache_key)
#         await redis.delete(all_users_key)

#         return updated_user
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
