import logging
import inspect

class Utils(object):
    def common_headers_json(self):
        headers = {
            "Content-Type": "application/json",
        }
        return headers

    def common_headers_xml(self):
        headers = {
            "Content-Type": "application/xml",
        }
        return headers

    @staticmethod
    def custom_logger(log_level=logging.DEBUG):
        logger_name=inspect.stack()[1][3]
        logger=logging.getLogger(logger_name)
        logger.setLevel(log_level)
        fh=logging.FileHandler("automation.log")
        formatter=logging.Formatter('%(asctime)s-%(levelname)s:%(name)s:%(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger