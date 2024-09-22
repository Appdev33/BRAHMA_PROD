import os
from pydantic_settings import BaseSettings
from pydantic import SecretStr, Field

class Settings(BaseSettings):
    mongodb_uri: SecretStr = Field(..., env="MONGODB_URI")  # MongoDB URI
    mongodb_name: str = Field(..., env="MONGODB_NAME")      # Database name
    host: str = Field("127.0.0.1", env="APP_HOST")           # App host
    port: int = Field(8000, env="APP_PORT")                  # App port
    
    class Config:
        env_file = ".env"  # Load default .env file
        env_file_encoding = 'utf-8'

# Override the env_file based on the ENVIRONMENT variable
environment = os.getenv("ENVIRONMENT")
if environment:
    Settings.Config.env_file = f".env.{environment}"  # Load based on ENVIRONMENT variable

settings = Settings()




# import os
# from pydantic_settings import BaseSettings
# from pydantic import SecretStr

# class Settings(BaseSettings):
#     mongodb_uri: SecretStr  # This will store the MongoDB URI securely
#     mongodb_name: str        # Database name

#     class Config:
#         env_file = ".env"      # Load environment variables from .env file
#         env_file_encoding = 'utf-8'

# settings = Settings()
