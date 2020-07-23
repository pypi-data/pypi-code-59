import os

from functools import wraps
from inspect import signature


class BaseLogger:
    """ Log public functions and @properties of subclasses"""

    def __init_subclass__(cls, **kwargs):
        log_limit = int(log_limit) if (log_limit := os.getenv("LOG_LIMIT")) else 100

        for attribute_name in dir(cls):
            attribute = getattr(cls, attribute_name)
            if attribute_name.startswith("_"):
                continue
            if isinstance(cls.__dict__.get(attribute_name), staticmethod):
                wrapped_static_method = log_method(attribute, prefix=f"{cls.__name__}.", log_limit=log_limit)
                setattr(cls, attribute_name, staticmethod(wrapped_static_method))
            elif isinstance(cls.__dict__.get(attribute_name), property):
                wrapped_property = property(log_method(attribute.fget, prefix=f"{cls.__name__}.", log_limit=log_limit))
                setattr(cls, attribute_name, wrapped_property)
            elif callable(attribute):
                wrapped_callable = log_method(attribute, prefix=f"{cls.__name__}.", log_limit=log_limit)
                setattr(cls, attribute_name, wrapped_callable)


def log_method(func, prefix="", log_limit: int = None):
    """
    Log the method name with args and kwargs.
    If there is a return value from the function, it will be printed.
    e.g.
        @log_function(prefix="foo.")
        def function_name(x, y, z=100):
            ...
        function_name()
        >> foo.function_name
    :param func: decorated function to log
    :param prefix: logged descriptor to the function
    :param log_limit: limit the number of characters printed to console
    """

    @wraps(func)
    def with_logging(*args, **kwargs):
        if callable(func):
            print(f"{prefix}{func.__name__}")
            arg_keys = []
            for i, arg in enumerate(args):  # record all args
                if not str(arg).startswith("<"):  # skip logging object references
                    arg_keys.append(list(signature(func).parameters.keys())[i])
                    print(f"\t{arg_keys[-1]}: {str(arg)[:log_limit]}")
            for k, v in kwargs.items():  # record all kwargs
                print(f"\t{k}: {str(v)[:log_limit]}")
            for k, kv in signature(func).parameters.items():  # record accepted default kwargs
                if k not in kwargs.keys() and k not in arg_keys and "=" in str(kv):
                    print(f"\t{k}: {str(kv).split('=')[1].strip()[:log_limit]}")
            result = func(*args, **kwargs)
        else:  # log @properties
            print(f"{prefix}{func.fget.__name__}")
            result = func

        if result is not None:
            print(f"\tReturning: {str(result)[:log_limit]}")
        print(" --" * 27)
        return result

    return with_logging
