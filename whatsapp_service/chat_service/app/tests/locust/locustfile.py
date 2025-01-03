from locust import HttpUser, task, between
from config.test_config import test_settings
import random

BASE_URL = test_settings.TEST_API_URL  # Using test API URL from the config

class UserBehavior(HttpUser):
    # Simulate wait time between requests
    wait_time = between(1, 3)  # Simulate 1-2 seconds of wait time between requests

    @task
    def get_user_by_id(self):
        user_id = random.randint(13, 33)  # Random user ID between 1 and 10
        response = self.client.get(f"{BASE_URL}/users/{user_id}")
        print(f"User {user_id}: {response.status_code} - {response.text}")

# from locust import HttpUser, task, between
# from prometheus_client import start_http_server, Summary, Counter
# import random
# from config.test_config import test_settings

# BASE_URL = test_settings.TEST_API_URL  # Using test API URL from the config

# # Define Prometheus metrics
# REQUESTS_TOTAL = Counter('locust_requests_total', 'Total number of requests processed')
# REQUESTS_DURATION = Summary('locust_requests_duration_seconds', 'Request duration in seconds')

# # Start the Prometheus HTTP server on port 8089
# start_http_server(8089)

# class UserBehavior(HttpUser):
#     # Simulate wait time between requests
#     wait_time = between(1, 3)  # Simulate 1-3 seconds of wait time between requests

#     @task
#     @REQUESTS_DURATION.time()
#     def get_user_by_id(self):
#         user_id = random.randint(13, 33)  # Random user ID between 13 and 33
#         response = self.client.get(f"{BASE_URL}/users/{user_id}")
#         print(f"User {user_id}: {response.status_code} - {response.text}")
#         REQUESTS_TOTAL.inc()  # Increment request counter after every request

