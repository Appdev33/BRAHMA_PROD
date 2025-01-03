import asyncio
import httpx
import time

BASE_URL = "http://127.0.0.1:8000/api/users"

async def get_user_by_id(client, user_id):
    try:
        response = await client.get(f"{BASE_URL}/{user_id}")
        print(f"User {user_id}: {response.status_code}")
    except Exception as e:
        print(f"Error fetching user {user_id}: {e}")

async def run_concurrent_requests(concurrent_users, user_ids):
    async with httpx.AsyncClient() as client:
        tasks = [get_user_by_id(client, user_id) for user_id in user_ids[:concurrent_users]]
        start_time = time.time()
        await asyncio.gather(*tasks)
        end_time = time.time()
        print(f"Completed {concurrent_users} requests in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    print("Running concurrent requests")
    concurrent_users = 10
    user_ids = list(range(1, 11))  # Simulating 10 user IDs (1 to 10)
    asyncio.run(run_concurrent_requests(concurrent_users, user_ids))
