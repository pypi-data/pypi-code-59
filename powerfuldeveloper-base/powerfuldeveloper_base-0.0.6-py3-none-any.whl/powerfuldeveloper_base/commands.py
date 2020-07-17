import subprocess

import psutil


class Command(object):
    @staticmethod
    def exec(*command,
             stdout=subprocess.PIPE,
             stderr=subprocess.DEVNULL,
             shell=False) -> psutil.Popen:
        kwargs = dict(
            shell=shell,
            stdout=stdout,
            stderr=stderr
        )

        return psutil.Popen(list(command), **kwargs)
