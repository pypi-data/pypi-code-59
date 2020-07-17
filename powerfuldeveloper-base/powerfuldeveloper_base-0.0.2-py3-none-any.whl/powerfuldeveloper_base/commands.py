from subprocess import PIPE

import psutil


class Command(object):
    @staticmethod
    def exec(*command) -> psutil.Popen:
        return psutil.Popen(list(command), stdout=PIPE)
