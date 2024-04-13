
import logging
from logging.handlers import RotatingFileHandler
import os

def configure_logging(microservice_name):
    # Ensure logs directory exists
    logs_dir = 'logs'
    os.makedirs(logs_dir, exist_ok=True)

    # Configure logging
    logging.basicConfig(level=logging.INFO)  # Default log level

    # Create rotating file handler
    log_file = os.path.join(logs_dir, f'{microservice_name}.log')
    file_handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=10)  # 1 MB log files, keep 10 backup files
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - {microservice_name} - %(message)s')  # Include microservice name in log format
    file_handler.setFormatter(file_formatter)

    # Add file handler to root logger
    logger = logging.getLogger('')
    logger.addHandler(file_handler)

    return logger
