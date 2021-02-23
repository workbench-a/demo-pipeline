from demo_model.config import config
import logging
import sys

# PSA: Multiple calls to logging.getLogger('someLogger') return a
# reference to the same logger object.  This is true not only
# within the same module, but also across modules as long as
# it is in the same Python interpreter process.

FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s —" "%(funcName)s:%(lineno)d — %(message)s"
)

def get_console_handler():
    """Setup for logging handler."""
    if(config.LOG_MODE == "file"):
        console_handler = logging.FileHandler(f"{config.LOGGING_DIR}/{config.LOG_FILE}")
    elif(config.LOG_MODE == "console"):
        console_handler = logging.StreamHandler(sys.stdout)

    console_handler.setFormatter(FORMATTER)
    return console_handler