#!/usr/bin/python
#
# Copyright 2018-2020 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from datetime import timedelta

from marshmallow import fields

from polyaxon.schemas.api.log_handler import LogHandlerSchema
from polyaxon.schemas.base import BaseConfig, BaseSchema
from polyaxon.utils.tz_utils import now


class CliConfigurationSchema(BaseSchema):
    current_version = fields.Str(allow_none=True)
    server_installation = fields.Dict(allow_none=True)
    log_handler = fields.Nested(LogHandlerSchema, allow_none=True)
    last_check = fields.DateTime(allow_none=True)

    @staticmethod
    def schema_config():
        return CliConfigurationConfig


class CliConfigurationConfig(BaseConfig):
    SCHEMA = CliConfigurationSchema
    IDENTIFIER = "cli"
    INTERVAL = 30 * 60

    def __init__(
        self,
        current_version=None,
        server_installation=None,
        log_handler=None,
        last_check=None,
    ):
        self.current_version = current_version
        self.server_installation = server_installation
        self.log_handler = log_handler
        self.last_check = self.get_last_check(last_check)

    @classmethod
    def get_last_check(cls, last_check):
        return last_check or now() - timedelta(cls.INTERVAL)

    @property
    def min_version(self):
        if not self.server_installation or "cli" not in self.server_installation:
            return None
        cli_version = self.server_installation["cli"] or {}
        return cli_version.get("min_version")

    @property
    def latest_version(self):
        if not self.server_installation or "cli" not in self.server_installation:
            return None
        cli_version = self.server_installation["cli"] or {}
        return cli_version.get("latest_version")

    def should_check(self):
        if (now() - self.last_check).total_seconds() > self.INTERVAL:
            return True
        if self.current_version is None or self.min_version is None:
            return True

        return False
