# -*- coding: utf-8 -*-
"""DNACenterAPI Path Trace API fixtures and tests.

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


def is_valid_retrives_all_previous_pathtraces_summary(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.path_trace
def test_retrives_all_previous_pathtraces_summary(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'path-trace', 'retrives-all-previous-pathtraces-summary',
                                 """--dest_ip='string'""",
                                 """--dest_port='string'""",
                                 """--gt_create_time='string'""",
                                 """--last_update_time='string'""",
                                 """--limit='string'""",
                                 """--lt_create_time='string'""",
                                 """--offset='string'""",
                                 """--order='string'""",
                                 """--periodic_refresh=True""",
                                 """--protocol='string'""",
                                 """--sort_by='string'""",
                                 """--source_ip='string'""",
                                 """--source_port='string'""",
                                 """--status='string'""",
                                 """--task_id='string'"""])
    assert not result.exception
    assert is_valid_retrives_all_previous_pathtraces_summary(result)


def is_valid_deletes_pathtrace_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.path_trace
def test_deletes_pathtrace_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'path-trace', 'deletes-pathtrace-by-id',
                                 """--flow_analysis_id='string'"""])
    assert not result.exception
    assert is_valid_deletes_pathtrace_by_id(result)


def is_valid_initiate_a_new_pathtrace(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.path_trace
def test_initiate_a_new_pathtrace(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'path-trace', 'initiate-a-new-pathtrace',
                                 """--active_validation=True""",
                                 """--controlpath=True""",
                                 """--destip='string'""",
                                 """--destport='string'""",
                                 """--inclusions='string'""",
                                 """--payload=None""",
                                 """--periodicrefresh=True""",
                                 """--protocol='string'""",
                                 """--sourceip='string'""",
                                 """--sourceport='string'"""])
    assert not result.exception
    assert is_valid_initiate_a_new_pathtrace(result)


def is_valid_retrieves_previous_pathtrace(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.path_trace
def test_retrieves_previous_pathtrace(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'path-trace', 'retrieves-previous-pathtrace',
                                 """--flow_analysis_id='string'"""])
    assert not result.exception
    assert is_valid_retrieves_previous_pathtrace(result)
