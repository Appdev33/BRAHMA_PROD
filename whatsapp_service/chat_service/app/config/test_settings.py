from .base_settings import BaseSettingsConfig


class TestSettingsConfig(BaseSettingsConfig):
    DEBUG: bool = False
    LOG_LEVEL: str = "WARNING"

    class Config:
        env_file = ".env.test"
