import logging
import logging.config
from config.logging_config import get_logging_config

def setup_logger():
    logging.config.dictConfig(get_logging_config())
    return logging.getLogger("app")

# Usage:
logger = setup_logger()

# import logging
# import logging.config
# from config.logging_config import get_logging_config
# import inspect
# from pythonjsonlogger import jsonlogger


# class CustomJsonFormatter(jsonlogger.JsonFormatter):
#     def format(self, record):
#         # Dynamically populate filename, function name, and line number
#         frame = inspect.currentframe().f_back.f_back
#         record.filename = frame.f_code.co_filename
#         record.funcName = frame.f_code.co_name
#         record.lineno = frame.f_lineno

#         # Handle extra dictionary to avoid errors when empty
#         if not hasattr(record, 'extra'):
#             record.extra = None

#         return super().format(record)


# def get_logging_config_with_custom_formatter():
#     config = get_logging_config()

#     # Replace the formatter for JSON logs with the custom formatter
#     config["formatters"]["json"]["()"] = CustomJsonFormatter

#     return config


# def setup_logger():
#     logging.config.dictConfig(get_logging_config_with_custom_formatter())
#     return logging.getLogger("app")


