import logging as log
import requests
from pprint import pprint
from subprocess import Popen, PIPE
from os import path
from fabric import Connection
import sys
import os
from pathlib import Path
# sys.path.append("bot/")
import fancybox as fb  # needed
from termcolor import colored, cprint


class Remote:
    def __init__(self, ip, user, password, port=22):
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password
        self.path = ""

    def connect(self):
        self.con = Connection(self.ip, port=self.port, user=self.user, connect_kwargs={
                              "password": self.password})
        if(self.con):
            print(colored("Remote VPS Conntectd",
                          'yellow', attrs=['reverse', 'bold']))

    def setPath(self, path):
        Path(os.path.dirname(path)).mkdir(parents=True, exist_ok=True)
        self.path = path

    def _exe(self, cmd):
        try:
            out = self.con.run(cmd)
            return out.stdout.strip()
        except Exception as e:
            print("Error")
            print(e)

    def exe(self, cmd, path=None):
        if(path):
            self.path = path
        print("")
        print(colored(self.path+"$", 'cyan', attrs=['reverse', 'bold']) +
              colored(" " + cmd, 'green', attrs=['reverse', 'bold']))
        with self.con.cd(self.path):
            self._exe(cmd)
