import requests
from pprint import pprint
from os import path
import sys
import os
from subprocess import Popen, PIPE
from pathlib import Path
# sys.path.append("bot/")
import fancybox as fb  # needed
from termcolor import colored, cprint

from .git import Git


class Local:
    def __init__(self):
        self.path = ""
        self.git = Git(self)

    def setPath(self, path):
        self.path = path
        os.chdir(path)

    def exe(self, cmd):
        cmds = cmd.split()
        print("")
        print(colored(self.path+"$", 'cyan', attrs=['reverse', 'bold']) +
              colored(" "+cmd, 'green', attrs=['reverse', 'bold']))
        out, error = Popen(cmds, stdout=PIPE, stderr=PIPE).communicate()
        print(out.decode("utf-8"), end="")
        print(error.decode("utf-8"))
