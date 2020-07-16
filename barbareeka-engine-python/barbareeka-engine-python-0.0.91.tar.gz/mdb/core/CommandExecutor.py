import os


class CommandExecutor(object):
    command = str()

    def exec_as_list(self, command):
        command = os.popen(command).read()
        return [command][0].split("\n")
