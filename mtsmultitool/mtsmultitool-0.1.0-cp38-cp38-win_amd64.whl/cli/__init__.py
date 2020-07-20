import sys
import argparse
import textwrap

from .. import __version__
from . import device_cli as device


def create_parser():
    desc = textwrap.dedent(f'''\
            ''')
    top_parser = argparse.ArgumentParser(
        prog='multitool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=desc)
    subparsers = top_parser.add_subparsers(metavar='CMD')

    device.add_parser(subparsers)

    return top_parser


def main():
    print(f'Multitool Utility - Version {__version__} - MultiTech Systems Inc.\n')
    parser = create_parser()
    if len(sys.argv) == 1:
        parser.print_help()
    else:
        args = parser.parse_args()
        try:
            args.func(args)
        except AttributeError:
            pass


if __name__ == '__main__':
    main()

