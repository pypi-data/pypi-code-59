# -*- coding: utf-8 -*-
"""DNACenterAPI Application Policy API fixtures and tests.

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


def is_valid_create_application_set(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.application_policy
def test_create_application_set(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'application-policy', 'create-application-set',
                                 """--active_validation=True""",
                                 """--payload='{"name": "string"}'"""])
    assert not result.exception
    assert is_valid_create_application_set(result)


def is_valid_get_application_sets_count(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.application_policy
def test_get_application_sets_count(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'application-policy', 'get-application-sets-count',
                                 """--"""])
    assert not result.exception
    assert is_valid_get_application_sets_count(result)


def is_valid_create_application(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.application_policy
def test_create_application(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'application-policy', 'create-application',
                                 """--active_validation=True""",
                                 """--payload='{"name": "string", "networkApplications": [{"appProtocol": "string", "applicationSubType": "string", "applicationType": "string", "categoryId": "string", "displayName": "string", "engineId": "string", "helpString": "string", "longDescription": "string", "name": "string", "popularity": "string", "rank": "string", "trafficClass": "string", "serverName": "string", "url": "string", "dscp": "string", "ignoreConflict": "string"}], "networkIdentity": [{"displayName": "string", "lowerPort": "string", "ports": "string", "protocol": "string", "upperPort": "string"}], "applicationSet": {"idRef": "string"}}'"""])
    assert not result.exception
    assert is_valid_create_application(result)


def is_valid_delete_application(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.application_policy
def test_delete_application(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'application-policy', 'delete-application',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_delete_application(result)


def is_valid_get_application_sets(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.application_policy
def test_get_application_sets(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'application-policy', 'get-application-sets',
                                 """--limit=500""",
                                 """--name='string'""",
                                 """--offset=1"""])
    assert not result.exception
    assert is_valid_get_application_sets(result)


def is_valid_get_applications_count(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.application_policy
def test_get_applications_count(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'application-policy', 'get-applications-count',
                                 """--"""])
    assert not result.exception
    assert is_valid_get_applications_count(result)


def is_valid_edit_application(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.application_policy
def test_edit_application(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'application-policy', 'edit-application',
                                 """--active_validation=True""",
                                 """--payload='{"id": "string", "name": "string", "networkApplications": [{"id": "string", "appProtocol": "string", "applicationSubType": "string", "applicationType": "string", "categoryId": "string", "displayName": "string", "engineId": "string", "helpString": "string", "longDescription": "string", "name": "string", "popularity": "string", "rank": "string", "trafficClass": "string", "serverName": "string", "url": "string", "dscp": "string", "ignoreConflict": "string"}], "networkIdentity": [{"id": "string", "displayName": "string", "lowerPort": "string", "ports": "string", "protocol": "string", "upperPort": "string"}], "applicationSet": {"idRef": "string"}}'"""])
    assert not result.exception
    assert is_valid_edit_application(result)


def is_valid_delete_application_set(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.application_policy
def test_delete_application_set(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'application-policy', 'delete-application-set',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_delete_application_set(result)


def is_valid_get_applications(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.application_policy
def test_get_applications(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'application-policy', 'get-applications',
                                 """--limit=500""",
                                 """--name='string'""",
                                 """--offset=1"""])
    assert not result.exception
    assert is_valid_get_applications(result)
