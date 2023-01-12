from config.config import LOGGING_CONFIG
from logging import Logger
import logging.config


logging.config.dictConfig(LOGGING_CONFIG)

def get_logger(name: str) -> Logger:
    return logging.getLogger(name)

