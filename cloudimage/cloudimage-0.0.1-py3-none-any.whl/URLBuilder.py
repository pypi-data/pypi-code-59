from cloudimage.constants import DEFAULT_DOMAIN

from os.path import dirname, basename, isfile, join
import glob
import importlib

versions = glob.glob(join(dirname(__file__), "lib", "v*.py"))
__all_versions__ = [ basename(f)[:-3] for f in versions if isfile(f) and not f.endswith('__init__.py')]

def URLBuilder(token, domain=DEFAULT_DOMAIN, version="v7", salt="", active_salt="", SCRSET="w"):
        
    if str(version) in __all_versions__:
        version = str(version)
    else:
        version = "v7"

    module_version = importlib.import_module('cloudimage.lib.' + version)

    return module_version.URLHandler(token, domain, salt, active_salt, SCRSET)