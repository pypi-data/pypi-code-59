# -*- coding: utf-8 -*-
"""DNACenterAPI Devices API fixtures and tests.

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


def is_valid_get_module_info_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_module_info_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-module-info-by-id',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_get_module_info_by_id(result)


def is_valid_get_device_interface_count(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_device_interface_count(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-device-interface-count',
                                 """--"""])
    assert not result.exception
    assert is_valid_get_device_interface_count(result)


def is_valid_sync_devices_using_forcesync(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_sync_devices_using_forcesync(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'sync-devices-using-forcesync',
                                 """--active_validation=True""",
                                 """--force_sync=True""",
                                 """--payload='{}'"""])
    assert not result.exception
    assert is_valid_sync_devices_using_forcesync(result)


def is_valid_get_device_list(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_device_list(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-device-list',
                                 """--associated_wlc_ip='value1,value2'""",
                                 """--collection_interval='value1,value2'""",
                                 """--collection_status='value1,value2'""",
                                 """--error_code='value1,value2'""",
                                 """--error_description='value1,value2'""",
                                 """--family='value1,value2'""",
                                 """--hostname='value1,value2'""",
                                 """--id='string'""",
                                 """--license_name='value1,value2'""",
                                 """--license_status='value1,value2'""",
                                 """--license_type='value1,value2'""",
                                 """--location='value1,value2'""",
                                 """--location_name='value1,value2'""",
                                 """--mac_address='value1,value2'""",
                                 """--management_ip_address='value1,value2'""",
                                 """--module_equpimenttype='value1,value2'""",
                                 """--module_name='value1,value2'""",
                                 """--module_operationstatecode='value1,value2'""",
                                 """--module_partnumber='value1,value2'""",
                                 """--module_servicestate='value1,value2'""",
                                 """--module_vendorequipmenttype='value1,value2'""",
                                 """--not_synced_for_minutes='value1,value2'""",
                                 """--platform_id='value1,value2'""",
                                 """--reachability_status='value1,value2'""",
                                 """--role='value1,value2'""",
                                 """--serial_number='value1,value2'""",
                                 """--series='value1,value2'""",
                                 """--software_type='value1,value2'""",
                                 """--software_version='value1,value2'""",
                                 """--type='value1,value2'""",
                                 """--up_time='value1,value2'"""])
    assert not result.exception
    assert is_valid_get_device_list(result)


def is_valid_get_polling_interval_for_all_devices(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_polling_interval_for_all_devices(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-polling-interval-for-all-devices',
                                 """--"""])
    assert not result.exception
    assert is_valid_get_polling_interval_for_all_devices(result)


def is_valid_get_device_count(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_device_count(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-device-count',
                                 """--"""])
    assert not result.exception
    assert is_valid_get_device_count(result)


def is_valid_get_device_interface_vlans(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_device_interface_vlans(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-device-interface-vlans',
                                 """--id='string'""",
                                 """--interface_type='string'"""])
    assert not result.exception
    assert is_valid_get_device_interface_vlans(result)


def is_valid_get_device_interfaces_by_specified_range(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_device_interfaces_by_specified_range(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-device-interfaces-by-specified-range',
                                 """--device_id='string'""",
                                 """--records_to_return=0""",
                                 """--start_index=0"""])
    assert not result.exception
    assert is_valid_get_device_interfaces_by_specified_range(result)


def is_valid_delete_device_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_delete_device_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'delete-device-by-id',
                                 """--id='string'""",
                                 """--is_force_delete=True"""])
    assert not result.exception
    assert is_valid_delete_device_by_id(result)


def is_valid_get_device_config_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_device_config_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-device-config-by-id',
                                 """--network_device_id='string'"""])
    assert not result.exception
    assert is_valid_get_device_config_by_id(result)


def is_valid_add_device(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_add_device(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'add-device',
                                 """--active_validation=True""",
                                 """--clitransport='string'""",
                                 """--computedevice=True""",
                                 """--enablepassword='string'""",
                                 """--extendeddiscoveryinfo='string'""",
                                 """--httppassword='string'""",
                                 """--httpport='string'""",
                                 """--httpsecure=True""",
                                 """--httpusername='string'""",
                                 """--ipaddress='string'""",
                                 """--merakiorgid='string'""",
                                 """--netconfport='string'""",
                                 """--password='string'""",
                                 """--payload=None""",
                                 """--serialnumber='string'""",
                                 """--snmpauthpassphrase='string'""",
                                 """--snmpauthprotocol='string'""",
                                 """--snmpmode='string'""",
                                 """--snmpprivpassphrase='string'""",
                                 """--snmpprivprotocol='string'""",
                                 """--snmprocommunity='string'""",
                                 """--snmprwcommunity='string'""",
                                 """--snmpretry=0""",
                                 """--snmptimeout=0""",
                                 """--snmpusername='string'""",
                                 """--snmpversion='string'""",
                                 """--type='COMPUTE_DEVICE'""",
                                 """--updatemgmtipaddresslist='{"existMgmtIpAddress": "string", "newMgmtIpAddress": "string"}'""",
                                 """--username='string'"""])
    assert not result.exception
    assert is_valid_add_device(result)


def is_valid_get_device_config_count(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_device_config_count(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-device-config-count',
                                 """--"""])
    assert not result.exception
    assert is_valid_get_device_config_count(result)


def is_valid_get_interface_details(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_interface_details(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-interface-details',
                                 """--device_id='string'""",
                                 """--name='string'"""])
    assert not result.exception
    assert is_valid_get_interface_details(result)


def is_valid_get_polling_interval_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_polling_interval_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-polling-interval-by-id',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_get_polling_interval_by_id(result)


def is_valid_get_module_count(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_module_count(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-module-count',
                                 """--device_id='string'""",
                                 """--name_list='value1,value2'""",
                                 """--operational_state_code_list='value1,value2'""",
                                 """--part_number_list='value1,value2'""",
                                 """--vendor_equipment_type_list='value1,value2'"""])
    assert not result.exception
    assert is_valid_get_module_count(result)


def is_valid_get_device_interface_count_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_device_interface_count_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-device-interface-count-by-id',
                                 """--device_id='string'"""])
    assert not result.exception
    assert is_valid_get_device_interface_count_by_id(result)


def is_valid_get_organization_list_for_meraki(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_organization_list_for_meraki(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-organization-list-for-meraki',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_get_organization_list_for_meraki(result)


def is_valid_get_ospf_interfaces(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_ospf_interfaces(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-ospf-interfaces',
                                 """--"""])
    assert not result.exception
    assert is_valid_get_ospf_interfaces(result)


def is_valid_get_functional_capability_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_functional_capability_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-functional-capability-by-id',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_get_functional_capability_by_id(result)


def is_valid_get_isis_interfaces(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_isis_interfaces(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-isis-interfaces',
                                 """--"""])
    assert not result.exception
    assert is_valid_get_isis_interfaces(result)


def is_valid_get_device_config_for_all_devices(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_device_config_for_all_devices(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-device-config-for-all-devices',
                                 """--"""])
    assert not result.exception
    assert is_valid_get_device_config_for_all_devices(result)


def is_valid_update_device_role(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_update_device_role(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'update-device-role',
                                 """--active_validation=True""",
                                 """--id='string'""",
                                 """--payload=None""",
                                 """--role='string'""",
                                 """--rolesource='string'"""])
    assert not result.exception
    assert is_valid_update_device_role(result)


def is_valid_get_interface_info_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_interface_info_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-interface-info-by-id',
                                 """--device_id='string'"""])
    assert not result.exception
    assert is_valid_get_interface_info_by_id(result)


def is_valid_get_interface_by_ip(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_interface_by_ip(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-interface-by-ip',
                                 """--ip_address='string'"""])
    assert not result.exception
    assert is_valid_get_interface_by_ip(result)


def is_valid_get_network_device_by_ip(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_network_device_by_ip(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-network-device-by-ip',
                                 """--ip_address='string'"""])
    assert not result.exception
    assert is_valid_get_network_device_by_ip(result)


def is_valid_get_device_summary(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_device_summary(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-device-summary',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_get_device_summary(result)


def is_valid_get_device_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_device_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-device-by-id',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_get_device_by_id(result)


def is_valid_get_all_interfaces(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_all_interfaces(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-all-interfaces',
                                 """--limit=500""",
                                 """--offset=1"""])
    assert not result.exception
    assert is_valid_get_all_interfaces(result)


def is_valid_sync_devices(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_sync_devices(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'sync-devices',
                                 """--active_validation=True""",
                                 """--clitransport='string'""",
                                 """--computedevice=True""",
                                 """--enablepassword='string'""",
                                 """--extendeddiscoveryinfo='string'""",
                                 """--httppassword='string'""",
                                 """--httpport='string'""",
                                 """--httpsecure=True""",
                                 """--httpusername='string'""",
                                 """--ipaddress='string'""",
                                 """--merakiorgid='string'""",
                                 """--netconfport='string'""",
                                 """--password='string'""",
                                 """--payload=None""",
                                 """--serialnumber='string'""",
                                 """--snmpauthpassphrase='string'""",
                                 """--snmpauthprotocol='string'""",
                                 """--snmpmode='string'""",
                                 """--snmpprivpassphrase='string'""",
                                 """--snmpprivprotocol='string'""",
                                 """--snmprocommunity='string'""",
                                 """--snmprwcommunity='string'""",
                                 """--snmpretry=0""",
                                 """--snmptimeout=0""",
                                 """--snmpusername='string'""",
                                 """--snmpversion='string'""",
                                 """--type='COMPUTE_DEVICE'""",
                                 """--updatemgmtipaddresslist='{"existMgmtIpAddress": "string", "newMgmtIpAddress": "string"}'""",
                                 """--username='string'"""])
    assert not result.exception
    assert is_valid_sync_devices(result)


def is_valid_get_interface_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_interface_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-interface-by-id',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_get_interface_by_id(result)


def is_valid_get_functional_capability_for_devices(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_functional_capability_for_devices(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-functional-capability-for-devices',
                                 """--device_id='string'""",
                                 """--function_name='value1,value2'"""])
    assert not result.exception
    assert is_valid_get_functional_capability_for_devices(result)


def is_valid_register_device_for_wsa(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_register_device_for_wsa(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'register-device-for-wsa',
                                 """--macaddress='string'""",
                                 """--serial_number='string'"""])
    assert not result.exception
    assert is_valid_register_device_for_wsa(result)


def is_valid_get_device_by_serial_number(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_device_by_serial_number(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-device-by-serial-number',
                                 """--serial_number='string'"""])
    assert not result.exception
    assert is_valid_get_device_by_serial_number(result)


def is_valid_export_device_list(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_export_device_list(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'export-device-list',
                                 """--active_validation=True""",
                                 """--deviceuuids='string'""",
                                 """--id='string'""",
                                 """--operationenum='CREDENTIALDETAILS'""",
                                 """--parameters='string'""",
                                 """--password='string'""",
                                 """--payload=None"""])
    assert not result.exception
    assert is_valid_export_device_list(result)


def is_valid_get_network_device_by_pagination_range(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_network_device_by_pagination_range(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-network-device-by-pagination-range',
                                 """--records_to_return=0""",
                                 """--start_index=0"""])
    assert not result.exception
    assert is_valid_get_network_device_by_pagination_range(result)


def is_valid_retrieves_all_network_devices(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_retrieves_all_network_devices(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'retrieves-all-network-devices',
                                 """--associated_wlc_ip='string'""",
                                 """--collection_interval='string'""",
                                 """--collection_status='string'""",
                                 """--error_code='string'""",
                                 """--family='string'""",
                                 """--hostname='string'""",
                                 """--limit='string'""",
                                 """--mac_address='string'""",
                                 """--management_ip_address='string'""",
                                 """--offset='string'""",
                                 """--platform_id='string'""",
                                 """--reachability_failure_reason='string'""",
                                 """--reachability_status='string'""",
                                 """--role='string'""",
                                 """--role_source='string'""",
                                 """--serial_number='string'""",
                                 """--series='string'""",
                                 """--software_type='string'""",
                                 """--software_version='string'""",
                                 """--type='string'""",
                                 """--up_time='string'""",
                                 """--vrf_name='string'"""])
    assert not result.exception
    assert is_valid_retrieves_all_network_devices(result)


def is_valid_get_modules(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_modules(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-modules',
                                 """--device_id='string'""",
                                 """--limit='string'""",
                                 """--name_list='value1,value2'""",
                                 """--offset='string'""",
                                 """--operational_state_code_list='value1,value2'""",
                                 """--part_number_list='value1,value2'""",
                                 """--vendor_equipment_type_list='value1,value2'"""])
    assert not result.exception
    assert is_valid_get_modules(result)


def is_valid_get_wireless_lan_controller_details_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_wireless_lan_controller_details_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-wireless-lan-controller-details-by-id',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_get_wireless_lan_controller_details_by_id(result)


def is_valid_get_device_detail(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.devices
def test_get_device_detail(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.2.10', *auth_options,
                                 'devices', 'get-device-detail',
                                 """--identifier='string'""",
                                 """--search_by='string'""",
                                 """--timestamp=0"""])
    assert not result.exception
    assert is_valid_get_device_detail(result)
