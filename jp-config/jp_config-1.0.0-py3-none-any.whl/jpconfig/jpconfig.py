import os
import sys
import json

class Config(object):
    def __init__(self, file=None):
        if file:
            Config.file_path = file
            self._load()
        else:
            sys.exit("file keyword argument required")

    def __add__(self, dict_):
        self._update(dict_)

    def __getattr__(self, name):
        return self.__dict__.get(name)

    def __repr__(self):
        return json.dumps(self.__dict__, sort_keys=2, indent=2)

    def __setattr__(self, name , value):
        self.__dict__[name] = value
        self._save()
   
    def __delitem__(self, name):
        self.__dict__.pop(name, None)
        self._save()

    def __delattr__(self, name):
        self.__dict__.pop(name, None)
        self._save()

    def keys(self):
        return list(self.__dict__.keys())

    def _update(self, value):
        self.__dict__.update(value)
        self._save()

    def _load(self):
        if os.path.exists(Config.file_path):
            with open(Config.file_path, 'r') as file:
                self.__dict__.update(json.loads(file.read()))
           
    def _save(self):
        with open(Config.file_path, 'w') as file:
            file.write(json.dumps(self.__dict__,sort_keys=True, indent=2))
