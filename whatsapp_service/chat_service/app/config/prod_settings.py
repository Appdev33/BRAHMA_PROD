from .base_settings import BaseSettingsConfig


class ProdSettingsConfig(BaseSettingsConfig):
    DEBUG: bool = False
    LOG_LEVEL: str = "ERROR"

    class Config:
        env_file = ".env.prod"
