import logging


logging.basicConfig(
    level=logging.DEBUG,
    encoding='utf-8',
    filename="log_file.log",
    format="%(asctime)s -- %(module)s -- %(levelname)s -- %(message)s",
    datefmt='%d_%m_%Y %H:%M:%S',
)
