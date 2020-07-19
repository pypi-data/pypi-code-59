import asyncio
import argparse

from .change_detector import ChangeDetector
from .watcher import Watcher


async def cli():
    example = '\n'.join([
        'Examples:',
        '  wch -d src -d tests -- pytest',
        '  wch -i docs -- black .'
    ])

    parser = argparse.ArgumentParser(
        prog="wch",
        usage="%(prog)s [options] -- <command>",
        description="Runs the provided command on detected file changes.",
        epilog=example,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "-d",
        "--directory",
        action="append",
        default=[],
        help="Directory to watch. Defaults to current working directory.",
    )
    parser.add_argument(
        "-i", "--ignore", action="append", default=[], help="Directory to ignore.",
    )
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    directories = args.directory
    if not len(directories):
        directories = ["."]

    command = args.command
    if not command:
        parser.print_help()
        exit(1)
    if command[0] == "--":
        command = command[1:]
    command = " ".join(command)

    change_detector = ChangeDetector(directories, args.ignore)
    watcher = Watcher(change_detector, command)
    await watcher.run()


def cli_sync():
    asyncio.run(cli())
