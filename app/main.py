from typing import Callable


def cache(func: Callable) -> Callable:
    cache_stores = []

    def wrapper(*args, **kwargs) -> Callable:
        cache_find = [
            cache_store
            for cache_store in cache_stores
            if cache_store["args"] == args and cache_store["kwargs"] == kwargs
        ]
        if len(cache_find) == 0:
            result = func(*args, **kwargs)
            cache_stores.append({
                "args": args,
                "kwargs": kwargs,
                "result": result
            })
            print("Calculating new result")
        else:
            result = cache_find[0]["result"]
            print("Getting from cache")

        return result

    return wrapper
