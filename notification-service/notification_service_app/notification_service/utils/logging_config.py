# import logging
# from logging.handlers import RotatingFileHandler
# import os

# def configure_logging(microservice_name):
#     # Ensure logs directory exists
#     logs_dir = 'logs'
#     os.makedirs(logs_dir, exist_ok=True)

#     # Configure logging
#     logger = logging.getLogger(microservice_name)
#     logger.setLevel(logging.INFO)  # Default log level

#     # Create rotating file handler
#     log_file = os.path.join(logs_dir, f'{microservice_name}.log')
#     file_handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=10)  # 1 MB log files, keep 10 backup files
#     file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')  # Include microservice name in log format
#     file_handler.setFormatter(file_formatter)

#     # Add file handler to logger
#     logger.addHandler(file_handler)

#     # Also log to console
#     console_handler = logging.StreamHandler()
#     console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')  # Include microservice name in log format
#     console_handler.setFormatter(console_formatter)
#     logger.addHandler(console_handler)

#     return logger

# # Initialize logger
# logger = configure_logging("notification_service")