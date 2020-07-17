# -*- coding: utf-8 -*-
"""DNACenterAPI Network Discovery API fixtures and tests.

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


def is_valid_get_count_of_all_discovery_jobs(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_get_count_of_all_discovery_jobs(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'get-count-of-all-discovery-jobs',
                                 """--"""])
    assert not result.exception
    assert is_valid_get_count_of_all_discovery_jobs(result)


def is_valid_update_snmp_write_community(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_update_snmp_write_community(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'update-snmp-write-community',
                                 """--active_validation=True""",
                                 """--comments='string'""",
                                 """--credentialtype='GLOBAL'""",
                                 """--description='string'""",
                                 """--id='string'""",
                                 """--instancetenantid='string'""",
                                 """--instanceuuid='string'""",
                                 """--payload=None""",
                                 """--writecommunity='string'"""])
    assert not result.exception
    assert is_valid_update_snmp_write_community(result)


def is_valid_update_snmpv3_credentials(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_update_snmpv3_credentials(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'update-snmpv3-credentials',
                                 """--active_validation=True""",
                                 """--authpassword='string'""",
                                 """--authtype='SHA'""",
                                 """--comments='string'""",
                                 """--credentialtype='GLOBAL'""",
                                 """--description='string'""",
                                 """--id='string'""",
                                 """--instancetenantid='string'""",
                                 """--instanceuuid='string'""",
                                 """--payload=None""",
                                 """--privacypassword='string'""",
                                 """--privacytype='DES'""",
                                 """--snmpmode='AUTHPRIV'""",
                                 """--username='string'"""])
    assert not result.exception
    assert is_valid_update_snmpv3_credentials(result)


def is_valid_get_network_devices_from_discovery(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_get_network_devices_from_discovery(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'get-network-devices-from-discovery',
                                 """--cli_status='value1,value2'""",
                                 """--http_status='value1,value2'""",
                                 """--id='string'""",
                                 """--ip_address='value1,value2'""",
                                 """--netconf_status='value1,value2'""",
                                 """--ping_status='value1,value2'""",
                                 """--snmp_status='value1,value2'""",
                                 """--sort_by='string'""",
                                 """--sort_order='string'""",
                                 """--task_id='string'"""])
    assert not result.exception
    assert is_valid_get_network_devices_from_discovery(result)


def is_valid_get_snmp_properties(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_get_snmp_properties(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'get-snmp-properties',
                                 """--"""])
    assert not result.exception
    assert is_valid_get_snmp_properties(result)


def is_valid_get_discoveries_by_range(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_get_discoveries_by_range(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'get-discoveries-by-range',
                                 """--records_to_return=0""",
                                 """--start_index=0"""])
    assert not result.exception
    assert is_valid_get_discoveries_by_range(result)


def is_valid_delete_discovery_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_delete_discovery_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'delete-discovery-by-id',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_delete_discovery_by_id(result)


def is_valid_update_snmp_read_community(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_update_snmp_read_community(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'update-snmp-read-community',
                                 """--active_validation=True""",
                                 """--comments='string'""",
                                 """--credentialtype='GLOBAL'""",
                                 """--description='string'""",
                                 """--id='string'""",
                                 """--instancetenantid='string'""",
                                 """--instanceuuid='string'""",
                                 """--payload=None""",
                                 """--readcommunity='string'"""])
    assert not result.exception
    assert is_valid_update_snmp_read_community(result)


def is_valid_get_credential_sub_type_by_credential_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_get_credential_sub_type_by_credential_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'get-credential-sub-type-by-credential-id',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_get_credential_sub_type_by_credential_id(result)


def is_valid_start_discovery(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_start_discovery(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'start-discovery',
                                 """--active_validation=True""",
                                 """--cdplevel=0""",
                                 """--discoverytype='string'""",
                                 """--enablepasswordlist='string'""",
                                 """--globalcredentialidlist='string'""",
                                 """--httpreadcredential='{"comments": "string", "credentialType": "GLOBAL", "description": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "password": "string", "port": 0, "secure": true, "username": "string"}'""",
                                 """--httpwritecredential='{"comments": "string", "credentialType": "GLOBAL", "description": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "password": "string", "port": 0, "secure": true, "username": "string"}'""",
                                 """--ipaddresslist='string'""",
                                 """--ipfilterlist='string'""",
                                 """--lldplevel=0""",
                                 """--name='string'""",
                                 """--netconfport='string'""",
                                 """--noaddnewdevice=True""",
                                 """--parentdiscoveryid='string'""",
                                 """--passwordlist='string'""",
                                 """--payload=None""",
                                 """--preferredmgmtipmethod='string'""",
                                 """--protocolorder='string'""",
                                 """--rediscovery=True""",
                                 """--retry=0""",
                                 """--snmpauthpassphrase='string'""",
                                 """--snmpauthprotocol='string'""",
                                 """--snmpmode='string'""",
                                 """--snmpprivpassphrase='string'""",
                                 """--snmpprivprotocol='string'""",
                                 """--snmprocommunity='string'""",
                                 """--snmprocommunitydesc='string'""",
                                 """--snmprwcommunity='string'""",
                                 """--snmprwcommunitydesc='string'""",
                                 """--snmpusername='string'""",
                                 """--snmpversion='string'""",
                                 """--timeout=0""",
                                 """--updatemgmtip=True""",
                                 """--usernamelist='string'"""])
    assert not result.exception
    assert is_valid_start_discovery(result)


def is_valid_update_global_credentials(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_update_global_credentials(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'update-global-credentials',
                                 """--active_validation=True""",
                                 """--global_credential_id='string'""",
                                 """--payload=None""",
                                 """--siteuuids='string'"""])
    assert not result.exception
    assert is_valid_update_global_credentials(result)


def is_valid_get_discovery_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_get_discovery_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'get-discovery-by-id',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_get_discovery_by_id(result)


def is_valid_create_snmp_read_community(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_create_snmp_read_community(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'create-snmp-read-community',
                                 """--active_validation=True""",
                                 """--payload='{"comments": "string", "credentialType": "GLOBAL", "description": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "readCommunity": "string"}'"""])
    assert not result.exception
    assert is_valid_create_snmp_read_community(result)


def is_valid_create_snmp_write_community(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_create_snmp_write_community(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'create-snmp-write-community',
                                 """--active_validation=True""",
                                 """--payload='{"comments": "string", "credentialType": "GLOBAL", "description": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "writeCommunity": "string"}'"""])
    assert not result.exception
    assert is_valid_create_snmp_write_community(result)


def is_valid_update_http_read_credential(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_update_http_read_credential(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'update-http-read-credential',
                                 """--active_validation=True""",
                                 """--comments='string'""",
                                 """--credentialtype='GLOBAL'""",
                                 """--description='string'""",
                                 """--id='string'""",
                                 """--instancetenantid='string'""",
                                 """--instanceuuid='string'""",
                                 """--password='string'""",
                                 """--payload=None""",
                                 """--port=0""",
                                 """--secure=True""",
                                 """--username='string'"""])
    assert not result.exception
    assert is_valid_update_http_read_credential(result)


def is_valid_updates_discovery_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_updates_discovery_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'updates-discovery-by-id',
                                 """--active_validation=True""",
                                 """--attributeinfo='{}'""",
                                 """--cdplevel=0""",
                                 """--deviceids='string'""",
                                 """--discoverycondition='string'""",
                                 """--discoverystatus='string'""",
                                 """--discoverytype='string'""",
                                 """--enablepasswordlist='string'""",
                                 """--globalcredentialidlist='string'""",
                                 """--httpreadcredential='{"comments": "string", "credentialType": "GLOBAL", "description": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "password": "string", "port": 0, "secure": true, "username": "string"}'""",
                                 """--httpwritecredential='{"comments": "string", "credentialType": "GLOBAL", "description": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "password": "string", "port": 0, "secure": true, "username": "string"}'""",
                                 """--id='string'""",
                                 """--ipaddresslist='string'""",
                                 """--ipfilterlist='string'""",
                                 """--isautocdp=True""",
                                 """--lldplevel=0""",
                                 """--name='string'""",
                                 """--netconfport='string'""",
                                 """--numdevices=0""",
                                 """--parentdiscoveryid='string'""",
                                 """--passwordlist='string'""",
                                 """--payload=None""",
                                 """--preferredmgmtipmethod='string'""",
                                 """--protocolorder='string'""",
                                 """--retrycount=0""",
                                 """--snmpauthpassphrase='string'""",
                                 """--snmpauthprotocol='string'""",
                                 """--snmpmode='string'""",
                                 """--snmpprivpassphrase='string'""",
                                 """--snmpprivprotocol='string'""",
                                 """--snmprocommunity='string'""",
                                 """--snmprocommunitydesc='string'""",
                                 """--snmprwcommunity='string'""",
                                 """--snmprwcommunitydesc='string'""",
                                 """--snmpusername='string'""",
                                 """--timeout=0""",
                                 """--updatemgmtip=True""",
                                 """--usernamelist='string'"""])
    assert not result.exception
    assert is_valid_updates_discovery_by_id(result)


def is_valid_create_update_snmp_properties(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_create_update_snmp_properties(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'create-update-snmp-properties',
                                 """--active_validation=True""",
                                 """--payload='{"id": "string", "instanceTenantId": "string", "instanceUuid": "string", "intValue": 0, "systemPropertyName": "string"}'"""])
    assert not result.exception
    assert is_valid_create_update_snmp_properties(result)


def is_valid_create_cli_credentials(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_create_cli_credentials(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'create-cli-credentials',
                                 """--active_validation=True""",
                                 """--payload='{"comments": "string", "credentialType": "GLOBAL", "description": "string", "enablePassword": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "password": "string", "username": "string"}'"""])
    assert not result.exception
    assert is_valid_create_cli_credentials(result)


def is_valid_update_http_write_credentials(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_update_http_write_credentials(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'update-http-write-credentials',
                                 """--active_validation=True""",
                                 """--comments='string'""",
                                 """--credentialtype='GLOBAL'""",
                                 """--description='string'""",
                                 """--id='string'""",
                                 """--instancetenantid='string'""",
                                 """--instanceuuid='string'""",
                                 """--password='string'""",
                                 """--payload=None""",
                                 """--port=0""",
                                 """--secure=True""",
                                 """--username='string'"""])
    assert not result.exception
    assert is_valid_update_http_write_credentials(result)


def is_valid_get_discovery_jobs_by_ip(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_get_discovery_jobs_by_ip(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'get-discovery-jobs-by-ip',
                                 """--ip_address='string'""",
                                 """--limit=0""",
                                 """--name='string'""",
                                 """--offset=0"""])
    assert not result.exception
    assert is_valid_get_discovery_jobs_by_ip(result)


def is_valid_create_snmpv3_credentials(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_create_snmpv3_credentials(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'create-snmpv3-credentials',
                                 """--active_validation=True""",
                                 """--payload='{"authPassword": "string", "authType": "SHA", "comments": "string", "credentialType": "GLOBAL", "description": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "privacyPassword": "string", "privacyType": "DES", "snmpMode": "AUTHPRIV", "username": "string"}'"""])
    assert not result.exception
    assert is_valid_create_snmpv3_credentials(result)


def is_valid_get_devices_discovered_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_get_devices_discovered_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'get-devices-discovered-by-id',
                                 """--id='string'""",
                                 """--task_id='string'"""])
    assert not result.exception
    assert is_valid_get_devices_discovered_by_id(result)


def is_valid_delete_all_discovery(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_delete_all_discovery(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'delete-all-discovery',
                                 """--"""])
    assert not result.exception
    assert is_valid_delete_all_discovery(result)


def is_valid_update_cli_credentials(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_update_cli_credentials(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'update-cli-credentials',
                                 """--active_validation=True""",
                                 """--comments='string'""",
                                 """--credentialtype='GLOBAL'""",
                                 """--description='string'""",
                                 """--enablepassword='string'""",
                                 """--id='string'""",
                                 """--instancetenantid='string'""",
                                 """--instanceuuid='string'""",
                                 """--password='string'""",
                                 """--payload=None""",
                                 """--username='string'"""])
    assert not result.exception
    assert is_valid_update_cli_credentials(result)


def is_valid_create_netconf_credentials(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_create_netconf_credentials(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'create-netconf-credentials',
                                 """--active_validation=True""",
                                 """--payload='{"comments": "string", "credentialType": "GLOBAL", "description": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "netconfPort": "string"}'"""])
    assert not result.exception
    assert is_valid_create_netconf_credentials(result)


def is_valid_create_http_write_credentials(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_create_http_write_credentials(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'create-http-write-credentials',
                                 """--active_validation=True""",
                                 """--payload='{"comments": "string", "credentialType": "GLOBAL", "description": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "password": "string", "port": 0, "secure": true, "username": "string"}'"""])
    assert not result.exception
    assert is_valid_create_http_write_credentials(result)


def is_valid_get_list_of_discoveries_by_discovery_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_get_list_of_discoveries_by_discovery_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'get-list-of-discoveries-by-discovery-id',
                                 """--id='string'""",
                                 """--ip_address='string'""",
                                 """--limit=0""",
                                 """--offset=0"""])
    assert not result.exception
    assert is_valid_get_list_of_discoveries_by_discovery_id(result)


def is_valid_get_discovered_devices_by_range(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_get_discovered_devices_by_range(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'get-discovered-devices-by-range',
                                 """--id='string'""",
                                 """--records_to_return=0""",
                                 """--start_index=0""",
                                 """--task_id='string'"""])
    assert not result.exception
    assert is_valid_get_discovered_devices_by_range(result)


def is_valid_create_http_read_credentials(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_create_http_read_credentials(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'create-http-read-credentials',
                                 """--active_validation=True""",
                                 """--payload='{"comments": "string", "credentialType": "GLOBAL", "description": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "password": "string", "port": 0, "secure": true, "username": "string"}'"""])
    assert not result.exception
    assert is_valid_create_http_read_credentials(result)


def is_valid_update_netconf_credentials(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_update_netconf_credentials(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'update-netconf-credentials',
                                 """--active_validation=True""",
                                 """--comments='string'""",
                                 """--credentialtype='GLOBAL'""",
                                 """--description='string'""",
                                 """--id='string'""",
                                 """--instancetenantid='string'""",
                                 """--instanceuuid='string'""",
                                 """--netconfport='string'""",
                                 """--payload=None"""])
    assert not result.exception
    assert is_valid_update_netconf_credentials(result)


def is_valid_delete_global_credentials_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_delete_global_credentials_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'delete-global-credentials-by-id',
                                 """--global_credential_id='string'"""])
    assert not result.exception
    assert is_valid_delete_global_credentials_by_id(result)


def is_valid_delete_discovery_by_specified_range(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_delete_discovery_by_specified_range(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'delete-discovery-by-specified-range',
                                 """--records_to_delete=0""",
                                 """--start_index=0"""])
    assert not result.exception
    assert is_valid_delete_discovery_by_specified_range(result)


def is_valid_get_discovered_network_devices_by_discovery_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_get_discovered_network_devices_by_discovery_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'get-discovered-network-devices-by-discovery-id',
                                 """--id='string'""",
                                 """--task_id='string'"""])
    assert not result.exception
    assert is_valid_get_discovered_network_devices_by_discovery_id(result)


def is_valid_get_global_credentials(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.network_discovery
def test_get_global_credentials(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.1', *auth_options,
                                 'network-discovery', 'get-global-credentials',
                                 """--credential_sub_type='string'""",
                                 """--order='string'""",
                                 """--sort_by='string'"""])
    assert not result.exception
    assert is_valid_get_global_credentials(result)
