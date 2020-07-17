from subprocess import PIPE

import psutil


class Command(object):
    @staticmethod
    def exec(*command, stdout=True) -> psutil.Popen:
        if stdout is not None:
            if isinstance(stdout, bool):
                return psutil.Popen(list(command), stdout=PIPE)
            else:
                return psutil.Popen(list(command), stdout=stdout)
        else:
            return psutil.Popen(list(command))

