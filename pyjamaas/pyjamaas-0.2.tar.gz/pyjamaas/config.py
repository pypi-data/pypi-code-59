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

import os

from pyjamaas.log import log


class Config:
    """
    Manage configuration
    """
    _entries = dict(
        maas_api_key=os.getenv('MAAS_API_KEY', ''),
        maas_api_url=os.getenv('MAAS_API_URL', ''),
    )

    def __getattribute__(self, name):
        """overrides so that config.OPTION returns config.entries['OPTION']"""
        if name.replace('-', '_') in super().__getattribute__('_entries'):
            return super().__getattribute__('_entries')[name.replace('-', '_')]

        return super().__getattribute__(name)

    @classmethod
    def load(cls, config):
        """loads and overrides configuration from @config dict"""
        try:
            for key, value in (config or {}).items():
                key = key.replace('-', '_')
                if key in cls._entries:
                    cls._entries[key] = value
                else:
                    raise KeyError(key)

        except KeyError as e:
            log.exception('Invalid config: {}'.format(e))


config = Config()
