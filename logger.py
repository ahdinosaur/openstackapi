import logging
import os
from pythonjsonlogger import jsonlogger

log_level = os.getenv('LOG_LEVEL', logging.DEBUG)

logger = logging.getLogger()
logger.setLevel(log_level)

log_handler = logging.StreamHandler()
json_formatter = jsonlogger.JsonFormatter()
log_handler.setFormatter(json_formatter)
logger.addHandler(log_handler)
