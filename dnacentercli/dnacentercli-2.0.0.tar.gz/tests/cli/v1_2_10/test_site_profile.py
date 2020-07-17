# -*- coding: utf-8 -*-
"""DNACenterAPI Site Profile API fixtures and tests.

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


def is_valid_get_device_details_by_ip(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.site_profile
def test_get_device_details_by_ip(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'site-profile', 'get-device-details-by-ip',
                                 """--device_ip='string'"""])
    assert not result.exception
    assert is_valid_get_device_details_by_ip(result)


def is_valid_provision_nfv(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.site_profile
def test_provision_nfv(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'site-profile', 'provision-nfv',
                                 """--active_validation=True""",
                                 """--callbackurl='string'""",
                                 """--payload=None""",
                                 """--provisioning='{"site": {"siteProfileName": "string", "area": {"name": "string", "parentName": "string"}, "building": {"name": "string", "address": "string"}, "floor": {"name": "string", "parentName": "string"}}, "templateParam": {"nfvis": {"var1": "string"}, "asav": {"var1": "string"}}, "networksettings": {"ipPool": {"globalPool": {"name": "string"}}}, "device": [{"ip": "string", "deviceSerialNumber": "string", "tagName": "string", "serviceProviders": [{"serviceProvider": "string", "wanInterface": {"ipAddress": "string", "interfaceName": "string", "subnetmask": "string", "bandwidth": "string", "gateway": "string"}}], "services": [{"type": "string", "mode": "string", "systemIp": "string", "centralManagerIP": "string", "centralRegistrationKey": "string", "commonKey": "string", "adminPasswordHash": "string"}], "vlan": [{"type": "string", "id": "string", "interfaces": "string", "network": "string"}], "subPools": [{"type": "Lan", "name": "string", "ipSubnet": "string", "gateway": "string"}], "customNetworks": [{"name": "string", "port": "string", "ipAddressPool": "string"}]}]}'""",
                                 """--siteprofile='{"siteProfileName": "string", "device": [{"deviceType": "ENCS5100", "tagName": "string", "serviceProviders": [{"serviceProvider": "string", "linkType": "GigabitEthernet", "connect": true, "defaultGateway": true}], "dia": true, "services": [{"type": "isr", "profile": "string", "mode": "string"}], "customServices": [{"name": "string", "applicationType": "string", "profile": "string"}], "customNetworks": [{"name": "string", "servicesToConnect": [{"service": "string"}], "connectionType": "string", "networkMode": "string", "vlan": "string"}], "vlan": [{"type": "string", "id": "string"}]}], "customTemplate": [{"deviceType": "NFVIS", "template": "string"}]}'"""])
    assert not result.exception
    assert is_valid_provision_nfv(result)
