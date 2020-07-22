from collections import UserDict
from functools import wraps
from pathlib import Path

import yaml


def memoized_singleton(cls, keyfunc=None):
    memoized_instances = {}
    
    @wraps(cls)
    def factory(*args, **kwargs):
        key = keyfunc(*args, **kwargs) if keyfunc else cls.keyfunc(*args, **kwargs)
        if key in memoized_instances:
            return memoized_instances[key]

        instance = cls(*args, **kwargs)
        memoized_instances[key] = instance
        return instance

    return factory


@memoized_singleton
class DictPersistYAML(UserDict):
    
    @staticmethod
    def keyfunc(filename):
        return Path(filename).expanduser().absolute()

    def __init__(self, filename, *args, **kwargs):
        self._path = self.keyfunc(filename)
        super().__init__(*args, **kwargs)
        self._load()

    def _load(self):
        if self._path.is_file() and self._path.exists():
            with self._path.open() as f:
                yaml_dict = yaml.safe_load(f)
                if yaml_dict:
                    self.update(yaml_dict)

    def _dump(self):
        with self._path.open('w') as f:
            yaml.safe_dump(self.data, f, default_flow_style=False)
    
    def __getitem__(self, key):
        return super().__getitem__(key)

    def __setitem__(self, key, val):
        super().__setitem__(key, val)
        self._dump()

    def __repr__(self):
        return f'{type(self).__name__}({repr(self.data)})'

    def update(self, *args, **kwargs):
        dict_ = dict(*args, **kwargs)
        if dict_:
            for k, v in dict_.items():
                self[k] = v
            self._dump()
