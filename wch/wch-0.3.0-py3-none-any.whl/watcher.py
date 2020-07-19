import asyncio


class Watcher:
    def __init__(self, change_detector, command):
        self._change_detector = change_detector
        self._command = command
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
            line = (await process.stdout.readline()).decode().strip()
            if not line:
                break
            print(line)

    async def run(self):
        asyncio.create_task(self._change_detector.run())

        while True:
            await self._change_detector.queue.get()
            if self._process:
                try:
                    self._process.kill()
                except ProcessLookupError:
                    # Process already finished.
                    pass
            print("\n\n\n")
            await self._create_process()
            asyncio.create_task(self._print_process(self._process))
