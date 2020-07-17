# -*- coding: utf-8 -*-
"""DNACenterAPI Task API fixtures and tests.

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


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.1.1', reason='version does not match')


def is_valid_get_task_count(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.task
def test_get_task_count(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'task', 'get-task-count',
                                 """--data='string'""",
                                 """--end_time='string'""",
                                 """--error_code='string'""",
                                 """--failure_reason='string'""",
                                 """--is_error='string'""",
                                 """--parent_id='string'""",
                                 """--progress='string'""",
                                 """--service_type='string'""",
                                 """--start_time='string'""",
                                 """--username='string'"""])
    assert not result.exception
    assert is_valid_get_task_count(result)


def is_valid_get_task_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.task
def test_get_task_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'task', 'get-task-by-id',
                                 """--task_id='string'"""])
    assert not result.exception
    assert is_valid_get_task_by_id(result)


def is_valid_get_tasks(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.task
def test_get_tasks(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'task', 'get-tasks',
                                 """--data='string'""",
                                 """--end_time='string'""",
                                 """--error_code='string'""",
                                 """--failure_reason='string'""",
                                 """--is_error='string'""",
                                 """--limit='string'""",
                                 """--offset='string'""",
                                 """--order='string'""",
                                 """--parent_id='string'""",
                                 """--progress='string'""",
                                 """--service_type='string'""",
                                 """--sort_by='string'""",
                                 """--start_time='string'""",
                                 """--username='string'"""])
    assert not result.exception
    assert is_valid_get_tasks(result)


def is_valid_get_task_tree(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.task
def test_get_task_tree(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'task', 'get-task-tree',
                                 """--task_id='string'"""])
    assert not result.exception
    assert is_valid_get_task_tree(result)


def is_valid_get_task_by_operationid(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.task
def test_get_task_by_operationid(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'task', 'get-task-by-operationid',
                                 """--limit=0""",
                                 """--offset=0""",
                                 """--operation_id='string'"""])
    assert not result.exception
    assert is_valid_get_task_by_operationid(result)
