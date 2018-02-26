import os
import logging
import logging.handlers

from utils import get_logs_dir

BOT_TOKEN = 'SET ME IN local_settings!!!'

# Logging
LOG_FILENAME = os.path.join(get_logs_dir(), 'balabot.log')  # name of log file
MAX_LOG_SIZE = 300 * 1024 * 1024  # means 300 megabytes

logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.ERROR,
                    format='%(asctime)s %(levelname)s %(name)s\n%(message)s',  # format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                    datefmt='%H:%M:%S')
log_handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=MAX_LOG_SIZE, backupCount=1)


from local_settings import *
