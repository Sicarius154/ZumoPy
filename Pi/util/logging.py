import logging
from datetime import datetime

class Logging:
    def __init__(self, path):
        self.path = path
        logging.basicConfig(filename="{datetime.now()[8:]}_{path}", level=logging.INFO)

    def log_info(string):
        log.info(f"{datetime.now()[8:]}--{string}")

    def log_error(string):
        log.error(f"{datetime.now()[8:]}--{string}")

    def log_warn(string):
        log.warning(f"{datetime.now()[8:]}--{string}")
