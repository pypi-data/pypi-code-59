# -*- coding: utf-8 -*-
"""DNACenterAPI Wireless API fixtures and tests.

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


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.3.3', reason='version does not match')


def is_valid_retrieve_rf_profiles(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.wireless
def test_retrieve_rf_profiles(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.3', *auth_options,
                                 'wireless', 'retrieve-rf-profiles',
                                 """--rf_profile_name='string'"""])
    assert not result.exception
    assert is_valid_retrieve_rf_profiles(result)


def is_valid_create_and_provision_ssid(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.wireless
def test_create_and_provision_ssid(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.3', *auth_options,
                                 'wireless', 'create-and-provision-ssid',
                                 """--active_validation=True""",
                                 """--enablefabric=True""",
                                 """--flexconnect='{"enableFlexConnect": true, "localToVlan": 0}'""",
                                 """--managedaplocations='string'""",
                                 """--payload=None""",
                                 """--ssiddetails='{"name": "string", "securityLevel": "WPA2_ENTERPRISE", "enableFastLane": true, "passphrase": "string", "trafficType": "data", "enableBroadcastSSID": true, "radioPolicy": "Dual band operation (2.4GHz and 5GHz)", "enableMACFiltering": true, "fastTransition": "Adaptive", "webAuthURL": "string"}'""",
                                 """--ssidtype='Guest'"""])
    assert not result.exception
    assert is_valid_create_and_provision_ssid(result)


def is_valid_delete_rf_profiles(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.wireless
def test_delete_rf_profiles(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.3', *auth_options,
                                 'wireless', 'delete-rf-profiles',
                                 """--rf_profile_name='string'"""])
    assert not result.exception
    assert is_valid_delete_rf_profiles(result)


def is_valid_create_wireless_profile(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.wireless
def test_create_wireless_profile(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.3', *auth_options,
                                 'wireless', 'create-wireless-profile',
                                 """--active_validation=True""",
                                 """--payload=None""",
                                 """--profiledetails='{"name": "string", "sites": ["string"], "ssidDetails": [{"name": "string", "type": "Guest", "enableFabric": true, "flexConnect": {"enableFlexConnect": true, "localToVlan": 0}, "interfaceName": "string"}]}'"""])
    assert not result.exception
    assert is_valid_create_wireless_profile(result)


def is_valid_provision_update(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.wireless
def test_provision_update(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.3', *auth_options,
                                 'wireless', 'provision-update',
                                 """--active_validation=True""",
                                 """--payload='{"deviceName": "string", "managedAPLocations": ["string"], "dynamicInterfaces": [{"interfaceIPAddress": "string", "interfaceNetmaskInCIDR": 0, "interfaceGateway": "string", "lagOrPortNumber": 0, "vlanId": 0, "interfaceName": "string"}]}'"""])
    assert not result.exception
    assert is_valid_provision_update(result)


def is_valid_create_enterprise_ssid(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.wireless
def test_create_enterprise_ssid(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.3', *auth_options,
                                 'wireless', 'create-enterprise-ssid',
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


def is_valid_get_wireless_profile(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.wireless
def test_get_wireless_profile(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.3', *auth_options,
                                 'wireless', 'get-wireless-profile',
                                 """--profile_name='string'"""])
    assert not result.exception
    assert is_valid_get_wireless_profile(result)


def is_valid_create_or_update_rf_profile(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.wireless
def test_create_or_update_rf_profile(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.3', *auth_options,
                                 'wireless', 'create-or-update-rf-profile',
                                 """--active_validation=True""",
                                 """--channelwidth='string'""",
                                 """--defaultrfprofile=True""",
                                 """--enablebrownfield=True""",
                                 """--enablecustom=True""",
                                 """--enableradiotypea=True""",
                                 """--enableradiotypeb=True""",
                                 """--name='string'""",
                                 """--payload=None""",
                                 """--radiotypeaproperties='{"parentProfile": "string", "radioChannels": "string", "dataRates": "string", "mandatoryDataRates": "string", "powerThresholdV1": 0, "rxSopThreshold": "string", "minPowerLevel": 0, "maxPowerLevel": 0}'""",
                                 """--radiotypebproperties='{"parentProfile": "string", "radioChannels": "string", "dataRates": "string", "mandatoryDataRates": "string", "powerThresholdV1": 0, "rxSopThreshold": "string", "minPowerLevel": 0, "maxPowerLevel": 0}'"""])
    assert not result.exception
    assert is_valid_create_or_update_rf_profile(result)


def is_valid_delete_enterprise_ssid(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.wireless
def test_delete_enterprise_ssid(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.3', *auth_options,
                                 'wireless', 'delete-enterprise-ssid',
                                 """--ssid_name='string'"""])
    assert not result.exception
    assert is_valid_delete_enterprise_ssid(result)


def is_valid_get_enterprise_ssid(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.wireless
def test_get_enterprise_ssid(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.3', *auth_options,
                                 'wireless', 'get-enterprise-ssid',
                                 """--ssid_name='string'"""])
    assert not result.exception
    assert is_valid_get_enterprise_ssid(result)


def is_valid_provision(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.wireless
def test_provision(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.3', *auth_options,
                                 'wireless', 'provision',
                                 """--active_validation=True""",
                                 """--payload='{"deviceName": "string", "site": "string", "managedAPLocations": ["string"], "dynamicInterfaces": [{"interfaceIPAddress": "string", "interfaceNetmaskInCIDR": 0, "interfaceGateway": "string", "lagOrPortNumber": 0, "vlanId": 0, "interfaceName": "string"}]}'"""])
    assert not result.exception
    assert is_valid_provision(result)


def is_valid_update_wireless_profile(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.wireless
def test_update_wireless_profile(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.3', *auth_options,
                                 'wireless', 'update-wireless-profile',
                                 """--active_validation=True""",
                                 """--payload=None""",
                                 """--profiledetails='{"name": "string", "sites": ["string"], "ssidDetails": [{"name": "string", "type": "Guest", "enableFabric": true, "flexConnect": {"enableFlexConnect": true, "localToVlan": 0}, "interfaceName": "string"}]}'"""])
    assert not result.exception
    assert is_valid_update_wireless_profile(result)


def is_valid_ap_provision(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.wireless
def test_ap_provision(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.3', *auth_options,
                                 'wireless', 'ap-provision',
                                 """--active_validation=True""",
                                 """--payload='{"rfProfile": "string", "siteId": "string", "type": "string", "deviceName": "string", "customFlexGroupName": ["string"], "customApGroupName": "string"}'"""])
    assert not result.exception
    assert is_valid_ap_provision(result)


def is_valid_delete_wireless_profile(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.wireless
def test_delete_wireless_profile(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.3', *auth_options,
                                 'wireless', 'delete-wireless-profile',
                                 """--wireless_profile_name='string'"""])
    assert not result.exception
    assert is_valid_delete_wireless_profile(result)


def is_valid_delete_ssid_and_provision_it_to_devices(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.wireless
def test_delete_ssid_and_provision_it_to_devices(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.3', *auth_options,
                                 'wireless', 'delete-ssid-and-provision-it-to-devices',
                                 """--managed_aplocations='string'""",
                                 """--ssid_name='string'"""])
    assert not result.exception
    assert is_valid_delete_ssid_and_provision_it_to_devices(result)
