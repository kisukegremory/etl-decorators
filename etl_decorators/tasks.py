from functools import wraps
import logging

def etl_task(func):
    @wraps(func)
    def inner(*args, **kwargs):
        logging.info(f"Task: {func.__name__} started")
        result = func(*args, **kwargs)
        logging.info(f"Task: {func.__name__} success")
        return result
    return inner

def etl_flow(name = 'flow'):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            logging.info(f"Flow: {name} started")
            try:
                result = func(*args, **kwargs)
                logging.info(f"Flow: {name} success")
                return result
            except Exception as e:
                logging.critical(f"Flow: {name} failed ({e})")
        return inner
    return decorator
