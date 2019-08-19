from functools import reduce
from settings import INSTALLED_MODULES


def get_server_actions():
    return reduce(
        lambda value, item: value + tuple(getattr(item, 'actionnames', tuple())),
        reduce(
            lambda value, item: value + (getattr(item, 'actions', tuple()),),
            reduce(
                lambda value, item: value + (__import__(f'{item}.actions'),),
                INSTALLED_MODULES,
                tuple(),
            ),
            tuple(),
        ),
        tuple(),
    )


def resolve(action, actions=None):
    for x in actions or get_server_actions():
        if x.get('actions') == action:
            return x.get('controller')

    return None
