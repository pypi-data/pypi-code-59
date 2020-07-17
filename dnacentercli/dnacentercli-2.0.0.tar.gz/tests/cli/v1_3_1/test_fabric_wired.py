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


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.3.1', reason='version does not match')


def is_valid_delete_ip_pool_from_sda_virtual_network(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.fabric_wired
def test_delete_ip_pool_from_sda_virtual_network(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'fabric-wired', 'delete-ip-pool-from-sda-virtual-network',
                                 """--ip_pool_name='string'""",
                                 """--virtual_network_name='string'"""])
    assert not result.exception
    assert is_valid_delete_ip_pool_from_sda_virtual_network(result)


def is_valid_delete_edge_device(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.fabric_wired
def test_delete_edge_device(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'fabric-wired', 'delete-edge-device',
                                 """--device_ipaddress='string'"""])
    assert not result.exception
    assert is_valid_delete_edge_device(result)


def is_valid_delete_default_authentication_profile(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.fabric_wired
def test_delete_default_authentication_profile(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'fabric-wired', 'delete-default-authentication-profile',
                                 """--site_name_hierarchy='string'"""])
    assert not result.exception
    assert is_valid_delete_default_authentication_profile(result)


def is_valid_update_default_authentication_profile(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.fabric_wired
def test_update_default_authentication_profile(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'fabric-wired', 'update-default-authentication-profile',
                                 """--active_validation=True""",
                                 """--payload='{"siteNameHierarchy": "string", "authenticateTemplateName": "string"}'"""])
    assert not result.exception
    assert is_valid_update_default_authentication_profile(result)


def is_valid_get_edge_device(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.fabric_wired
def test_get_edge_device(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'fabric-wired', 'get-edge-device',
                                 """--device_ipaddress='string'"""])
    assert not result.exception
    assert is_valid_get_edge_device(result)


def is_valid_add_port_assignment_for_user_device(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.fabric_wired
def test_add_port_assignment_for_user_device(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'fabric-wired', 'add-port-assignment-for-user-device',
                                 """--active_validation=True""",
                                 """--payload='{"siteNameHierarchy": "string", "deviceManagementIpAddress": "string", "interfaceName": "string", "dataIpAddressPoolName": "string", "voiceIpAddressPoolName": "string", "authenticateTemplateName": "string"}'"""])
    assert not result.exception
    assert is_valid_add_port_assignment_for_user_device(result)


def is_valid_deletes_border_device(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.fabric_wired
def test_deletes_border_device(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'fabric-wired', 'deletes-border-device',
                                 """--device_ipaddress='string'"""])
    assert not result.exception
    assert is_valid_deletes_border_device(result)


def is_valid_add_edge_device(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.fabric_wired
def test_add_edge_device(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'fabric-wired', 'add-edge-device',
                                 """--active_validation=True""",
                                 """--payload='{"deviceManagementIpAddress": "string", "siteNameHierarchy": "string"}'"""])
    assert not result.exception
    assert is_valid_add_edge_device(result)


def is_valid_add_default_authentication_profile(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.fabric_wired
def test_add_default_authentication_profile(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'fabric-wired', 'add-default-authentication-profile',
                                 """--active_validation=True""",
                                 """--payload='{"siteNameHierarchy": "string", "authenticateTemplateName": "string"}'"""])
    assert not result.exception
    assert is_valid_add_default_authentication_profile(result)


def is_valid_delete_port_assignment_for_user_device(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.fabric_wired
def test_delete_port_assignment_for_user_device(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'fabric-wired', 'delete-port-assignment-for-user-device',
                                 """--device_ip='string'""",
                                 """--interface_name='string'"""])
    assert not result.exception
    assert is_valid_delete_port_assignment_for_user_device(result)


def is_valid_add_ip_pool_in_sda_virtual_network(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.fabric_wired
def test_add_ip_pool_in_sda_virtual_network(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'fabric-wired', 'add-ip-pool-in-sda-virtual-network',
                                 """--active_validation=True""",
                                 """--payload='{"virtualNetworkName": "string", "ipPoolName": "string", "trafficType": "string", "authenticationPolicyName": "string", "scalableGroupName": "string", "isL2FloodingEnabled": true, "isThisCriticalPool": true, "poolType": "string"}'"""])
    assert not result.exception
    assert is_valid_add_ip_pool_in_sda_virtual_network(result)


def is_valid_gets_border_device_detail(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.fabric_wired
def test_gets_border_device_detail(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'fabric-wired', 'gets-border-device-detail',
                                 """--device_ipaddress='string'"""])
    assert not result.exception
    assert is_valid_gets_border_device_detail(result)


def is_valid_get_port_assignment_for_user_device(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.fabric_wired
def test_get_port_assignment_for_user_device(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'fabric-wired', 'get-port-assignment-for-user-device',
                                 """--device_ip='string'""",
                                 """--interface_name='string'"""])
    assert not result.exception
    assert is_valid_get_port_assignment_for_user_device(result)


def is_valid_get_default_authentication_profile(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.fabric_wired
def test_get_default_authentication_profile(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'fabric-wired', 'get-default-authentication-profile',
                                 """--site_name_hierarchy='string'"""])
    assert not result.exception
    assert is_valid_get_default_authentication_profile(result)


def is_valid_adds_border_device(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.fabric_wired
def test_adds_border_device(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'fabric-wired', 'adds-border-device',
                                 """--active_validation=True""",
                                 """--payload='{"deviceManagementIpAddress": "string", "siteNameHierarchy": "string", "externalDomainRoutingProtocolName": "string", "externalConnectivityIpPoolName": "string", "internalAutonomouSystemNumber": "string", "borderSessionType": "string", "connectedToInternet": true, "externalConnectivitySettings": [{"interfaceName": "string", "externalAutonomouSystemNumber": "string", "l3Handoff": [{"virtualNetwork": {"virtualNetworkName": "string"}}]}]}'"""])
    assert not result.exception
    assert is_valid_adds_border_device(result)


def is_valid_get_ip_pool_from_sda_virtual_network(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.fabric_wired
def test_get_ip_pool_from_sda_virtual_network(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'fabric-wired', 'get-ip-pool-from-sda-virtual-network',
                                 """--ip_pool_name='string'""",
                                 """--virtual_network_name='string'"""])
    assert not result.exception
    assert is_valid_get_ip_pool_from_sda_virtual_network(result)
