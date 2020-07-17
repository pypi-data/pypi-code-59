# -*- coding: utf-8 -*-
"""DNACenterAPI Event Management API fixtures and tests.

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


def is_valid_count_of_event_subscriptions(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.event_management
def test_count_of_event_subscriptions(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'event-management', 'count-of-event-subscriptions',
                                 """--event_ids='string'"""])
    assert not result.exception
    assert is_valid_count_of_event_subscriptions(result)


def is_valid_get_events(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.event_management
def test_get_events(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'event-management', 'get-events',
                                 """--event_id=' '""",
                                 """--limit=10""",
                                 """--offset=0""",
                                 """--order='string'""",
                                 """--sort_by='string'""",
                                 """--tags='string'"""])
    assert not result.exception
    assert is_valid_get_events(result)


def is_valid_create_event_subscriptions(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.event_management
def test_create_event_subscriptions(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'event-management', 'create-event-subscriptions',
                                 """--active_validation=True""",
                                 """--payload='{"subscriptionId": "string", "version": "string", "name": "string", "description": "string", "subscriptionEndpoints": [{"instanceId": "string", "subscriptionDetails": {"name": "string", "url": "string", "method": "string", "connectorType": "string"}}], "filter": {"eventIds": ["string"]}}'"""])
    assert not result.exception
    assert is_valid_create_event_subscriptions(result)


def is_valid_update_event_subscriptions(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.event_management
def test_update_event_subscriptions(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'event-management', 'update-event-subscriptions',
                                 """--active_validation=True""",
                                 """--payload='{"subscriptionId": "string", "version": "string", "name": "string", "description": "string", "subscriptionEndpoints": [{"instanceId": "string", "subscriptionDetails": {"name": "string", "url": "string", "method": "string", "connectorType": "string"}}], "filter": {"eventIds": ["string"]}}'"""])
    assert not result.exception
    assert is_valid_update_event_subscriptions(result)


def is_valid_count_of_notifications(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.event_management
def test_count_of_notifications(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'event-management', 'count-of-notifications',
                                 """--category='string'""",
                                 """--domain='string'""",
                                 """--end_time='string'""",
                                 """--event_ids='string'""",
                                 """--severity='string'""",
                                 """--source='string'""",
                                 """--start_time='string'""",
                                 """--sub_domain='string'""",
                                 """--type='string'"""])
    assert not result.exception
    assert is_valid_count_of_notifications(result)


def is_valid_delete_event_subscriptions(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.event_management
def test_delete_event_subscriptions(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'event-management', 'delete-event-subscriptions',
                                 """--subscriptions='string'"""])
    assert not result.exception
    assert is_valid_delete_event_subscriptions(result)


def is_valid_get_notifications(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.event_management
def test_get_notifications(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'event-management', 'get-notifications',
                                 """--category='string'""",
                                 """--domain='string'""",
                                 """--end_time='string'""",
                                 """--event_ids='string'""",
                                 """--limit=20""",
                                 """--offset=0""",
                                 """--order='string'""",
                                 """--severity='string'""",
                                 """--sort_by='string'""",
                                 """--source='string'""",
                                 """--start_time='string'""",
                                 """--sub_domain='string'""",
                                 """--type='string'"""])
    assert not result.exception
    assert is_valid_get_notifications(result)


def is_valid_get_status_api_for_events(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.event_management
def test_get_status_api_for_events(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'event-management', 'get-status-api-for-events',
                                 """--execution_id='string'"""])
    assert not result.exception
    assert is_valid_get_status_api_for_events(result)


def is_valid_count_of_events(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.event_management
def test_count_of_events(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'event-management', 'count-of-events',
                                 """--event_id='string'""",
                                 """--tags='string'"""])
    assert not result.exception
    assert is_valid_count_of_events(result)


def is_valid_get_event_subscriptions(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.event_management
def test_get_event_subscriptions(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'event-management', 'get-event-subscriptions',
                                 """--event_ids='string'""",
                                 """--limit=10""",
                                 """--offset=0""",
                                 """--order='string'""",
                                 """--sort_by='string'"""])
    assert not result.exception
    assert is_valid_get_event_subscriptions(result)
