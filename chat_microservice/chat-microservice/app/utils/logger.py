import logging
import os
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "app.log")

def setup_logger():
    logger = logging.getLogger("chat_microservice")
    logger.setLevel(LOG_LEVEL)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL)

    # File handler with rotation
    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=10**6, backupCount=5)
    file_handler.setLevel(LOG_LEVEL)

    # Formatter
    formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s - '
    'Module: %(module)s - Function: %(funcName)s - '
    'Line: %(lineno)d - Process ID: %(process)d'
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

logger = setup_logger()
