from builtins import exec as _builtin_exec, eval as _builtin_eval

class Scope:
    
    def __init__(self, settings={}):
        if not isinstance(settings, dict): raise TypeError("Arg 'settings' must be a dict object")
        self.settings = settings
        if not settings:
            self.exec('from builtins import *')
    
    def getitem(self, key, none_default=None):
        return self.settings.get(key, none_default)
    
    def setitems(self, settings):
        self.settings.update(settings)
    
    def getitems(self, *keys, none_default):
        result = []
        for key in keys:
            result.append(self.getitem(key, none_default))
        return result
    
    def setitem(self, key, value):
        self.setitems({key: value})
    
    def exec(self, s):
        _builtin_exec(s, self.settings)
    
    def eval(self, s):
        return _builtin_eval(s, self.settings)
    
    def __bool__(self):
        return bool(self.settings)
    
    def __dict__(self):
        return self.settings
    
    def __list__(self):
        return(self.settings.keys)

    def __tuple__(self):
        return tuple(list(self))
    
    def __repr__(self):
        return '<Scope object with value %s>' % self.settings
    
    def __len__(self):
        return len(list(self))