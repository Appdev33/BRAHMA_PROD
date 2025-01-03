# test_config.py

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load the environment variables from .env.test file
env_file_path_test =  "../.env.test" # Default to .env.dev if ENV_FILE is not set
load_dotenv(env_file_path_test)  # Load the environment variables from the dynamically chosen file
load_dotenv("../tests/config/.env.test")

class TestSettingsConfig(BaseSettings):
    # Database configuration
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_DATABASE: str

    # API configuration for testing
    TEST_API_URL: str
    TEST_LOG_LEVEL: str

# Create an instance of the settings for test-specific use
test_settings = TestSettingsConfig()

# Example usage
print(test_settings.TEST_API_URL)  # Prints the test API URL
