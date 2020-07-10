import warnings

import requests


def raise_connection_error(*args, **kwargs):
    requests.get('https://jibber.ish', timeout=0.01, *args, **kwargs)


def decorate_methods(decorator, *args, **kwargs):
    def decorate(cls):
        for attr in cls.__dict__:
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr), *args, **kwargs))
        return cls

    return decorate


def catch_errors_raise_warnings(f, ignored_errors):  # pragma: no cover
    def wrapper(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except ignored_errors:
            warnings.warn('Unreachable API from {}'.format(f.__name__), Warning)
            assert True

    return wrapper


def check_not_all_raise_errors(fs, ignored_errors):  # pragma: no cover
    def wrapper(*args, **kwargs):
        success = False
        ret = []
        for f in fs:
            try:
                ret.append(f(*args, **kwargs))
                success = True
            except ignored_errors:
                continue

        if not success:
            raise ConnectionError('All API calls to {} are unreachable'.format(fs[0].__name__))

        return ret

    return wrapper
