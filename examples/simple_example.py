import logging
from etl_decorators.tasks import etl_task


@etl_task
def logging_madoka(magic: str) -> str:
    print(f"é a magic {magic}")
    return magic

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    logger.addHandler(handler)


    name = logging_madoka('madoka')
    print(name)
