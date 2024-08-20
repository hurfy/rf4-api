from time   import time
from typing import Callable


def time_spent(func: Callable) -> Callable:
    """
    A decorator that calculates the execution time of a function
    """
    def wrapper(*args, **kwargs):
        start  = time()
        result = func(*args, **kwargs)

        print(f"[+] {func.__name__}: {round(time() - start, 2)}")

        return result

    return wrapper