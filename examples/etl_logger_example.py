import random
from retry import retry
from etl_decorators import logger
from etl_decorators.tasks import task_logger


@retry(ZeroDivisionError, tries=2, delay=1)
@task_logger(logger)
def to_break():
    if random.randint(0, 4) > 1:
        raise ZeroDivisionError


if __name__ == '__main__':
    for _ in range(1, 3):
        to_break()
