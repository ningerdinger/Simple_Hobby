import sys
import logging

class logger:
    def __init__(self):
        print('test')
        logger = logging.Logger('AmazeballsLogger')
        #Stream/console output
        logger.handler = logging.StreamHandler(sys.stdout)
        logger.handler.setLevel(logging.WARNING)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        logger.handler.setFormatter(formatter)

        #File output
        fh = logging.FileHandler("test.log")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
        logger.addHandler(fh)