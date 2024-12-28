from .base_settings import BaseSettingsConfig


class DevSettingsConfig(BaseSettingsConfig):
    DEBUG: bool = True
    LOG_LEVEL: str = "DEBUG"

    class Config:
        env_file = ".env.dev"
