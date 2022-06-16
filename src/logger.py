import logging


def get_console_handler():
    """
        Create and return a logging handler object with a particular formatter
    """
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    return handler


def get_logger(logger_name, log_level):
    """
        Create and return a python logger object
    """
    logger = logging.getLogger(logger_name)
    level = logging.getLevelName(log_level)
    logger.setLevel(level)
    logger.addHandler(get_console_handler())
    return logger
