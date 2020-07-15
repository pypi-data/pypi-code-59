import sys as _sys, platform as _pl

class NumberError(TypeError):
    pass

class LessThanZeroError(NumberError):
    pass

class MoreThanZeroError(NumberError):
    pass

class EqualToZeroError(NumberError):
    pass

class NotLessThanZeroError(NumberError):
    pass

class NotMoreThanZeroError(NumberError):
    pass

class NotEqualToZeroError(NumberError):
    pass

class ArgError(TypeError):
    pass

class SystemError(TypeError): # Do NOT use "from PyErr import SystemError"!
    pass

class VersionError(SystemError):
    pass

def checkOS(name, version, err=True):
    os = _pl.system()
    os_version = tuple(_pl.platform().split('-')[2].split('.'))[:len(version)]
    if name != os:
        if err:
            raise SystemError("Your system is not %r, but%r" % (name, os))
        else:
            return False
    if version > os_version:
        if err:
            raise VersionError("Your system version is not right(at least %s, but %s)" % ('.'.join(list(version)), '.'.join(ist(os_version)))) 
        else:
            return False
    if not err:
        return True

def checkpyversion(version, err=True):
    ver = _sys.version_info[:3]
    if ver < version:
        if err:
            raise VersionError("Your Python version is not right(at least %s, but %s)" % ('.'.join(list(version)), '.'.join(ist(ver))))
        else:
            return False
    if not err:
        return True
