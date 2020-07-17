# -*- coding: utf-8 -*-
"""DNACenterAPI Site Design API fixtures and tests.

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


def is_valid_get_nfv_profile(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.site_design
def test_get_nfv_profile(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'site-design', 'get-nfv-profile',
                                 """--id='string'""",
                                 """--limit='string'""",
                                 """--name='string'""",
                                 """--offset='string'"""])
    assert not result.exception
    assert is_valid_get_nfv_profile(result)


def is_valid_update_nfv_profile(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.site_design
def test_update_nfv_profile(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'site-design', 'update-nfv-profile',
                                 """--active_validation=True""",
                                 """--device='{"deviceTag": "string", "directInternetAccessForFirewall": true, "services": [{"serviceType": "isr", "profileType": "ASAv5", "serviceName": "string", "imageName": "string", "vNicMapping": [{"networkType": "wan-net", "assignIpAddressToNetwork": "string"}], "firewallMode": "routed"}], "customNetworks": [{"networkName": "string", "servicesToConnect": [{"serviceName": "string"}], "connectionType": "wan-net", "vlanMode": "trunk", "vlanId": 0}], "vlanForL2": [{"vlanType": "access", "vlanId": 0, "vlanDescription": "string"}], "customTemplate": [{"deviceType": "Cisco 5400 Enterprise Network Compute System", "template": "string", "templateType": "Onboarding Template(s)"}], "currentDeviceTag": "string"}'""",
                                 """--id='string'""",
                                 """--name='string'""",
                                 """--payload=None"""])
    assert not result.exception
    assert is_valid_update_nfv_profile(result)


def is_valid_nfv_provisioning_detail(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.site_design
def test_nfv_provisioning_detail(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'site-design', 'nfv-provisioning-detail',
                                 """--active_validation=True""",
                                 """--device_ip='string'""",
                                 """--payload=None"""])
    assert not result.exception
    assert is_valid_nfv_provisioning_detail(result)


def is_valid_delete_nfv_profile(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.site_design
def test_delete_nfv_profile(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'site-design', 'delete-nfv-profile',
                                 """--id='string'""",
                                 """--name='string'"""])
    assert not result.exception
    assert is_valid_delete_nfv_profile(result)


def is_valid_create_nfv_profile(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.site_design
def test_create_nfv_profile(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'site-design', 'create-nfv-profile',
                                 """--active_validation=True""",
                                 """--device='{"deviceType": "Cisco 5400 Enterprise Network Compute System", "deviceTag": "string", "serviceProviderProfile": [{"serviceProvider": "string", "linkType": "GigabitEthernet", "connect": true, "connectDefaultGatewayOnWan": true}], "directInternetAccessForFirewall": true, "services": [{"serviceType": "isr", "profileType": "ASAv5", "serviceName": "string", "imageName": "string", "vNicMapping": [{"networkType": "wan-net", "assignIpAddressToNetwork": "string"}], "firewallMode": "routed"}], "customNetworks": [{"networkName": "string", "servicesToConnect": [{"serviceName": "string"}], "connectionType": "wan-net", "vlanMode": "trunk", "vlanId": 0}], "vlanForL2": [{"vlanType": "access", "vlanId": 0, "vlanDescription": "string"}], "customTemplate": [{"deviceType": "Cisco 5400 Enterprise Network Compute System", "template": "string", "templateType": "Onboarding Template(s)"}]}'""",
                                 """--payload=None""",
                                 """--profilename='string'"""])
    assert not result.exception
    assert is_valid_create_nfv_profile(result)


def is_valid_provision_nfv(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.site_design
def test_provision_nfv(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'site-design', 'provision-nfv',
                                 """--active_validation=True""",
                                 """--payload=None""",
                                 """--provisioning='{"site": {"siteProfileName": "string", "area": {"name": "string", "parentName": "string"}, "building": {"name": "string", "address": "string", "latitude": 0, "longitude": 0, "parentName": "string"}, "floor": {"name": "string", "parentName": "string", "rfModel": "string", "width": 0, "length": 0, "height": 0}}, "device": [{"ip": "string", "deviceSerialNumber": "string", "tagName": "string", "serviceProviders": [{"serviceProvider": "string", "wanInterface": {"ipAddress": "string", "interfaceName": "string", "subnetmask": "string", "bandwidth": "string", "gateway": "string"}}], "services": [{"type": "string", "mode": "string", "systemIp": "string", "centralManagerIP": "string", "centralRegistrationKey": "string", "commonKey": "string", "adminPasswordHash": "string", "disk": "string"}], "vlan": [{"type": "string", "id": "string", "interfaces": "string", "network": "string"}], "subPools": [{"type": "Lan", "name": "string", "ipSubnet": "string", "gateway": "string", "parentPoolName": "string"}], "customNetworks": [{"name": "string", "port": "string", "ipAddressPool": "string"}], "templateParam": {"nfvis": {"var1": "string"}, "asav": {"var1": "string"}}}]}'""",
                                 """--siteprofile='{"siteProfileName": "string", "device": [{"deviceType": "ENCS5100", "tagName": "string", "serviceProviders": [{"serviceProvider": "string", "linkType": "GigabitEthernet", "connect": true, "defaultGateway": true}], "dia": true, "services": [{"type": "isr", "profile": "string", "mode": "string", "name": "string", "imageName": "string", "topology": {"type": "string", "name": "string", "assignIp": "string"}}], "customServices": [{"name": "string", "applicationType": "string", "profile": "string", "topology": {"type": "string", "name": "string", "assignIp": "string"}, "imageName": "string"}], "customNetworks": [{"name": "string", "servicesToConnect": [{"service": "string"}], "connectionType": "string", "networkMode": "string", "vlan": "string"}], "vlan": [{"type": "string", "id": "string"}], "customTemplate": [{"deviceType": "NFVIS", "template": "string"}]}]}'"""])
    assert not result.exception
    assert is_valid_provision_nfv(result)


def is_valid_get_device_details_by_ip(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.site_design
def test_get_device_details_by_ip(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'site-design', 'get-device-details-by-ip',
                                 """--device_ip='string'"""])
    assert not result.exception
    assert is_valid_get_device_details_by_ip(result)
