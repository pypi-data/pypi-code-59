# -*- coding: utf-8 -*-
"""DNACenterAPI Sites API fixtures and tests.

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


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.3.0', reason='version does not match')


def is_valid_get_site_health(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.sites
def test_get_site_health(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'sites', 'get-site-health',
                                 """--timestamp=0"""])
    assert not result.exception
    assert is_valid_get_site_health(result)


def is_valid_update_site(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.sites
def test_update_site(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'sites', 'update-site',
                                 """--active_validation=True""",
                                 """--payload=None""",
                                 """--site='{"area": {"name": "string", "parentName": "string"}, "building": {"name": "string", "address": "string", "parentName": "string", "latitude": 0, "longitude": 0}, "floor": {"name": "string", "rfModel": "Cubes And Walled Offices", "width": 0, "length": 0, "height": 0}}'""",
                                 """--site_id='string'""",
                                 """--type='area'"""])
    assert not result.exception
    assert is_valid_update_site(result)


def is_valid_create_site(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.sites
def test_create_site(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'sites', 'create-site',
                                 """--active_validation=True""",
                                 """--payload=None""",
                                 """--site='{"area": {"name": "string", "parentName": "string"}, "building": {"name": "string", "address": "string", "parentName": "string", "latitude": 0, "longitude": 0}, "floor": {"name": "string", "parentName": "string", "rfModel": "Cubes And Walled Offices", "width": 0, "length": 0, "height": 0}}'""",
                                 """--type='area'"""])
    assert not result.exception
    assert is_valid_create_site(result)


def is_valid_get_site(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.sites
def test_get_site(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'sites', 'get-site',
                                 """--limit=0""",
                                 """--name='string'""",
                                 """--offset=0""",
                                 """--site_id='string'""",
                                 """--type='string'"""])
    assert not result.exception
    assert is_valid_get_site(result)


def is_valid_delete_site(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.sites
def test_delete_site(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'sites', 'delete-site',
                                 """--site_id='string'"""])
    assert not result.exception
    assert is_valid_delete_site(result)


def is_valid_get_site_count(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.sites
def test_get_site_count(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'sites', 'get-site-count',
                                 """--site_id='string'"""])
    assert not result.exception
    assert is_valid_get_site_count(result)


def is_valid_assign_device_to_site(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.sites
def test_assign_device_to_site(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'sites', 'assign-device-to-site',
                                 """--active_validation=True""",
                                 """--device='{"ip": "string"}'""",
                                 """--payload=None""",
                                 """--site_id='string'"""])
    assert not result.exception
    assert is_valid_assign_device_to_site(result)


def is_valid_get_membership(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.sites
def test_get_membership(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'sites', 'get-membership',
                                 """--site_id='string'"""])
    assert not result.exception
    assert is_valid_get_membership(result)
