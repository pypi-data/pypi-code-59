import asyncio
from typing import Optional

from .change_detector import ChangeDetector


class Watcher:
    def __init__(self, change_detector: ChangeDetector, command: str):
        self._change_detector = change_detector
        self._command = command

    async def _create_process(self) -> asyncio.subprocess.Process:
        process = await asyncio.create_subprocess_shell(
            self._command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT,
        )
        return process

    @staticmethod
    async def _print_process(process: asyncio.subprocess.Process):
        if not process.stdout:
            return
        while True:
            line = (await process.stdout.readline()).decode().strip()
            if not line:
                break
            print(line)

    async def run(self):
        asyncio.create_task(self._change_detector.run())

        process: Optional[asyncio.subprocess.Process] = None
        while True:
            await self._change_detector.queue.get()
            if process:
                try:
                    process.kill()
                except ProcessLookupError:
                    # Process already finished.
                    pass
            print("\n\n\n")
            process = await self._create_process()
            asyncio.create_task(self._print_process(process))
