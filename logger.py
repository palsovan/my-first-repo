import logging

def setup_logger(name, log_file, level=logging.INFO):
    """Function to set up a logger with file and console handlers"""
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Create a default logger
default_logger = setup_logger('default_logger', 'app.log')

def log_info(message):
    default_logger.info(message)

def log_warning(message):
    default_logger.warning(message)

def log_error(message):
    default_logger.error(message)