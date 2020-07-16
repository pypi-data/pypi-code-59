#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import python libs
import os
import shutil
import sys
from setuptools import setup
from distutils.command import install_scripts, install, build

NAME = "idem_salt"
DESC = "Run idem exec and state modules from salt"

# Version info -- read without importing
_locals = {}
VERSION = 2.0
SETUP_DIRNAME = os.path.dirname(__file__)
if not SETUP_DIRNAME:
    SETUP_DIRNAME = os.getcwd()

with open("README.rst", encoding="utf-8") as f:
    LONG_DESC = f.read()


class Build(build.build):
    def run(self):
        self.run_command("install_scripts")


class Install(install.install):
    def run(self):
        self.run_command("install_scripts")


class InstallScripts(install_scripts.install_scripts):
    SRC_MODULES = os.path.join(SETUP_DIRNAME, "_modules")
    SRC_STATES = os.path.join(SETUP_DIRNAME, "_states")
    _managed = None

    def initialize_options(self):
        self.install_dir = "/srv/salt"
        self.force = 0
        self.build_dir = None
        self.skip_build = None

    @staticmethod
    def check_elevate(path):
        if os.getuid() and os.stat(path).st_uid == 0:
            sys.exit(f"Insufficent permissions to write files to {path}")

    # The directory is owned by root and we are not root, elevate
    @property
    def dest_states(self):
        path = os.path.join(self.install_dir, "_states")
        self.check_elevate(path)
        os.makedirs(path, exist_ok=True)
        return path

    @property
    def dest_modules(self):
        path = os.path.join(self.install_dir, "_modules")
        self.check_elevate(path)
        os.makedirs(path, exist_ok=True)
        return path

    @property
    def managed(self):
        """
        Find the packages at the destination that are managed by idem-salt
        """
        if self._managed is None:
            ret = set()
            for loc in (self.dest_states, self.dest_modules):
                os.makedirs(loc, exist_ok=True)
                for managed in os.listdir(loc):
                    path = os.path.abspath(os.path.join(loc, managed))
                    if not os.path.isdir(path):
                        with open(path) as fh:
                            header = fh.readline().strip()
                            if header == "# Managed by idem-salt":
                                ret.add(path)
            self._managed = ret
        return self._managed

    def get_inputs(self):
        ret = []
        for src_dir in (self.SRC_STATES, self.SRC_MODULES):
            for s in os.listdir(src_dir):
                if not os.path.isdir(s):
                    src = os.path.join(src_dir, s).lstrip(SETUP_DIRNAME)
                    ret.append(src)
        return ret

    def get_outputs(self):
        ret = []
        for src_dir, dest_dir in zip(
            (self.SRC_STATES, self.SRC_MODULES), (self.dest_states, self.dest_modules)
        ):
            for s in os.listdir(src_dir):
                if not os.path.isdir(s):
                    dest = os.path.join(dest_dir, s)
                    if os.path.exists(dest) and dest not in self.managed:
                        print(
                            f"Ignoring module that isn't managed by idem-salt: {dest}"
                        )
                    else:
                        ret.append(dest.lstrip(self.install_dir))
        return ret

    def run(self):
        for src in self.get_inputs():
            if src in self.get_outputs():
                full_src = os.path.join(SETUP_DIRNAME, src)
                full_dest = os.path.join(self.install_dir, src)
                print(f"Copying {full_src} to {full_dest}")
                shutil.copy(full_src, full_dest)


setup(
    name="idem-salt",
    author="Tyler Johnson",
    author_email="tjohnson@saltstack.com",
    url="https://gitlab.com/Akm0d/idem-salt",
    version=VERSION,
    description=DESC,
    long_description=LONG_DESC,
    long_description_content_type="text/x-rst",
    python_requires=">=3.6",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 5 - Production/Stable",
    ],
    cmdclass={"install_scripts": InstallScripts, "install": Install, "build": Build},
)
