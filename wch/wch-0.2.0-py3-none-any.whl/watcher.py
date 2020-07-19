import asyncio

from change_detector import ChangeDetector


class Watcher:
    def __init__(self, directories, ignores, command):
        self._directories = directories
        self._ignores = ignores
        self._command = command

        self._change_q = asyncio.Queue(maxsize=-1)
        self._process = None

    async def _create_process(self):
        process = await asyncio.create_subprocess_shell(
            self._command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT,
        )
        self._process = process

    @staticmethod
    async def _print_process(process):
        while True:
            line = (await process.stdout.readline()).decode()
            if not line:
                break
            print(line)

    async def run(self):
        change_detector = ChangeDetector(self._change_q)
        asyncio.create_task(change_detector.run(self._directories, self._ignores))

        while True:
            await self._change_q.get()
            if self._process:
                try:
                    self._process.terminate()
                except ProcessLookupError:
                    # Process already finished.
                    pass
            print("\n\n")
            await self._create_process()
            asyncio.create_task(self._print_process(self._process))
