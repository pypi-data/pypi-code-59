# Copyright (C) 2020  GRNET S.A.
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys

from cliff.app import App
from cliff.commandmanager import CommandManager

from pyjamaas import parse
from pyjamaas.config import config

README = 'https://github.com/grnet/pyjamaas/blob/master/README.md'


class PyjamaasApp(App):
    def __init__(self):
        super(PyjamaasApp, self).__init__(
            description='pyjamaas: Python MaaS and Juju Toolkit',
            version='0.2',
            command_manager=CommandManager('pyjamaas.entrypoints'),
            deferred_help=True
        )

    def build_option_parser(self, description, version, argparse_kwargs=None):
        parser = super().build_option_parser(
            description, version, argparse_kwargs=argparse_kwargs)

        parser.add_argument(
            '--config', type=parse.yaml_argument,
            help='pyjamaas configuration')

        parser.epilog = f'Refer to {README} for configuration instructions'
        return parser

    def initialize_app(self, argv):
        super().initialize_app(argv)
        config.load(self.options.config)


def main(argv=sys.argv[1:]):
    m = PyjamaasApp()
    return m.run(argv)


if __name__ == '__main__':
    sys.exit(main())
