# -*- coding: utf-8 -*-
"""DNACenterAPI Device Replacement API fixtures and tests.

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


def is_valid_deploy_device_replacement_workflow(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.device_replacement
def test_deploy_device_replacement_workflow(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'device-replacement', 'deploy-device-replacement-workflow',
                                 """--active_validation=True""",
                                 """--faultydeviceserialnumber='string'""",
                                 """--payload=None""",
                                 """--replacementdeviceserialnumber='string'"""])
    assert not result.exception
    assert is_valid_deploy_device_replacement_workflow(result)


def is_valid_unmark_device_for_replacement(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.device_replacement
def test_unmark_device_for_replacement(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'device-replacement', 'unmark-device-for-replacement',
                                 """--active_validation=True""",
                                 """--payload='{"creationTime": 0, "family": "string", "faultyDeviceId": "string", "faultyDeviceName": "string", "faultyDevicePlatform": "string", "faultyDeviceSerialNumber": "string", "id": "string", "neighbourDeviceId": "string", "networkReadinessTaskId": "string", "replacementDevicePlatform": "string", "replacementDeviceSerialNumber": "string", "replacementStatus": "string", "replacementTime": 0, "workflowId": "string"}'"""])
    assert not result.exception
    assert is_valid_unmark_device_for_replacement(result)


def is_valid_mark_device_for_replacement(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.device_replacement
def test_mark_device_for_replacement(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'device-replacement', 'mark-device-for-replacement',
                                 """--active_validation=True""",
                                 """--payload='{"creationTime": 0, "family": "string", "faultyDeviceId": "string", "faultyDeviceName": "string", "faultyDevicePlatform": "string", "faultyDeviceSerialNumber": "string", "id": "string", "neighbourDeviceId": "string", "networkReadinessTaskId": "string", "replacementDevicePlatform": "string", "replacementDeviceSerialNumber": "string", "replacementStatus": "string", "replacementTime": 0, "workflowId": "string"}'"""])
    assert not result.exception
    assert is_valid_mark_device_for_replacement(result)


def is_valid_return_replacement_devices_with_details(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.device_replacement
def test_return_replacement_devices_with_details(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'device-replacement', 'return-replacement-devices-with-details',
                                 """--family='value1,value2'""",
                                 """--faulty_device_name='string'""",
                                 """--faulty_device_platform='string'""",
                                 """--faulty_device_serial_number='string'""",
                                 """--limit=0""",
                                 """--offset=0""",
                                 """--replacement_device_platform='string'""",
                                 """--replacement_device_serial_number='string'""",
                                 """--replacement_status='value1,value2'""",
                                 """--sort_by='string'""",
                                 """--sort_order='string'"""])
    assert not result.exception
    assert is_valid_return_replacement_devices_with_details(result)


def is_valid_return_replacement_devices_count(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.device_replacement
def test_return_replacement_devices_count(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'device-replacement', 'return-replacement-devices-count',
                                 """--replacement_status='value1,value2'"""])
    assert not result.exception
    assert is_valid_return_replacement_devices_count(result)
