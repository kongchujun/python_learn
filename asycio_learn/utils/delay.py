import asyncio
import time
import functools
from typing import Callable, Any
async def delay(seconds:int) -> int:
    print(f"sleeping for {seconds} seconds...")
    await asyncio.sleep(seconds)
    print(f"finished for {seconds} seconds...")
    return seconds

def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args: Any, **kwargs: Any) -> Any:
            print(f"starting {func}...with args {args}, kwargs {kwargs}")
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f"finished {func} in {total:.4f} seconds")
        return wrapped
    return wrapper
