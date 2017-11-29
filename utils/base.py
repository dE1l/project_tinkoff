import json


def is_json(myjson):
    try:
        json.loads(myjson)
    except (ValueError, TypeError):
        return False
    return True


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]




