import logging
import os
LOG_LEVEL = "DEBUG" if os.environ.get(
    "FLASK_ENV") == "development" else "INFO"


def get_console_handler():
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    return handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    level = logging.getLevelName(LOG_LEVEL)
    logger.setLevel(level)
    logger.addHandler(get_console_handler())
    return logger
