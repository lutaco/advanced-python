import logging
from functools import wraps

logger = logging.getLogger('server.decorators')


def log(func):
    @wraps(func)
    def deco(request, *args, **kwargs):
        logger.debug(f'{func.__name__} called with request: {request}')
        return func(request, *args, **kwargs)
    return deco
