import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S"
logging.basicConfig(filename='my.log', level=10, format=LOG_FORMAT, datefmt=DATE_FORMAT)

logging.info("hello world")
