from importlib import import_module


def create(class_module_name: str, class_name: str, arguments: dict = {}):
    return getattr(import_module(class_module_name), class_name)(**arguments)
