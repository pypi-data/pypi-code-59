import functools,inspect
from flask import request

def rename_func(name):
    def decorator(func):
        func.__name__=name
        @functools.wraps(func)
        def new_func(*args,**kwargs):
            return func(*args,**kwargs)
        return new_func
    return decorator

def get_arg_dict(func):
    sign = inspect.signature(func)
    keys = list(sign.parameters.keys())
    dic = dict()
    for key in keys:
        value = sign.parameters.get(key).default
        dic[key] = value
    return dic


def parse_from(*refers):
    def decorator(f):
        arg_dict=get_arg_dict(f)
        fargs=list(arg_dict.keys())
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            dic = {}
            data_resource=[*refers,kwargs]
            for ref in data_resource:
                d = ref() if callable(ref) else dict(ref)
                d = d or {}
                if d: dic.update(d)
            params = {}
            for ag in fargs:
                val = dic.get(ag, None)
                if val is None:
                    for k, v in dic.items():
                        if k.replace('-', '_') == ag:
                            val = v
                if val is None:
                    val=arg_dict.get(ag,None)
                params[ag]=val
            params.update(kwargs)
            return f(*args, **params)

        return wrapper

    return decorator


def get_files(): return dict(request.files)


def get_form(): return request.form


def get_json(): return request.json


def get_cookies(): return request.cookies


def get_url_args(): return request.args


# parse_json is a decorator
parse_json_and_form = parse_from(get_json, get_form)
parse_json = parse_from(get_json)
parse_form = parse_from(get_form)
parse_files = parse_from(get_files)
parse_cookies = parse_from(get_cookies)
parse_args = parse_from(get_url_args)
parse_all = parse_from(get_cookies, get_form, get_json, get_url_args)


