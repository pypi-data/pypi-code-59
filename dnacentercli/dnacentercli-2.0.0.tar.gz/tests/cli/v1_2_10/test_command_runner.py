# -*- coding: utf-8 -*-
"""DNACenterAPI Command Runner API fixtures and tests.

Copyright (c) 2019 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import click
import pytest
from json import loads
from tests.environment import DNA_CENTER_VERSION


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


def is_valid_get_all_keywords_of_clis_accepted(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.command_runner
def test_get_all_keywords_of_clis_accepted(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'command-runner', 'get-all-keywords-of-clis-accepted',
                                 """--"""])
    assert not result.exception
    assert is_valid_get_all_keywords_of_clis_accepted(result)


def is_valid_run_read_only_commands_on_devices(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.command_runner
def test_run_read_only_commands_on_devices(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'command-runner', 'run-read-only-commands-on-devices',
                                 """--active_validation=True""",
                                 """--commands='string'""",
                                 """--description='string'""",
                                 """--deviceuuids='string'""",
                                 """--name='string'""",
                                 """--payload=None""",
                                 """--timeout=0"""])
    assert not result.exception
    assert is_valid_run_read_only_commands_on_devices(result)
