from dataclasses import dataclass
from typing import Set, Callable, Dict, Type

from pybeandi.model import UserGeneralBeanRef, id_ref, BeanRef
from pybeandi.util import camel_case_to_snake_case


@dataclass
class BeanMeta:
    bean_id: str
    profile_func: Callable[[Set[str]], bool]
    cls: Type
    depends_on: Dict[str, BeanRef]


def bean(bean_id: str = None,
         profiles: Set[str] = None,
         profile_func: Callable[[Set[str]], bool] = lambda profs: True,
         **depends_on: Dict[str, UserGeneralBeanRef]):
    def wrapper(cls):
        nonlocal bean_id, depends_on, profile_func
        depends_on = {
            arg_name: (id_ref(arg_ref) if type(arg_ref) is str else arg_ref)
            for (arg_name, arg_ref) in depends_on.items()}
        bean_id = bean_id \
            if bean_id is not None \
            else camel_case_to_snake_case(cls.__name__)
        profile_func = profile_func \
            if profiles is None \
            else lambda profs: profs >= profiles

        cls._bean_meta = BeanMeta(bean_id, profile_func, cls, depends_on)

        return cls

    return wrapper


@dataclass
class AfterInitMeta:
    depends_on: Dict[str, BeanRef]


def after_init(**depends_on: Dict[str, UserGeneralBeanRef]):
    def wrapper(func):
        nonlocal depends_on
        depends_on = {
            arg_name: (id_ref(arg_ref) if type(arg_ref) is str else arg_ref)
            for (arg_name, arg_ref) in depends_on.items()}

        func._bean_meta = AfterInitMeta(depends_on)

        return func

    return wrapper
