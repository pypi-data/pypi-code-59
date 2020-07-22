"""Library for loading dynamic library files.

Python library for choosing and loading dynamic library
files compatible with the operating environment.
"""

import doctest
import sys
import os.path
import platform
from ctypes import cdll, create_string_buffer
from multiprocessing import Pool

class canaries():
    """
    Wrapper class for static methods.
    """

    @staticmethod
    def _xdll(path):
        """
        Load a library using the appropriate method.
        """
        system = platform.system()
        xdll = cdll
        if system == 'Windows':
            # pylint: disable=import-outside-toplevel
            from ctypes import windll as xdll # pragma: no cover
        return xdll.LoadLibrary(path)

    @staticmethod
    def _probe(lib):
        """
        Probe whether a library has a correctly implemented
        verification method.
        """
        # Build input and output buffers.
        treat = create_string_buffer(5)
        for (i, c) in enumerate('treat'):
            try:
                treat[i] = c
            except:
                treat[i] = ord(c)
        chirp = create_string_buffer(5)

        # Attempt to invoke the canary method.
        r = lib.canary(chirp, treat)

        # Decode results.
        chirp = chirp.raw
        if isinstance(chirp, bytes):
            chirp = chirp.decode()

        # Check that results are correct.
        return r == 0 and chirp == 'chirp'

    @staticmethod
    def _isolated(path):
        """
        Method to be used by isolated probe process.
        """
        return canaries._probe(canaries._xdll(path))

    @staticmethod
    def canary(system, path, probe=False):
        """
        Single-path wrapper method for convenience.
        """
        paths = {}
        paths[system] = [path]
        obj = canaries(paths, probe)
        return obj.lib if hasattr(obj, 'lib') else None

    @staticmethod
    def load(paths, probe=False):
        """
        Wrapper method for backwards compatibility.
        """
        obj = canaries(paths, probe)
        return obj.lib if hasattr(obj, 'lib') else None

    def __init__(self, paths, probe=False):
        """
        Attempt to load a library at one of the supplied
        paths based on the platform. Retains state in order
        to record all exceptions and incorrect outputs.
        """
        if not isinstance(paths, (str, list, dict)):
            raise TypeError(
                "input must be a string, list, or dictionary"
            )

        if isinstance(paths, dict) and\
           not all(isinstance(p, (str, list)) for p in paths.values()):
            raise TypeError(
                "path values in dictionary must be strings or lists of strings"
            )

        self.lib = None
        self.exceptions = []
        self.outputs = []

        system = platform.system()
        if isinstance(paths, str):
            self.lib = self._canary(system, paths, probe)

        elif isinstance(paths, list):
            for path in paths:
                self.lib = self._canary(system, path, probe)
                if self.lib is not None:
                    break

        elif isinstance(paths, dict):
            if system in paths:
                ps = paths[system]
                for path in [ps] if isinstance(ps, str) else ps:
                    self.lib = self._canary(system, path, probe)
                    if self.lib is not None:
                        break

    def _canary(self, system, path, probe=False):
        """
        Attempt to load a library file at the supplied path
        and verify that its exported functions work.
        """
        lib = None

        # Only attempt to load object files that exist.
        if os.path.exists(path):
            # Confirm that the library's exported functions work.
            try:
                # Invoke compatibility validation method
                # only if instructed to do so.
                if not probe:
                    lib = canaries._xdll(path)
                else:
                    # Perform probe in a subprocess to isolate
                    # segmentation faults and other runtime errors.
                    with Pool(1) as p:
                        task = p.imap(canaries._isolated, [path])
                        if task.next(5): # Process has five seconds to succeed.
                            lib = canaries._xdll(path)
            except:
                self.exceptions.append((
                    (system, path),
                    (
                        sys.exc_info()[0], sys.exc_info()[1],
                        sys.exc_info()[2].tb_lineno
                    )
                ))

        return lib

# Provide direct access to static methods.
canary = canaries.canary
load = canaries.load

if __name__ == "__main__":
    doctest.testmod() # pragma: no cover
