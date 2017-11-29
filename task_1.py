import os
import sys

if os.name == 'nt':
    from time import clock as os_timer
else:
    from time import time as os_timer


import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def timer(f):
    def tmp(*args, **kwargs):
        t = os_timer()
        res = f(*args, **kwargs)
        logger.info("Время выполнения функции: %s" % (os_timer()-t))
        return res
    return tmp


@timer
def reverse(st):
    """
    Reverse symbols of the string.

    :param string: string to reverse.
    :returns: string that consists of the same symbols in reversed order.

    """
    return st[::-1]


if __name__ == "__main__":
    if len(sys.argv) == 2:
        logger.info(reverse(sys.argv[1]))
    elif len(sys.argv) == 1:
        logger.warning('Please specify one parameter')
    else:
        logger.warning('Please specify only one parameter')
