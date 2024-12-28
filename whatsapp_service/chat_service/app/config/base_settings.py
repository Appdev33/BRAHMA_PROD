from pydantic_settings import BaseSettings



class BaseSettingsConfig(BaseSettings):
    APP_NAME: str = "FastAPI Chat Microservice"
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        
# from pydantic_settings import BaseSettings


# class BaseSettingsConfig(BaseSettings):
#     APP_NAME: str = "FastAPI Chat Microservice"
#     DEBUG: bool = False
#     LOG_LEVEL: str = "INFO"

#     # Database configurations
#     MYSQL_USER: str
#     MYSQL_PASSWORD: str
#     MYSQL_HOST: str
#     MYSQL_PORT: int
#     MYSQL_DATABASE: str

#     class Config:
#         # Specify the .env file if needed
#         env_file = ".env"  # You can specify a different file based on your environment


# # Initialize settings
# settings = BaseSettingsConfig()

