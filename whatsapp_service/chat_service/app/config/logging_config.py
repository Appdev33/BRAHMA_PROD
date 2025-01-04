
from pythonjsonlogger import jsonlogger

def get_logging_config():
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {
                "()": jsonlogger.JsonFormatter,
                  "format": "%(asctime)s %(name)s %(levelname)s %(message)s %(filename)s  %(extra)s"
            },
            "default": {
                  "format": "%(asctime)s %(name)s %(levelname)s %(message)s %(filename)s  %(extra)s"
            }
        },
        "handlers": {
            "console": {
                "level": "INFO",
                "class": "logging.StreamHandler",
                "formatter": "json",
            },
            "file": {
                "level": "ERROR",
                "class": "logging.FileHandler",
                "filename": "app_logs.json",
                "formatter": "json",
            },
        },
        "loggers": {
            "uvicorn": {
                "level": "INFO",
                "handlers": ["console", "file"],
                "propagate": True,
            },
            "uvicorn.error": {
                "level": "ERROR",
                "handlers": ["console", "file"],
                "propagate": False,
            },
            "uvicorn.access": {
                "level": "INFO",
                "handlers": ["console", "file"],
                "propagate": True,  # Ensure propagation is enabled
            },
            "app": {
                "level": "INFO",
                "handlers": ["console", "file"],
                "propagate": True,
            },
        },
    }




