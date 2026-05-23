import asyncio
import random
import logging
import aiohttp

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def retry_async(
    func,
    retries: int = 3,
    base_delay: float = 0.5,
    max_delay: float = 5,
    exceptions: tuple = (Exception,),
):
    for attempt in range(retries):
        try:
            return await func()

        except exceptions as e:
            if attempt == retries - 1:
                logger.error(f"Final attempt failed: {e}")
                raise

            delay = min(base_delay * (2 ** attempt), max_delay)
            jitter = random.uniform(0, delay * 0.1)

            logger.warning(
                f"Retry {attempt + 1}/{retries} failed: {e}, retrying in {delay + jitter:.2f}s"
            )

            await asyncio.sleep(delay + jitter)


async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://httpbin.org/status/500") as resp:
            if resp.status != 200:
                raise Exception(f"HTTP {resp.status}")
            return await resp.text()


async def main():
    try:
        result = await retry_async(fetch, retries=3)
        print(result)
    except Exception as e:
        print("Final failure:", e)


asyncio.run(main())



import time
import random
import requests


def retry_decorator(
    retries=3,
    base_delay=0.5,
    max_delay=5,
    exceptions=(Exception,),
):
    def wrapper(func):
        def inner(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)

                except exceptions as e:
                    if attempt == retries - 1:
                        print("Final failure:", e)
                        raise

                    delay = min(base_delay * (2 ** attempt), max_delay)
                    jitter = random.uniform(0, delay * 0.1)

                    print(f"Retry {attempt+1}, sleeping {delay+jitter:.2f}s")
                    time.sleep(delay + jitter)

        return inner
    return wrapper


@retry_decorator(retries=3)
def call_api():
    resp = requests.get("https://httpbin.org/status/500")
    if resp.status_code != 200:
        raise Exception(f"HTTP {resp.status_code}")
    return resp.text


try:
    call_api()
except Exception:
    pass



import time
import random
import requests


def retry_decorator(
    retries=3,
    base_delay=0.5,
    max_delay=5,
    exceptions=(Exception,),
):
    def wrapper(func):
        def inner(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)

                except exceptions as e:
                    if attempt == retries - 1:
                        print("Final failure:", e)
                        raise

                    delay = min(base_delay * (2 ** attempt), max_delay)
                    jitter = random.uniform(0, delay * 0.1)

                    print(f"Retry {attempt+1}, sleeping {delay+jitter:.2f}s")
                    time.sleep(delay + jitter)

        return inner
    return wrapper


@retry_decorator(retries=3)
def call_api():
    resp = requests.get("https://httpbin.org/status/500")
    if resp.status_code != 200:
        raise Exception(f"HTTP {resp.status_code}")
    return resp.text


try:
    call_api()
except Exception:
    pass


# import asyncio
# import random
# import logging

# logger = logging.getLogger(__name__)


# async def retry_async(
#     func,
#     retries: int = 3,
#     base_delay: float = 0.5,
#     max_delay: float = 10,
#     exceptions: tuple = (Exception,),
# ):
#     for attempt in range(retries):
#         try:
#             return await func()

#         except exceptions as e:
#             if attempt == retries - 1:
#                 logger.error(f"Final attempt failed: {e}")
#                 raise

#             # exponential backoff with jitter
#             delay = min(base_delay * (2 ** attempt), max_delay)
#             jitter = random.uniform(0, delay * 0.1)

#             logger.warning(
#                 f"Retry {attempt + 1}/{retries} failed: {e}, retrying in {delay + jitter:.2f}s"
#             )

#             await asyncio.sleep(delay + jitter)
            
# #Instead of writing your own, most teams use:
# #👉 tenacity

# from tenacity import retry, stop_after_attempt, wait_exponential

# @retry(stop=stop_after_attempt(3), wait=wait_exponential())
# def call_api():
#     return func()  
    
    
# def retry_decorator(
#     retries=3,
#     base_delay=0.5,
#     max_delay=10,
#     exceptions=(Exception,),
# ):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             for attempt in range(retries):
#                 try:
#                     return func(*args, **kwargs)

#                 except exceptions as e:
#                     if attempt == retries - 1:
#                         raise

#                     delay = min(base_delay * (2 ** attempt), max_delay)
#                     jitter = random.uniform(0, delay * 0.1)
#                     time.sleep(delay + jitter)

#             return None
#         return inner
#     return wrapper    