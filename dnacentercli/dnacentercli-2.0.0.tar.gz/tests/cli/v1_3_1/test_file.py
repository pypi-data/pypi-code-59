# -*- coding: utf-8 -*-
"""DNACenterAPI File API fixtures and tests.

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


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.3.1', reason='version does not match')


def is_valid_get_list_of_available_namespaces(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.file
def test_get_list_of_available_namespaces(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'file', 'get-list-of-available-namespaces',
                                 """--"""])
    assert not result.exception
    assert is_valid_get_list_of_available_namespaces(result)


def is_valid_get_list_of_files(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.file
def test_get_list_of_files(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'file', 'get-list-of-files',
                                 """--name_space='string'"""])
    assert not result.exception
    assert is_valid_get_list_of_files(result)


def is_valid_download_a_file_by_fileid(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.file
def test_download_a_file_by_fileid(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'file', 'download-a-file-by-fileid',
                                 """--dirpath=None""",
                                 """--save_file=False""",
                                 """--file_id='string'"""])
    assert not result.exception
    assert is_valid_download_a_file_by_fileid(result)
