import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from app_logging.log_handler import setup_logger


logger = setup_logger()

# Load the appropriate .env file based on the ENV environment variable
env_file_path =  "../.env.dev" # Default to .env.dev if ENV_FILE is not set
load_dotenv(env_file_path)  # Load the environment variables from the dynamically chosen file

class BaseSettingsConfig(BaseSettings):
    APP_NAME: str
    DEBUG: bool 
    LOG_LEVEL: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_DATABASE: str

    # logger.info(f"Loaded settings for {APP_NAME} + environmet loader {env_file_path}")

    # class Config:
    #     pass

# Create an instance of settings
settings = BaseSettingsConfig()



