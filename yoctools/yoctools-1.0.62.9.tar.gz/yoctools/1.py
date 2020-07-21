# -*- coding:utf-8 -*-
#
# Copyright (C) 2019-2020 Alibaba Group Holding Limited


import os
import sys
import pickle
import platform
import subprocess
import site
import codecs

def home_path(path=''):
    return os.path.join(os.path.expanduser('~'), path)

shell = os.getenv('SHELL')
shell = os.path.basename(shell)

if shell == 'zsh':
    rc = home_path('.zshrc')

elif shell == 'bash':
    rc = home_path('.bashrc')

#with codecs.open(rc, 'r', 'UTF-8') as f:
#    contents = f.readlines()
#
#contents.insert(0, 'export PATH=' + toolchain_path + ':$PATH\n\n')
#
#with codecs.open(rc, 'w', 'UTF-8') as f:
#    contents = f.writelines(contents)
print("rc=", rc)
os.system("source " + "rc")
