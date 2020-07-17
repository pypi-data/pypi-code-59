# -*- coding: utf-8 -*-
"""DNACenterAPI Network Settings API fixtures and tests.

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


def is_valid_update_global_pool(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_settings
def test_update_global_pool(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'network-settings', 'update-global-pool',
                                 """--active_validation=True""",
                                 """--payload=None""",
                                 """--settings='{"ippool": [{"ipPoolName": "string", "gateway": "string", "dhcpServerIps": ["string"], "dnsServerIps": ["string"], "id": "string"}]}'"""])
    assert not result.exception
    assert is_valid_update_global_pool(result)


def is_valid_get_network(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_settings
def test_get_network(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'network-settings', 'get-network',
                                 """--site_id='string'"""])
    assert not result.exception
    assert is_valid_get_network(result)


def is_valid_delete_sp_profile(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_settings
def test_delete_sp_profile(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'network-settings', 'delete-sp-profile',
                                 """--sp_profile_name='string'"""])
    assert not result.exception
    assert is_valid_delete_sp_profile(result)


def is_valid_delete_global_ip_pool(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_settings
def test_delete_global_ip_pool(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'network-settings', 'delete-global-ip-pool',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_delete_global_ip_pool(result)


def is_valid_update_sp_profile(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_settings
def test_update_sp_profile(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'network-settings', 'update-sp-profile',
                                 """--active_validation=True""",
                                 """--payload=None""",
                                 """--settings='{"qos": [{"profileName": "string", "model": "string", "wanProvider": "string", "oldProfileName": "string"}]}'"""])
    assert not result.exception
    assert is_valid_update_sp_profile(result)


def is_valid_delete_device_credential(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_settings
def test_delete_device_credential(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'network-settings', 'delete-device-credential',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_delete_device_credential(result)


def is_valid_assign_credential_to_site(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_settings
def test_assign_credential_to_site(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'network-settings', 'assign-credential-to-site',
                                 """--active_validation=True""",
                                 """--cliid='string'""",
                                 """--httpread='string'""",
                                 """--httpwrite='string'""",
                                 """--payload=None""",
                                 """--site_id='string'""",
                                 """--snmpv2readid='string'""",
                                 """--snmpv2writeid='string'""",
                                 """--snmpv3id='string'"""])
    assert not result.exception
    assert is_valid_assign_credential_to_site(result)


def is_valid_update_network(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_settings
def test_update_network(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'network-settings', 'update-network',
                                 """--active_validation=True""",
                                 """--payload=None""",
                                 """--settings='{"dhcpServer": ["string"], "dnsServer": {"domainName": "can only contain alphanumeric characters or hyphen", "primaryIpAddress": "valid range : 1.0.0.0 - 223.255.255.255", "secondaryIpAddress": "valid range : 1.0.0.0 - 223.255.255.255"}, "syslogServer": {"ipAddresses": ["string"], "configureDnacIP": true}, "snmpServer": {"ipAddresses": ["string"], "configureDnacIP": true}, "netflowcollector": {"ipAddress": "string", "port": 0}, "ntpServer": ["string"], "timezone": "string", "messageOfTheday": {"bannerMessage": "string", "retainExistingBanner": true}, "network_aaa": {"servers": "Server type supported by ISE and AAA", "ipAddress": "Mandatory for ISE servers and for AAA consider this as additional Ip.", "network": "For AAA server consider it as primary IP and For ISE consider as Network", "protocol": "string", "sharedSecret": "Supported only by ISE servers"}, "clientAndEndpoint_aaa": {"servers": "string", "ipAddress": "Mandatory for ISE servers.", "network": "string", "protocol": "string", "sharedSecret": "Supported only by ISE servers"}}'""",
                                 """--site_id='string'"""])
    assert not result.exception
    assert is_valid_update_network(result)


def is_valid_update_device_credentials(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_settings
def test_update_device_credentials(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'network-settings', 'update-device-credentials',
                                 """--active_validation=True""",
                                 """--payload=None""",
                                 """--settings='{"cliCredential": {"description": "string", "username": "string", "password": "string", "enablePassword": "string", "id": "string"}, "snmpV2cRead": {"description": "string", "readCommunity": "string", "id": "string"}, "snmpV2cWrite": {"description": "string", "writeCommunity": "string", "id": "string"}, "snmpV3": {"authPassword": "string", "authType": "string", "snmpMode": "string", "privacyPassword": "string", "privacyType": "string", "username": "string", "description": "string", "id": "string"}, "httpsRead": {"name": "string", "username": "string", "password": "string", "port": "string", "id": "string"}, "httpsWrite": {"name": "string", "username": "string", "password": "string", "port": "string", "id": "string"}}'"""])
    assert not result.exception
    assert is_valid_update_device_credentials(result)


def is_valid_get_service_provider_details(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_settings
def test_get_service_provider_details(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'network-settings', 'get-service-provider-details',
                                 """--"""])
    assert not result.exception
    assert is_valid_get_service_provider_details(result)


def is_valid_get_device_credential_details(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_settings
def test_get_device_credential_details(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'network-settings', 'get-device-credential-details',
                                 """--site_id='string'"""])
    assert not result.exception
    assert is_valid_get_device_credential_details(result)


def is_valid_create_sp_profile(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_settings
def test_create_sp_profile(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'network-settings', 'create-sp-profile',
                                 """--active_validation=True""",
                                 """--payload=None""",
                                 """--settings='{"qos": [{"profileName": "string", "model": "string", "wanProvider": "string"}]}'"""])
    assert not result.exception
    assert is_valid_create_sp_profile(result)


def is_valid_get_global_pool(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_settings
def test_get_global_pool(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'network-settings', 'get-global-pool',
                                 """--limit='string'""",
                                 """--offset='string'"""])
    assert not result.exception
    assert is_valid_get_global_pool(result)


def is_valid_create_network(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_settings
def test_create_network(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'network-settings', 'create-network',
                                 """--active_validation=True""",
                                 """--payload=None""",
                                 """--settings='{"dhcpServer": ["string"], "dnsServer": {"domainName": "can only contain alphanumeric characters or hyphen", "primaryIpAddress": "valid range : 1.0.0.0 - 223.255.255.255", "secondaryIpAddress": "valid range : 1.0.0.0 - 223.255.255.255"}, "syslogServer": {"ipAddresses": ["string"], "configureDnacIP": true}, "snmpServer": {"ipAddresses": ["string"], "configureDnacIP": true}, "netflowcollector": {"ipAddress": "string", "port": 0}, "ntpServer": ["string"], "timezone": "string", "messageOfTheday": {"bannerMessage": "string", "retainExistingBanner": true}, "network_aaa": {"servers": "Server type supported by ISE and AAA", "ipAddress": "Mandatory for ISE servers and for AAA consider this as additional Ip.", "network": "For AAA server consider it as primary IP and For ISE consider as Network", "protocol": "string", "sharedSecret": "Supported only by ISE servers"}, "clientAndEndpoint_aaa": {"servers": "string", "ipAddress": "Mandatory for ISE servers.", "network": "string", "protocol": "string", "sharedSecret": "Supported only by ISE servers"}}'""",
                                 """--site_id='string'"""])
    assert not result.exception
    assert is_valid_create_network(result)


def is_valid_create_device_credentials(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_settings
def test_create_device_credentials(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'network-settings', 'create-device-credentials',
                                 """--active_validation=True""",
                                 """--payload=None""",
                                 """--settings='{"cliCredential": [{"description": "string", "username": "string", "password": "string", "enablePassword": "string"}], "snmpV2cRead": [{"description": "string", "readCommunity": "string"}], "snmpV2cWrite": [{"description": "string", "writeCommunity": "string"}], "snmpV3": [{"description": "string", "username": "string", "privacyType": "AES128", "privacyPassword": "string", "authType": "SHA", "authPassword": "string", "snmpMode": "AUTHPRIV"}], "httpsRead": [{"name": "string", "username": "string", "password": "string", "port": 0}], "httpsWrite": [{"name": "string", "username": "string", "password": "string", "port": 0}]}'"""])
    assert not result.exception
    assert is_valid_create_device_credentials(result)


def is_valid_create_global_pool(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_settings
def test_create_global_pool(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'network-settings', 'create-global-pool',
                                 """--active_validation=True""",
                                 """--payload=None""",
                                 """--settings='{"ippool": [{"ipPoolName": "string", "type": "Generic", "ipPoolCidr": "string", "gateway": "string", "dhcpServerIps": ["string"], "dnsServerIps": ["string"], "IpAddressSpace": "IPv6 or IPv4"}]}'"""])
    assert not result.exception
    assert is_valid_create_global_pool(result)
