from functools import wraps
import logging


def etl_task(func):
    @wraps(func)
    def inner(*args, **kwargs):
        logging.info(f'Task: {func.__name__} started')
        result = func(*args, **kwargs)
        logging.info(f'Task: {func.__name__} success')
        return result

    return inner


def etl_flow(name='flow'):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            logging.info(f'Flow: {name} started')
            try:
                result = func(*args, **kwargs)
                logging.info(f'Flow: {name} success')
                return result
            except Exception as e:
                logging.critical(f'Flow: {name} failed ({e})')

        return inner

    return decorator


def task_logger(logger: logging.Logger):
    """
    A decorator that uses a logger to log the beginning of a function and its end for a pipeline pattern of events
    example:
    >> logger = logging.getLogger(__name__)
    >> @task_logger(logger)
    >> def example():
    >>      pass
    """

    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            logger.info(f'{func.__name__} started')
            try:
                result = func(*args, **kwargs)
                logger.info(f'{func.__name__} success')
                return result
            except Exception as e:
                logger.critical(f'{func.__name__} failed')
                raise e
        return inner

    return decorator
