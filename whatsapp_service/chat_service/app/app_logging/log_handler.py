import logging
import logging.config
from config.logging_config import get_logging_config

def setup_logger():
    logging.config.dictConfig(get_logging_config())
    return logging.getLogger("app")

# Usage:
logger = setup_logger()
