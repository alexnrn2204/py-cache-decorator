from typing import Callable


def cache(func: Callable) -> Callable:
    cache_stores = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = make_key(args, kwargs)

        if key not in cache_stores:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_stores[key] = result
        else:
            print("Getting from cache")
            result = cache_stores[key]

        return result

    return wrapper


def make_key(args: tuple, kwargs: dict) -> tuple:
    return args, tuple(sorted(kwargs.items()))
