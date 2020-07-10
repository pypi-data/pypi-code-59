import pkgutil
import sys
import fontTools
import importlib
import os
from pathlib import Path


def main():
    """Show this help"""
    path = fontTools.__path__
    descriptions = {}
    for pkg in sorted(
        mod.name
        for mod in pkgutil.walk_packages([fontTools.__path__[0]], prefix="fontTools.")
    ):
        try:
            imports = __import__(pkg, globals(), locals(), ["main"])
        except ImportError as e:
            continue
        try:
            description = imports.main.__doc__
            if description:
                pkg = pkg.replace("fontTools.", "").replace(".__main__", "")
                descriptions[pkg] = description
        except AttributeError as e:
            pass
    for pkg, description in descriptions.items():
        print("fonttools %-12s %s" % (pkg, description), file=sys.stderr)


if __name__ == "__main__":
    print("fonttools v%s\n" % fontTools.__version__, file=sys.stderr)
    main()
