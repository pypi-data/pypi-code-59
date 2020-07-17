#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# This file is part of SysPass Client
#
# Copyright (C) 2020  DigDeo SAS
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


import os
from colorama import init, Fore, Style
import syspassclient

from yaml import load

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
init(autoreset=True)

# Inspired by: http://zetcode.com/python/yaml/
# Inspired by: https://gitlab.com/Tuuux/galaxie-little-alice/raw/master/GLXLittleAlice/Config.py
import threading

lock = threading.Lock()


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(syspassclient.SyspassApi, metaclass=Singleton):
    def __init__(self):
        syspassclient.SyspassApi.__init__(self)

        # Load config file
        self.__rw = None
        self.__data = None
        self.__config_file = None
        self.__verify_ssl = None
        self.__authToken = None
        self.__tokenPass = None


        self.rw = True
        self.verify_ssl = True

        self.read_config()
        self.read_api()

    @property
    def config_directory(self):
        if 'DD_SYSPASS_CLIENT_CONFIG_DIR' in os.environ:
            return os.path.realpath(os.environ['DD_SYSPASS_CLIENT_CONFIG_DIR'])
        else:
            return os.path.realpath(
                os.path.abspath(
                    os.path.join(
                        os.path.join(
                            os.environ['HOME'],
                            '.config'),
                        'digdeo-syspass-client'
                    )
                )
            )

    @property
    def config_file(self):
        return self.__config_file

    @config_file.setter
    def config_file(self, value=None):
        if self.config_file != value:
            self.__config_file = value

    @property
    def authToken(self):
        if 'DD_SYSPASS_CLIENT_AUTH_TOKEN' in os.environ and os.environ['DD_SYSPASS_CLIENT_AUTH_TOKEN'] is not None:
            return os.environ['DD_SYSPASS_CLIENT_AUTH_TOKEN']

        return self.__authToken

    @authToken.setter
    def authToken(self, value=None):
        if value is None:
            raise ValueError('"authToken" property value can not be None')
        if type(value) != str:
            raise TypeError('"authToken" property value must be a str type')
        if self.__authToken != value:
            self.__authToken = value

    @property
    def tokenPass(self):
        if 'DD_SYSPASS_CLIENT_TOKEN_PASS' in os.environ and os.environ['DD_SYSPASS_CLIENT_TOKEN_PASS'] is not None:
            return os.environ['DD_SYSPASS_CLIENT_TOKEN_PASS']
        return self.__tokenPass

    @tokenPass.setter
    def tokenPass(self, value=None):
        if value is None:
            raise ValueError('"tokenPass" property value can not be None')
        if type(value) != str:
            raise TypeError('"tokenPass" property value must be a str type')
        if self.__tokenPass != value:
            self.__tokenPass = value

    @property
    def verify_ssl(self):
        """
        Verify the SSL Certificate

        :return: True if SSL Certificate have to be verify
        :rtype: bool
        """
        if 'DD_SYSPASS_CLIENT_VERIFY_SSL' in os.environ and os.environ['DD_SYSPASS_CLIENT_VERIFY_SSL'] is not None:
            return bool(os.environ['DD_SYSPASS_CLIENT_VERIFY_SSL'])

        return bool(self.__verify_ssl)

    @verify_ssl.setter
    def verify_ssl(self, value=None):
        if value is None:
            value = True
        if type(value) != bool:
            raise TypeError("'verify_sll' value must be a bool type or None")
        if self.verify_ssl != value:
            self.__verify_ssl = value

    @property
    def data(self):
        """
        Return the config file as Python dictionary structure

        :return: Config as a big dictionary
        :rtype: dict
        """
        return self.__data

    @data.setter
    def data(self, parameters):
        """
        set en data and raise in case of error

        :param parameters: something it like a dictionary key
        :type parameters: dict
        :raise TypeError: 'parameters' is not a dict type
        """
        if self.data != parameters:
            self.__data = parameters

    def read_config(self, config_file=None):
        """
        Read the configuration file

        :param config_file: the file it store the dd_ansible_syspass
        :type config_file: str or None for default
        """
        if config_file is None:
            config_file = self.get_config_file()

        self.data = {}
        with open(config_file) as f:
            config = load(f, Loader=Loader)
            f.close()

            if 'syspassclient' not in config:
                raise AttributeError('{0} do not contain syspassclient attribute'.format(config_file))

            if config["syspassclient"] is None:
                raise ImportError('nothing to import ...')

            if "api_url" in config["syspassclient"]:
                self.api_url = config["syspassclient"]["api_url"]

            if "api_version" in config["syspassclient"]:
                self.api_version = config["syspassclient"]["api_version"]

            if "authToken" in config["syspassclient"]:
                self.authToken = config["syspassclient"]["authToken"]

            if "tokenPass" in config["syspassclient"]:
                self.tokenPass = config["syspassclient"]["tokenPass"]

            if "verify_ssl" in config["syspassclient"]:
                self.verify_ssl = config["syspassclient"]["verify_ssl"]

            if "debug" in config["syspassclient"]:
                self.debug = config["syspassclient"]["debug"]

            if "debug_level" in config["syspassclient"]:
                self.debug_level = config["syspassclient"]["debug_level"]

            if "verbose" in config["syspassclient"]:
                self.verbose = config["syspassclient"]["verbose"]

            if "verbose_level" in config["syspassclient"]:
                self.verbose_level = config["syspassclient"]["verbose_level"]

        # Display
        if self.debug and self.debug_level > 1:
            print(Fore.YELLOW + Style.BRIGHT + "{0}: ".format(self.__class__.__name__.upper()), end='')
            print(Fore.WHITE + Style.BRIGHT + "{0} ".format("Load Config File"))

            print(Fore.WHITE + Style.BRIGHT + "File: ", end='')
            print(Fore.GREEN + Style.BRIGHT + "{0}".format(config_file))

            if self.debug and self.debug_level > 2:
                # API_URL
                if 'DD_SYSPASS_CLIENT_API_URL' in os.environ and os.environ['DD_SYSPASS_CLIENT_API_URL'] is not None:
                    print(Fore.CYAN + Style.BRIGHT + "< " + Fore.WHITE + "DD_SYSPASS_CLIENT_API_URL: ", end='')
                    print(Fore.GREEN + Style.BRIGHT + "{0}".format(os.environ['DD_SYSPASS_CLIENT_API_URL']))
                else:
                    print(Fore.CYAN + Style.BRIGHT + "< " + Fore.WHITE + "api_url: ", end='')
                    print(Fore.GREEN + Style.BRIGHT + "{0}".format(self.api_url))

                # API_VERSION
                if 'DD_SYSPASS_CLIENT_API_VERSION' in os.environ and os.environ['DD_SYSPASS_CLIENT_API_VERSION'] is not None:
                    print(Fore.CYAN + Style.BRIGHT + "< " + Fore.WHITE + "DD_SYSPASS_CLIENT_API_VERSION: ", end='')
                    print(Fore.GREEN + Style.BRIGHT + "{0}".format(os.environ['DD_SYSPASS_CLIENT_API_VERSION']))
                else:
                    print(Fore.CYAN + Style.BRIGHT + "< " + Fore.WHITE + "api_version: ", end='')
                    print(Fore.GREEN + Style.BRIGHT + "{0}".format(self.api_version))

                # AUTH_TOKEN
                if 'DD_SYSPASS_CLIENT_AUTH_TOKEN' in os.environ and os.environ['DD_SYSPASS_CLIENT_AUTH_TOKEN'] is not None:
                    print(Fore.CYAN + Style.BRIGHT + "< " + Fore.WHITE + "DD_SYSPASS_CLIENT_AUTH_TOKEN: ", end='')
                    print(Fore.GREEN + Style.BRIGHT + "{0}".format(os.environ['DD_SYSPASS_CLIENT_AUTH_TOKEN']))
                elif self.authToken is not None:
                    print(Fore.CYAN + Style.BRIGHT + "< " + Fore.WHITE + "authToken: ", end='')
                    print(Fore.GREEN + Style.BRIGHT + "{0}".format(self.authToken))

                # TOKEN_PASS
                if 'DD_SYSPASS_CLIENT_TOKEN_PASS' in os.environ and os.environ['DD_SYSPASS_CLIENT_TOKEN_PASS'] is not None:
                    print(Fore.CYAN + Style.BRIGHT + "< " + Fore.WHITE + "DD_SYSPASS_CLIENT_TOKEN_PASS: ", end='')
                    print(Fore.GREEN + Style.BRIGHT + "{0}".format(os.environ['DD_SYSPASS_CLIENT_TOKEN_PASS']))
                elif self.tokenPass is not None:
                    print(Fore.CYAN + Style.BRIGHT + "< " + Fore.WHITE + "tokenPass: ", end='')
                    print(Fore.GREEN + Style.BRIGHT + "{0}".format( self.tokenPass))

                # VERIFY_SSL
                if 'DD_SYSPASS_CLIENT_VERIFY_SSL' in os.environ and os.environ['DD_SYSPASS_CLIENT_VERIFY_SSL'] is not None:
                    print(Fore.CYAN + Style.BRIGHT + "< " + Fore.WHITE + "DD_SYSPASS_CLIENT_VERIFY_SSL: ", end='')
                    print(Fore.GREEN + Style.BRIGHT + "{0}".format(os.environ['DD_SYSPASS_CLIENT_VERIFY_SSL']))
                else:
                    print(Fore.CYAN + Style.BRIGHT + "< " + Fore.WHITE + "verify_ssl: ", end='')
                    print(Fore.GREEN + Style.BRIGHT + "{0}".format(self.verify_ssl))

                # DEBUG
                if 'DD_SYSPASS_CLIENT_DEBUG' in os.environ and os.environ['DD_SYSPASS_CLIENT_DEBUG'] is not None:
                    print(Fore.CYAN + Style.BRIGHT + "< " + Fore.WHITE + "DD_SYSPASS_CLIENT_DEBUG: ", end='')
                    print(Fore.GREEN + Style.BRIGHT + "{0}".format(os.environ['DD_SYSPASS_CLIENT_DEBUG']))
                else:
                    print(Fore.CYAN + Style.BRIGHT + "< " + Fore.WHITE + "debug: ", end='')
                    print(Fore.GREEN + Style.BRIGHT + "{0}".format(self.debug))

                # DEBUG_LEVEL
                if 'DD_SYSPASS_CLIENT_DEBUG_LEVEL' in os.environ and os.environ['DD_SYSPASS_CLIENT_DEBUG_LEVEL'] is not None:
                    print(Fore.CYAN + Style.BRIGHT + "< " + Fore.WHITE + "DD_SYSPASS_CLIENT_DEBUG_LEVEL: ", end='')
                    print(Fore.GREEN + Style.BRIGHT + "{0}".format(os.environ['DD_SYSPASS_CLIENT_DEBUG_LEVEL']))
                else:
                    print(Fore.CYAN + Style.BRIGHT + "< " + Fore.WHITE + "debug_level: ", end='')
                    print(Fore.GREEN + Style.BRIGHT + "{0}".format(self.debug_level))

                # VERBOSE
                if 'DD_SYSPASS_CLIENT_VERBOSE' in os.environ and os.environ['DD_SYSPASS_CLIENT_VERBOSE'] is not None:
                    print(Fore.CYAN + Style.BRIGHT + "< " + Fore.WHITE + "DD_SYSPASS_CLIENT_VERBOSE: ", end='')
                    print(Fore.GREEN + Style.BRIGHT + "{0}".format(os.environ['DD_SYSPASS_CLIENT_VERBOSE']))
                else:
                    print(Fore.CYAN + Style.BRIGHT + "< " + Fore.WHITE + "verbose: ", end='')
                    print(Fore.GREEN + Style.BRIGHT + "{0}".format(self.verbose))

                # VERBOSE_LEVEL
                if 'DD_SYSPASS_CLIENT_VERBOSE_LEVEL' in os.environ and os.environ['DD_SYSPASS_CLIENT_VERBOSE_LEVEL'] is not None:
                    print(Fore.CYAN + Style.BRIGHT + "< " + Fore.WHITE + "DD_SYSPASS_CLIENT_VERBOSE_LEVEL: ", end='')
                    print(Fore.GREEN + Style.BRIGHT + "{0}".format(os.environ['DD_SYSPASS_CLIENT_VERBOSE_LEVEL']))
                else:
                    print(Fore.CYAN + Style.BRIGHT + "< " + Fore.WHITE + "verbose_level: ", end='')
                    print(Fore.GREEN + Style.BRIGHT + "{0}".format(self.verbose_level))

            # API File loading
            print(Fore.YELLOW + Style.BRIGHT + "{0}: ".format(self.__class__.__name__.upper()), end='')
            print(Fore.WHITE + Style.BRIGHT + "{0} ".format("Load API File"))

            print(Fore.WHITE + Style.BRIGHT + "File: ", end='')
            print(Fore.GREEN + Style.BRIGHT + "{0}".format(self.api_file))

    @staticmethod
    def get_empty_config_dict():
        return {
            'syspassclient': {
                'api_url': None,
                'api_version': '3.1',
                'authToken': None,
                'tokenPass': None,
                'debug': True,
                'debug_level': 3,
                'verbose': False,
                'verbose_level': 0
            }
        }

    def get_config_file(self):
        return os.path.join(
            self.config_directory,
            "config.yml",
        )
