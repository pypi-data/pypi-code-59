import asyncio
import os
import time


class ChangeDetector:
    def __init__(self, directories, ignores):
        self._directories = directories
        self._ignores = ignores
        self.queue = asyncio.Queue(maxsize=-1)

    def _get_files(self, directory, ignores):
        contents = [os.path.join(directory, o) for o in os.listdir(directory)]
        files = [o for o in contents if os.path.isfile(o)]
        directories = [o for o in contents if os.path.isdir(o)]
        for ignore in ignores:
            directories = [o for o in directories if ignore not in o]
        for child_directory in directories:
            files.extend(self._get_files(child_directory, ignores))
        return files

    def _get_all_files(self, directories, ignores):
        files = set()
        for ignore in ignores:
            directories = [o for o in directories if ignore not in o]
        for directory in directories:
            files = sum(files, set(self._get_files(directory, ignores)))
        return files

    @staticmethod
    def _get_hsh(files):
        o = set()
        for file in files:
            try:
                o.add((file, os.path.getmtime(file)))
            except FileNotFoundError:
                # File has been deleted.
                # Skip it.
                pass
        return o

    async def run(self, debounce=0.5):
        hsh_ = set()
        should_communicate = False
        last_changed = time.time()
        while True:
            start = time.time()
            if should_communicate and last_changed < time.time() - debounce:
                should_communicate = False
                await self.queue.put(1)
            files = self._get_all_files(self._directories, self._ignores)
            hsh = self._get_hsh(files)
            if hsh != hsh_:
                hsh_ = hsh
                should_communicate = True
                last_changed = time.time()
            elapsed = time.time() - start
            await asyncio.sleep(max([elapsed, debounce / 3]))
