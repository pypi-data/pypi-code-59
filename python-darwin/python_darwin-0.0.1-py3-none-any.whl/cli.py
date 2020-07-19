import sys
import argparse
import json

from darwin import __version__, Darwin


def _get_parser(add_help=True):
    parser = argparse.ArgumentParser(
        add_help=add_help, description="Darwin Command Line Interface"
    )
    parser.add_argument("--version", help="Display the version.", action="store_true")
    parser.add_argument("query", type=str, help="the search query")
    return parser



def main():
    if "--version" in sys.argv:
        print(__version__)
        sys.exit(0)

    parser = _get_parser(add_help=False)

    if "--help" in sys.argv or "-h" in sys.argv:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    # Initialize a new Darwin client
    client = Darwin()

    # Perform search query
    try:
        result = client.query(args.query)
    except DarwinError as e:
        print(e)
        exit(1)

    print(json.dumps(result, indent=4))
    sys.exit(0)
