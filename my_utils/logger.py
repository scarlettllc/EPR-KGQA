import logging
from config import Config
import os

class Logger:

    log_format = '%(asctime)s %(name)s %(levelname)s %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    level_dict = {"DEBUG":logging.DEBUG, "INFO":logging.INFO, "WARN":logging.WARNING}
    log_file = Config.log_process
    if os.path.exists(log_file):
        os.remove(log_file)
    log_level = level_dict[Config.log_level]
    logging.basicConfig(filename=log_file, level=log_level, format=log_format, datefmt=date_format)
    
    @staticmethod
    def get_logger(name="Preprocess", to_stdout=False):
        logger = logging.getLogger(name)
        if to_stdout:
            logger.addHandler(logging.StreamHandler())
        return logging.getLogger(name)