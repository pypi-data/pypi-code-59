import asyncio
import argparse

from watcher import Watcher


async def cli():
    parser = argparse.ArgumentParser(
        prog="wch",
        usage="%(prog)s [options] -- <command>",
        description="Runs the provided command on detected file changes.",
    )
    parser.add_argument(
        "-d",
        "--directory",
        action="append",
        default=[],
        help="Directory to watch. Default to current working directory.",
    )
    parser.add_argument(
        "-i", "--ignore", action="append", default=[], help="Directories to ignores.",
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

    watcher = Watcher(directories, args.ignore, command)
    await watcher.run()


def cli_sync():
    asyncio.run(cli())


if __name__ == "__main__":
    cli_sync()
