# -*- coding:utf-8 -*-
#
# Copyright (C) 2019-2020 Alibaba Group Holding Limited


import os
import sys
import pickle
import platform
import subprocess
import codecs

from .tools import *
from .log import logger
from .yoc import YoC
from .builder import *

import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)

try:
    import SCons.Script as SCons
except:
    import scons
    for path in scons.__path__:
        sys.path.append(path)
        import SCons.Script as SCons


SCons.AddOption('--verbose', dest='verbose', default=True,
                action='store_false',
                help='verbose command line output')


SCons.AddOption('--board', dest='board', default=None,
                action='store', nargs=1, type='string',
                help='board component name')

class Make(object):
    def __init__(self, elf=None, objcopy=None, objdump=None):
        try:
            with open('.sconsign.dblite', "rb") as f:
                pickle.load(f)
        except ValueError:
            os.remove('.sconsign.dblite')
        except:
            pass

        board_name = SCons.GetOption('board')

        product_install()
        print("===>>>aa")

        self.yoc = YoC()
        solution = self.yoc.getSolution(board_name)
        if solution:
            self.build_env = Builder(solution)
            self.build_env.env.AppendUnique(
                ELF_FILE=elf, OBJCOPY_FILE=objcopy, OBJDUMP_FILE=objdump)
            # self.build_env.env.AppendUnique(BOARD_NAME=board, CHIP_NAME=chip)
        else:
            self.build_env = None

    def which(self, cmd):
        gcc = subprocess.Popen('which ' + cmd, shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        lines = gcc.stdout.readlines()
        for text in lines:
            text = text.decode().strip()
            info = 'which: no ' + os.path.basename(cmd) + ' in'
            if not text.find(info) >= 0:
                return text
        return ''

    def update_env(self):
        toolchain_path = '$HOME/.thead'
        shell = os.getenv('SHELL')
        shell = os.path.basename(shell)

        if shell == 'zsh':
            rc = home_path('.zshrc')

        elif shell == 'bash':
            rc = home_path('.bashrc')

        with codecs.open(rc, 'r', 'UTF-8') as f:
            contents = f.readlines()

        contents.insert(0, 'export PATH=' + toolchain_path + ':$PATH\n\n')

        with codecs.open(rc, 'w', 'UTF-8') as f:
            contents = f.writelines(contents)
        os.system("source " + "rc")

    def product_install(self):
        path = self.which('product')
        if len(path) > 0:
            return

        link_path = ''
        if os.getuid() != 0:
            dir_path = home_path('.thead')
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            link_path = dir_path + '/product'
        else:
            link_path = '/usr/local/bin/product'

        try:
            os.unlink(link_path)
        except:
            pass

        architecture = platform.architecture()
        if architecture[0] == '64bit':
            product = '/usr/local/bin/product64'
        else:
            product = '/usr/local/bin/product32'
        
        if os.path.exists(product) == False:
            for dist_dir in site.getsitepackages():
                path = dist_dir + product
                if os.path.exists(path):
                    print("path==>" + path)
                    product = path
                    break;
        
        try:
            os.symlink(product, link_path)
            if os.getuid() != 0:
                update_env()
        except:
            pass

    def library_yaml(self):
        package_file = self.build_env.env.GetBuildPath('package.yaml')
        conf = yaml_load(package_file)
        if conf and 'name' in conf:
            component = self.yoc.components.get(conf['name'])
            self.build_env.build_component(component)
            component.export()

    def build_component(self, component):
        new_file = False
        file_name = os.path.join(component.path, 'SConscript')
        if not os.path.exists(file_name):
            file_name = genSConcript(component.path)
            new_file = True
        if os.path.isfile(file_name):
            SCons.SConscript(file_name, exports={"env": self.build_env.env.Clone(
            )}, variant_dir='out/' + component.name, duplicate=0)
            if new_file:
                os.remove(file_name)

    def build_components(self, components=None):
        if components != None:
            for c in components:
                component = self.yoc.components.get(c)
                if component:
                    self.build_component(component)
        else:
            for component in self.build_env.solution.components:
                self.build_component(component)

    def build_image(self, elf=None, objcopy=None, objdump=None, product=None):
        self.build_env.build_image(elf, objcopy, objdump, product)
