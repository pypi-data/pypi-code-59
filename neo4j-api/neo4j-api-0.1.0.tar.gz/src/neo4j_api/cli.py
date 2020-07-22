# Why does this file exist, and why not put this in `__main__`?
#
# You might be tempted to import things from `__main__` later,
# but that will cause problems: the code will get executed twice:
#
# - When you run `python -m neo4j_api` python will execute
#   `__main__.py` as a script. That means there won't be any
#   `neo4j_api.__main__` in `sys.modules`.
# - When you import `__main__` it will get executed again (as a module) because
#   there's no `neo4j_api.__main__` in `sys.modules`.

"""Module that contains the command line application."""

import argparse


def get_parser():
    """Return the CLI argument parser."""
    return argparse.ArgumentParser(prog="neo4j-api")


def main(args=None):
    """The main function, which is executed when you type `neo4j-api` or `python -m neo4j_api`."""
    parser = get_parser()
    opts = parser.parse_args(args=args)
    print(opts)
    return 0
