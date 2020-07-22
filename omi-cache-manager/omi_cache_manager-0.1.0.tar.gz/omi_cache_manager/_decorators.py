import functools
from functools import wraps
import asyncio

def async_method_in_loop(func):
    @wraps(func)
    async def async_method_wrapper(*args, **kwargs):
        future = asyncio.get_event_loop().run_in_executor(None, 
            functools.partial(
                func,
                *args,
                **kwargs
            )
        )
        return await future
    return async_method_wrapper