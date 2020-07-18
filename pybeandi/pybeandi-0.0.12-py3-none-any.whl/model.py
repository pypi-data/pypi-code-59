import abc
import fnmatch
import re
from dataclasses import dataclass
from typing import Dict, Callable, Any, Set, Union


class BeanRef(abc.ABC):
    @abc.abstractmethod
    def all_dependencies_satisfied(self, ready_beans_ids: Set[str],
                                   all_beans_ids: Set[str]) -> bool:
        pass

    def need_to_inject(self, all_beans_ids: Set[str]) -> bool:
        return True


class IdBeanRef(BeanRef):

    def __init__(self, bean_id: str, optional=False):
        self.optional = optional
        self.bean_id = bean_id

    def all_dependencies_satisfied(self, ready_beans_ids: Set[str],
                                   all_beans_ids: Set[str]) -> bool:
        if self.bean_id not in all_beans_ids:
            return self.optional
        else:
            return self.bean_id in ready_beans_ids

    def need_to_inject(self, all_beans_ids: Set[str]) -> bool:
        if self.optional:
            return self.bean_id in all_beans_ids
        else:
            return True


class WildcardBeanRef(BeanRef):

    def __init__(self, wildcard: str):
        self.wildcard = wildcard

    def all_dependencies_satisfied(self, ready_beans_ids: Set[str],
                                   all_beans_ids: Set[str]) -> bool:
        required_beans = set(fnmatch.filter(all_beans_ids, self.wildcard))
        return ready_beans_ids >= required_beans


class RegexBeanRef(BeanRef):

    def __init__(self, regex: str):
        self.regex = regex

    def all_dependencies_satisfied(self, ready_beans_ids: Set[str],
                                   all_beans_ids: Set[str]) -> bool:
        required_beans = {bean_id for bean_id in all_beans_ids
                          if re.match(self.regex, bean_id)}
        return ready_beans_ids >= required_beans


# Aliases
id_ref = IdBeanRef
wildcard_ref = WildcardBeanRef
regex_ref = RegexBeanRef

UserGeneralBeanRef = Union[str, BeanRef]


@dataclass
class BeanDef:
    bean_id: str
    factory_func: Callable[..., Any]
    dependencies: Dict[str, BeanRef]
    profile_func: Callable[[Set[str]], bool]
