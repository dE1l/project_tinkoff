import os
import sys
from functools import wraps

if os.name == 'nt':
    from time import clock as os_timer
else:
    from time import time as os_timer

import logging


def timeit(level):
    def decorator(func):
        logger = logging.getLogger(__name__)
        logging.basicConfig(level=level)
        @wraps(func)
        def wrapper(*args, **kwargs):
            t = os_timer()
            res = func(*args, **kwargs)
            logger.info("Время выполнения функции: %s" % (os_timer()-t))
            return res
        return wrapper
    return decorator


@timeit(logging.INFO)
def reverse(st):
    """
    Reverse symbols of the string.

    :param string: string to reverse.
    :returns: string that consists of the same symbols in reversed order.

    """
    return st[::-1]


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) == 2:
        logger.info(reverse(sys.argv[1]))
    elif len(sys.argv) == 1:
        logger.warning('Please specify one parameter')
    else:
        logger.warning('Please specify only one parameter')
