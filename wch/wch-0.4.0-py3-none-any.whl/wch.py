import asyncio
from typing import Iterable, List

import typer

from .change_detector import ChangeDetector
from .watcher import Watcher

app = typer.Typer(add_completion=False)


async def _main(directories: Iterable[str], ignores: Iterable[str], command: str):
    change_detector = ChangeDetector(directories, ignores)
    watcher = Watcher(change_detector, command)
    await watcher.run()


@app.command()
def main(
    directories: List[str] = typer.Option(["."], "--directory", "-d"),
    ignores: List[str] = typer.Option([], "--ignore", "-i"),
    command: str = typer.Argument(...),
):
    """
    Runs the provided command on detected file changes.

    example: wch -d src -d tests -i docs "black --check ."
    """
    try:
        asyncio.run(_main(directories, ignores, command))
    except KeyboardInterrupt:
        pass
