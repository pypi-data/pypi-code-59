# -*- coding: utf-8 -*-
"""DNACenterAPI Non-Fabric Wireless API fixtures and tests.

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


def is_valid_delete_and_provision_ssid(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.non_fabric_wireless
def test_delete_and_provision_ssid(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'non-fabric-wireless', 'delete-and-provision-ssid',
                                 """--managed_aplocations='string'""",
                                 """--ssid_name='string'"""])
    assert not result.exception
    assert is_valid_delete_and_provision_ssid(result)


def is_valid_create_enterprise_ssid(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.non_fabric_wireless
def test_create_enterprise_ssid(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'non-fabric-wireless', 'create-enterprise-ssid',
                                 """--active_validation=True""",
                                 """--enablebroadcastssid=True""",
                                 """--enablefastlane=True""",
                                 """--enablemacfiltering=True""",
                                 """--fasttransition='Adaptive'""",
                                 """--name='********************************'""",
                                 """--passphrase='********'""",
                                 """--payload=None""",
                                 """--radiopolicy='Dual band operation (2.4GHz and 5GHz)'""",
                                 """--securitylevel='WPA2_ENTERPRISE'""",
                                 """--traffictype='voicedata'"""])
    assert not result.exception
    assert is_valid_create_enterprise_ssid(result)


def is_valid_create_and_provision_ssid(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.non_fabric_wireless
def test_create_and_provision_ssid(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'non-fabric-wireless', 'create-and-provision-ssid',
                                 """--active_validation=True""",
                                 """--enablefabric=True""",
                                 """--flexconnect='{"enableFlexConnect": true, "localToVlan": 0}'""",
                                 """--managedaplocations='string'""",
                                 """--payload=None""",
                                 """--ssiddetails='{"name": "string", "securityLevel": "WPA2_ENTERPRISE", "enableFastLane": true, "passphrase": "string", "trafficType": "data", "enableBroadcastSSID": true, "radioPolicy": "Dual band operation (2.4GHz and 5GHz)", "enableMACFiltering": true, "fastTransition": "Adaptive", "webAuthURL": "string"}'""",
                                 """--ssidtype='Guest'""",
                                 """--vlananddynamicinterfacedetails='{"managedAPLocation": {"interfaceIPAddress": "string", "interfaceNetmaskInCIDR": 0, "interfaceGateway": "string", "lagOrPortNumber": 0}, "vlanId": 0, "vlanName": "string"}'"""])
    assert not result.exception
    assert is_valid_create_and_provision_ssid(result)


def is_valid_delete_enterprise_ssid(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.non_fabric_wireless
def test_delete_enterprise_ssid(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'non-fabric-wireless', 'delete-enterprise-ssid',
                                 """--ssid_name='string'"""])
    assert not result.exception
    assert is_valid_delete_enterprise_ssid(result)


def is_valid_get_enterprise_ssid(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.non_fabric_wireless
def test_get_enterprise_ssid(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'non-fabric-wireless', 'get-enterprise-ssid',
                                 """--ssid_name='string'"""])
    assert not result.exception
    assert is_valid_get_enterprise_ssid(result)
