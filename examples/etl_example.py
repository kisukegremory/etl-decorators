
from retry import retry
import logging
import random
from etl_decorators.tasks import etl_task, etl_flow

@retry(ZeroDivisionError,tries=4,delay=2)
@etl_task
def extract() -> dict:
    if random.randint(0, 4) > 1:
        logging.error("Error in asking for help!")
        raise ZeroDivisionError
    return {'response':200, 'data':'Puella Magi Madoka Magica'}


@etl_task
def transform(response: dict) -> list:
    words: str = response['data']
    words = words.split(" ")
    words = [word.upper() for word in words]
    return words


def load(words: list):
    print("SHE CAME, is the: ")
    for word in words:
        print(word)

@etl_flow('MadokaFlow')
def main():
    extracted = extract()
    transformed = transform(extracted)
    load(transformed)

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    logger.addHandler(handler)

    main()
