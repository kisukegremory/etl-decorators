import logging

logger = logging.getLogger(__name__)
formatter = logging.Formatter(
    '%(name)s - %(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(handler)
