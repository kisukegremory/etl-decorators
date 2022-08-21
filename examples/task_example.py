
from retry import retry
import logging
import random

from etl_decorators.tasks import etl_task

@retry(ZeroDivisionError,tries=2,delay=1)
@etl_task
def to_break():
    if random.randint(0, 4) > 1:
        raise ZeroDivisionError

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    logger.addHandler(handler)

    for _ in range(1,3):
        to_break()