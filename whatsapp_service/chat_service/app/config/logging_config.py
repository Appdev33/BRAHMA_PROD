import logging
import logging.config
from pythonjsonlogger import jsonlogger

def get_logging_config():
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {
                "()": jsonlogger.JsonFormatter,
                "format": "%(asctime)s %(name)s %(levelname)s %(message)s %(extra)s"
            },
            "default": {
                "format": "%(asctime)s %(name)s %(levelname)s %(message)s"
            }
        },
        "handlers": {
            "console": {
                "level": "INFO",  # Make sure it's INFO or lower (e.g., DEBUG)
                "class": "logging.StreamHandler",
                "formatter": "json",
            },
            "file": {
                "level": "INFO",  # Same here, INFO level for file handler
                "class": "logging.FileHandler",
                "filename": "app_logs.json",
                "formatter": "json",
            },
        },
        "loggers": {
            "uvicorn": {
                "level": "INFO",  # Ensure uvicorn logs at INFO level
                "handlers": ["console", "file"],
                "propagate": True,
            },
            "uvicorn.error": {
                "level": "ERROR",
                "handlers": ["console", "file"],
                "propagate": False,
            },
            "uvicorn.access": {
                "level": "INFO",  # Ensure access logs are captured at INFO level
                "handlers": ["console", "file"],
                "propagate": False,
            },
            "app": {
                "level": "INFO",  # Ensure your app logs are also captured at INFO level
                "handlers": ["console", "file"],
                "propagate": True,
            },
        },
    }

