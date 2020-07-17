# -*- coding: utf-8 -*-
"""DNACenterAPI Fabric Wired API fixtures and tests.

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


def is_valid_gets_border_device_detail(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.fabric_wired
def test_gets_border_device_detail(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'fabric-wired', 'gets-border-device-detail',
                                 """--device_ip_address='string'""",
                                 """--sda_border_device='border-device'"""])
    assert not result.exception
    assert is_valid_gets_border_device_detail(result)


def is_valid_adds_border_device(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.fabric_wired
def test_adds_border_device(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'fabric-wired', 'adds-border-device',
                                 """--active_validation=True""",
                                 """--payload='{"deviceManagementIpAddress": "string", "siteHierarchy": "string", "externalDomainRoutingProtocolName": "string", "externalConnectivityIpPoolName": "string", "internalAutonomouSystemNumber": "string", "borderSessionType": "string", "connectedToInternet": true, "externalConnectivitySettings": [{"interfaceName": "string", "externalAutonomouSystemNumber": "string", "l3Handoff": [{"virtualNetwork": {"virtualNetworkName": "string"}}]}]}'""",
                                 """--sda_border_device='border-device'"""])
    assert not result.exception
    assert is_valid_adds_border_device(result)


def is_valid_deletes_border_device(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.fabric_wired
def test_deletes_border_device(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'fabric-wired', 'deletes-border-device',
                                 """--device_ip_address='string'""",
                                 """--sda_border_device='border-device'"""])
    assert not result.exception
    assert is_valid_deletes_border_device(result)
