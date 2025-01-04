import redis.asyncio as redis
import json
from typing import Optional
from pydantic import BaseModel
from fastapi import Depends, HTTPException
from config.base_settings import settings
from app_logging.log_handler import setup_logger



logger = setup_logger()

# Initialize Redis connection pool
# async def get_redis_pool() -> redis.Redis:
#     pool = redis.ConnectionPool(
#         host=settings.REDIS_HOST,
#         port=settings.REDIS_PORT,
#         # password=settings.REDIS_PASSWORD,
#         # db=settings.REDIS_DB,
#         decode_responses=True,
#         max_connections=20  # max connections in the pool
#     )
#     redis_client = redis.Redis(connection_pool=pool)
#     return redis_client
async def get_redis_pool() -> redis.Redis:
    print(">>>>>>>>>>>>")
    try:
        pool = redis.ConnectionPool(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            decode_responses=True,
            max_connections=20
        )
        print(">>>>>>>>>>>>")
        redis_client = redis.Redis(connection_pool=pool)
        print(">>>>>>>>>>>>")
        return redis_client
    except Exception as e:
        logger.error(f"Error initializing Redis connection: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# A Cache class to interact with Redis
class RedisCache:
    def __init__(self, redis: redis.Redis):
        logger.info(f"Initializing RedisCache with Redis client: {redis}")
        self.redis = redis

    # async def get(self, key: str, model: BaseModel = None) -> Optional[BaseModel]:
        
    #     data = await self.redis.get(key, model)
    #     print("$$$$$$$$$$$$$$$$$$$$$$$$$$$"+str(type(data)))
    #     if data:
    #         data_dict = json.loads(data)
    #         if model:
    #             return model(**data_dict)  # Convert dictionary to Pydantic model
    #         return data_dict
    #     return None
    
    async def get(self, key: str, model: BaseModel = None) -> Optional[BaseModel]:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("3333333333333"+str(redis))
        try:
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            # Attempt to fetch data from Redis
            print("hello world")
            print(f"Fetching from Redis using key: {key}")
            # data = await self.redis.get("14")
            data = await self.redis.get(key,BaseModel)
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$>>>>>>")
            if data:
                # Parse the data if it exists
                print(f"Data found: {data}")
                data_dict = json.loads(data)
                if model:
                    # Deserialize data into Pydantic model
                    return model(**data_dict)
                return data_dict
            return None
            
        # except redis.exceptions.ConnectionError as e:
        #     logger.error(f"Redis connection error while fetching key {key}: {str(e)}")
        #     # Returning None in case of Redis connection failure
        #     return None

        # except redis.exceptions.TimeoutError as e:
        #     logger.error(f"Redis timeout error while fetching key {key}: {str(e)}")
        #     # Returning None in case of a timeout
        #     return None

        # except json.JSONDecodeError as e:
        #     logger.error(f"Error decoding JSON data for key {key}: {str(e)}")
        #     # Returning None in case of a JSON decoding error
        #     return None

        except Exception as e:
            logger.error(f"Unexpected error while retrieving key {key}: {str(e)}")
            # Catch any other unexpected errors
            return None



    async def set(self, key: str, value: BaseModel, ttl: int = 3600) -> None:
        # Convert Pydantic model to dictionary and store it in Redis
        await self.redis.setex(key, ttl, json.dumps(value.dict()))

    async def delete(self, key: str) -> None:
        await self.redis.delete(key)


# Dependency for getting Redis cache
# def redis_cache(redis: redis.Redis = Depends(get_redis_pool)) -> RedisCache:
#     return RedisCache(redis)

# import redis.asyncio as redis
# # import redis.asyncio as aioredis  # Use redis.asyncio instead of aioredis
# import json
# from typing import Optional
# from fastapi import Depends
# from config.base_settings import settings # Assuming the settings are stored here for DB config


# # Initialize Redis connection pool
# async def get_redis_pool() -> redis.Redis:
#     pool = redis.ConnectionPool(
#         host=settings.REDIS_HOST,
#         port=settings.REDIS_PORT,
#         # password=settings.REDIS_PASSWORD,
#         # db=settings.REDIS_DB,
#         decode_responses=True,
#         max_connections=20  # max connections in the pool
#     )
#     # Use the pool to create the Redis client
#     redis_client = redis.Redis(connection_pool=pool)
#     return redis_client

# # A Cache class to interact with Redis
# class RedisCache:
#     def __init__(self, redis: redis.Redis):
#         self.redis = redis

#     async def get(self, key: str) -> Optional[dict]:
#         data = await self.redis.get(key)
#         if data:
#             return json.loads(data)
#         return None

#     async def set(self, key: str, value: dict, ttl: int = 3600) -> None:
#         await self.redis.setex(key, ttl, json.dumps(value))

#     async def delete(self, key: str) -> None:
#         await self.redis.delete(key)

# # Dependency for getting Redis cache
# def redis_cache(redis: redis.Redis = Depends(get_redis_pool)) -> RedisCache:
#     return RedisCache(redis)

