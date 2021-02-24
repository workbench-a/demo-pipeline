"""Cnfiguration for python logger.
"""
import sys
import logging
from demo_model.config import config

FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s —" "%(funcName)s:%(lineno)d — %(message)s"
)

def get_console_handler():
    """Setup for logging handler."""
    if config.LOG_MODE == "file":
        console_handler = logging.FileHandler(f"{config.LOGGING_DIR}/{config.LOG_FILE}")
    elif config.LOG_MODE == "console":
        console_handler = logging.StreamHandler(sys.stdout)

    console_handler.setFormatter(FORMATTER)
    return console_handler
