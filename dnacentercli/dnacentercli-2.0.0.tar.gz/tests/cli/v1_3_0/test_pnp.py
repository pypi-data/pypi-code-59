# -*- coding: utf-8 -*-
"""DNACenterAPI PnP API fixtures and tests.

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


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.3.0', reason='version does not match')


def is_valid_un_claim_device(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_un_claim_device(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'un-claim-device',
                                 """--active_validation=True""",
                                 """--deviceidlist='string'""",
                                 """--payload=None"""])
    assert not result.exception
    assert is_valid_un_claim_device(result)


def is_valid_get_sync_result_for_virtual_account(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_get_sync_result_for_virtual_account(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'get-sync-result-for-virtual-account',
                                 """--domain='string'""",
                                 """--name='string'"""])
    assert not result.exception
    assert is_valid_get_sync_result_for_virtual_account(result)


def is_valid_update_device(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_update_device(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'update-device',
                                 """--_id='string'""",
                                 """--active_validation=True""",
                                 """--deviceinfo='{"aaaCredentials": {"password": "string", "username": "string"}, "addedOn": 0, "addnMacAddrs": ["string"], "agentType": "POSIX", "authStatus": "string", "authenticatedSudiSerialNo": "string", "capabilitiesSupported": ["string"], "cmState": "NotContacted", "description": "string", "deviceSudiSerialNos": ["string"], "deviceType": "string", "featuresSupported": ["string"], "fileSystemList": [{"freespace": 0, "name": "string", "readable": true, "size": 0, "type": "string", "writeable": true}], "firstContact": 0, "hostname": "string", "httpHeaders": [{"key": "string", "value": "string"}], "imageFile": "string", "imageVersion": "string", "ipInterfaces": [{"ipv4Address": {}, "ipv6AddressList": [{}], "macAddress": "string", "name": "string", "status": "string"}], "lastContact": 0, "lastSyncTime": 0, "lastUpdateOn": 0, "location": {"address": "string", "altitude": "string", "latitude": "string", "longitude": "string", "siteId": "string"}, "macAddress": "string", "mode": "string", "name": "string", "neighborLinks": [{"localInterfaceName": "string", "localMacAddress": "string", "localShortInterfaceName": "string", "remoteDeviceName": "string", "remoteInterfaceName": "string", "remoteMacAddress": "string", "remotePlatform": "string", "remoteShortInterfaceName": "string", "remoteVersion": "string"}], "onbState": "NotContacted", "pid": "string", "pnpProfileList": [{"createdBy": "string", "discoveryCreated": true, "primaryEndpoint": {"certificate": "string", "fqdn": "string", "ipv4Address": {}, "ipv6Address": {}, "port": 0, "protocol": "string"}, "profileName": "string", "secondaryEndpoint": {"certificate": "string", "fqdn": "string", "ipv4Address": {}, "ipv6Address": {}, "port": 0, "protocol": "string"}}], "populateInventory": true, "preWorkflowCliOuputs": [{"cli": "string", "cliOutput": "string"}], "projectId": "string", "projectName": "string", "reloadRequested": true, "serialNumber": "string", "smartAccountId": "string", "source": "string", "stack": true, "stackInfo": {"isFullRing": true, "stackMemberList": [{"hardwareVersion": "string", "licenseLevel": "string", "licenseType": "string", "macAddress": "string", "pid": "string", "priority": 0, "role": "string", "serialNumber": "string", "softwareVersion": "string", "stackNumber": 0, "state": "string", "sudiSerialNumber": "string"}], "stackRingProtocol": "string", "supportsStackWorkflows": true, "totalMemberCount": 0, "validLicenseLevels": ["string"]}, "state": "Unclaimed", "sudiRequired": true, "tags": {}, "userSudiSerialNos": ["string"], "virtualAccountId": "string", "workflowId": "string", "workflowName": "string"}'""",
                                 """--id='string'""",
                                 """--payload=None""",
                                 """--runsummarylist='{"details": "string", "errorFlag": true, "historyTaskInfo": {"addnDetails": [{"key": "string", "value": "string"}], "name": "string", "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}, "timestamp": 0}'""",
                                 """--systemresetworkflow='{"_id": "string", "addToInventory": true, "addedOn": 0, "configId": "string", "currTaskIdx": 0, "description": "string", "endTime": 0, "execTime": 0, "imageId": "string", "instanceType": "SystemWorkflow", "lastupdateOn": 0, "name": "string", "startTime": 0, "state": "string", "tasks": [{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}], "tenantId": "string", "type": "string", "useState": "string", "version": 0}'""",
                                 """--systemworkflow='{"_id": "string", "addToInventory": true, "addedOn": 0, "configId": "string", "currTaskIdx": 0, "description": "string", "endTime": 0, "execTime": 0, "imageId": "string", "instanceType": "SystemWorkflow", "lastupdateOn": 0, "name": "string", "startTime": 0, "state": "string", "tasks": [{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}], "tenantId": "string", "type": "string", "useState": "string", "version": 0}'""",
                                 """--tenantid='string'""",
                                 """--version=0""",
                                 """--workflow='{"_id": "string", "addToInventory": true, "addedOn": 0, "configId": "string", "currTaskIdx": 0, "description": "string", "endTime": 0, "execTime": 0, "imageId": "string", "instanceType": "SystemWorkflow", "lastupdateOn": 0, "name": "string", "startTime": 0, "state": "string", "tasks": [{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}], "tenantId": "string", "type": "string", "useState": "string", "version": 0}'""",
                                 """--workflowparameters='{"configList": [{"configId": "string", "configParameters": [{"key": "string", "value": "string"}]}], "licenseLevel": "string", "licenseType": "string", "topOfStackSerialNumber": "string"}'"""])
    assert not result.exception
    assert is_valid_update_device(result)


def is_valid_deregister_virtual_account(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_deregister_virtual_account(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'deregister-virtual-account',
                                 """--domain='string'""",
                                 """--name='string'"""])
    assert not result.exception
    assert is_valid_deregister_virtual_account(result)


def is_valid_add_virtual_account(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_add_virtual_account(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'add-virtual-account',
                                 """--active_validation=True""",
                                 """--autosyncperiod=0""",
                                 """--ccouser='string'""",
                                 """--expiry=0""",
                                 """--lastsync=0""",
                                 """--payload=None""",
                                 """--profile='{"addressFqdn": "string", "addressIpV4": "string", "cert": "string", "makeDefault": true, "name": "string", "port": 0, "profileId": "string", "proxy": true}'""",
                                 """--smartaccountid='string'""",
                                 """--syncresult='{"syncList": [{"deviceSnList": ["string"], "syncType": "Add"}], "syncMsg": "string"}'""",
                                 """--syncresultstr='string'""",
                                 """--syncstarttime=0""",
                                 """--syncstatus='NOT_SYNCED'""",
                                 """--tenantid='string'""",
                                 """--token='string'""",
                                 """--virtualaccountid='string'"""])
    assert not result.exception
    assert is_valid_add_virtual_account(result)


def is_valid_import_devices_in_bulk(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_import_devices_in_bulk(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'import-devices-in-bulk',
                                 """--active_validation=True""",
                                 """--payload='{"_id": "string", "deviceInfo": {"aaaCredentials": {"password": "string", "username": "string"}, "addedOn": 0, "addnMacAddrs": ["string"], "agentType": "POSIX", "authStatus": "string", "authenticatedSudiSerialNo": "string", "capabilitiesSupported": ["string"], "cmState": "NotContacted", "description": "string", "deviceSudiSerialNos": ["string"], "deviceType": "string", "featuresSupported": ["string"], "fileSystemList": [{"freespace": 0, "name": "string", "readable": true, "size": 0, "type": "string", "writeable": true}], "firstContact": 0, "hostname": "string", "httpHeaders": [{"key": "string", "value": "string"}], "imageFile": "string", "imageVersion": "string", "ipInterfaces": [{"ipv4Address": {}, "ipv6AddressList": [{}], "macAddress": "string", "name": "string", "status": "string"}], "lastContact": 0, "lastSyncTime": 0, "lastUpdateOn": 0, "location": {"address": "string", "altitude": "string", "latitude": "string", "longitude": "string", "siteId": "string"}, "macAddress": "string", "mode": "string", "name": "string", "neighborLinks": [{"localInterfaceName": "string", "localMacAddress": "string", "localShortInterfaceName": "string", "remoteDeviceName": "string", "remoteInterfaceName": "string", "remoteMacAddress": "string", "remotePlatform": "string", "remoteShortInterfaceName": "string", "remoteVersion": "string"}], "onbState": "NotContacted", "pid": "string", "pnpProfileList": [{"createdBy": "string", "discoveryCreated": true, "primaryEndpoint": {"certificate": "string", "fqdn": "string", "ipv4Address": {}, "ipv6Address": {}, "port": 0, "protocol": "string"}, "profileName": "string", "secondaryEndpoint": {"certificate": "string", "fqdn": "string", "ipv4Address": {}, "ipv6Address": {}, "port": 0, "protocol": "string"}}], "populateInventory": true, "preWorkflowCliOuputs": [{"cli": "string", "cliOutput": "string"}], "projectId": "string", "projectName": "string", "reloadRequested": true, "serialNumber": "string", "smartAccountId": "string", "source": "string", "stack": true, "stackInfo": {"isFullRing": true, "stackMemberList": [{"hardwareVersion": "string", "licenseLevel": "string", "licenseType": "string", "macAddress": "string", "pid": "string", "priority": 0, "role": "string", "serialNumber": "string", "softwareVersion": "string", "stackNumber": 0, "state": "string", "sudiSerialNumber": "string"}], "stackRingProtocol": "string", "supportsStackWorkflows": true, "totalMemberCount": 0, "validLicenseLevels": ["string"]}, "state": "Unclaimed", "sudiRequired": true, "tags": {}, "userSudiSerialNos": ["string"], "virtualAccountId": "string", "workflowId": "string", "workflowName": "string"}, "runSummaryList": [{"details": "string", "errorFlag": true, "historyTaskInfo": {"addnDetails": [{"key": "string", "value": "string"}], "name": "string", "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}, "timestamp": 0}], "systemResetWorkflow": {"_id": "string", "addToInventory": true, "addedOn": 0, "configId": "string", "currTaskIdx": 0, "description": "string", "endTime": 0, "execTime": 0, "imageId": "string", "instanceType": "SystemWorkflow", "lastupdateOn": 0, "name": "string", "startTime": 0, "state": "string", "tasks": [{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}], "tenantId": "string", "type": "string", "useState": "string", "version": 0}, "systemWorkflow": {"_id": "string", "addToInventory": true, "addedOn": 0, "configId": "string", "currTaskIdx": 0, "description": "string", "endTime": 0, "execTime": 0, "imageId": "string", "instanceType": "SystemWorkflow", "lastupdateOn": 0, "name": "string", "startTime": 0, "state": "string", "tasks": [{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}], "tenantId": "string", "type": "string", "useState": "string", "version": 0}, "tenantId": "string", "version": 0, "workflow": {"_id": "string", "addToInventory": true, "addedOn": 0, "configId": "string", "currTaskIdx": 0, "description": "string", "endTime": 0, "execTime": 0, "imageId": "string", "instanceType": "SystemWorkflow", "lastupdateOn": 0, "name": "string", "startTime": 0, "state": "string", "tasks": [{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}], "tenantId": "string", "type": "string", "useState": "string", "version": 0}, "workflowParameters": {"configList": [{"configId": "string", "configParameters": [{"key": "string", "value": "string"}]}], "licenseLevel": "string", "licenseType": "string", "topOfStackSerialNumber": "string"}}'"""])
    assert not result.exception
    assert is_valid_import_devices_in_bulk(result)


def is_valid_update_workflow(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_update_workflow(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'update-workflow',
                                 """--_id='string'""",
                                 """--active_validation=True""",
                                 """--addtoinventory=True""",
                                 """--addedon=0""",
                                 """--configid='string'""",
                                 """--currtaskidx=0""",
                                 """--description='string'""",
                                 """--endtime=0""",
                                 """--exectime=0""",
                                 """--id='string'""",
                                 """--imageid='string'""",
                                 """--instancetype='SystemWorkflow'""",
                                 """--lastupdateon=0""",
                                 """--name='string'""",
                                 """--payload=None""",
                                 """--starttime=0""",
                                 """--state='string'""",
                                 """--tasks='{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}'""",
                                 """--tenantid='string'""",
                                 """--type='string'""",
                                 """--usestate='string'""",
                                 """--version=0"""])
    assert not result.exception
    assert is_valid_update_workflow(result)


def is_valid_get_smart_account_list(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_get_smart_account_list(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'get-smart-account-list',
                                 """--"""])
    assert not result.exception
    assert is_valid_get_smart_account_list(result)


def is_valid_claim_a_device_to_a_site(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_claim_a_device_to_a_site(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'claim-a-device-to-a-site',
                                 """--active_validation=True""",
                                 """--deviceid='string'""",
                                 """--payload=None""",
                                 """--siteid='string'""",
                                 """--type='Default'"""])
    assert not result.exception
    assert is_valid_claim_a_device_to_a_site(result)


def is_valid_update_pnp_server_profile(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_update_pnp_server_profile(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'update-pnp-server-profile',
                                 """--active_validation=True""",
                                 """--autosyncperiod=0""",
                                 """--ccouser='string'""",
                                 """--expiry=0""",
                                 """--lastsync=0""",
                                 """--payload=None""",
                                 """--profile='{"addressFqdn": "string", "addressIpV4": "string", "cert": "string", "makeDefault": true, "name": "string", "port": 0, "profileId": "string", "proxy": true}'""",
                                 """--smartaccountid='string'""",
                                 """--syncresult='{"syncList": [{"deviceSnList": ["string"], "syncType": "Add"}], "syncMsg": "string"}'""",
                                 """--syncresultstr='string'""",
                                 """--syncstarttime=0""",
                                 """--syncstatus='NOT_SYNCED'""",
                                 """--tenantid='string'""",
                                 """--token='string'""",
                                 """--virtualaccountid='string'"""])
    assert not result.exception
    assert is_valid_update_pnp_server_profile(result)


def is_valid_get_workflow_count(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_get_workflow_count(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'get-workflow-count',
                                 """--name='value1,value2'"""])
    assert not result.exception
    assert is_valid_get_workflow_count(result)


def is_valid_get_virtual_account_list(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_get_virtual_account_list(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'get-virtual-account-list',
                                 """--domain='string'"""])
    assert not result.exception
    assert is_valid_get_virtual_account_list(result)


def is_valid_get_pnp_global_settings(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_get_pnp_global_settings(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'get-pnp-global-settings',
                                 """--"""])
    assert not result.exception
    assert is_valid_get_pnp_global_settings(result)


def is_valid_update_pnp_global_settings(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_update_pnp_global_settings(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'update-pnp-global-settings',
                                 """--_id='string'""",
                                 """--aaacredentials='{"password": "string", "username": "string"}'""",
                                 """--accepteula=True""",
                                 """--active_validation=True""",
                                 """--defaultprofile='{"cert": "string", "fqdnAddresses": ["string"], "ipAddresses": ["string"], "port": 0, "proxy": true}'""",
                                 """--payload=None""",
                                 """--savamappinglist='{"autoSyncPeriod": 0, "ccoUser": "string", "expiry": 0, "lastSync": 0, "profile": {"addressFqdn": "string", "addressIpV4": "string", "cert": "string", "makeDefault": true, "name": "string", "port": 0, "profileId": "string", "proxy": true}, "smartAccountId": "string", "syncResult": {"syncList": [{"deviceSnList": ["string"], "syncType": "Add"}], "syncMsg": "string"}, "syncResultStr": "string", "syncStartTime": 0, "syncStatus": "NOT_SYNCED", "tenantId": "string", "token": "string", "virtualAccountId": "string"}'""",
                                 """--tasktimeouts='{"configTimeOut": 0, "generalTimeOut": 0, "imageDownloadTimeOut": 0}'""",
                                 """--tenantid='string'""",
                                 """--version=0"""])
    assert not result.exception
    assert is_valid_update_pnp_global_settings(result)


def is_valid_add_a_workflow(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_add_a_workflow(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'add-a-workflow',
                                 """--_id='string'""",
                                 """--active_validation=True""",
                                 """--addtoinventory=True""",
                                 """--addedon=0""",
                                 """--configid='string'""",
                                 """--currtaskidx=0""",
                                 """--description='string'""",
                                 """--endtime=0""",
                                 """--exectime=0""",
                                 """--imageid='string'""",
                                 """--instancetype='SystemWorkflow'""",
                                 """--lastupdateon=0""",
                                 """--name='string'""",
                                 """--payload=None""",
                                 """--starttime=0""",
                                 """--state='string'""",
                                 """--tasks='{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}'""",
                                 """--tenantid='string'""",
                                 """--type='string'""",
                                 """--usestate='string'""",
                                 """--version=0"""])
    assert not result.exception
    assert is_valid_add_a_workflow(result)


def is_valid_sync_virtual_account_devices(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_sync_virtual_account_devices(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'sync-virtual-account-devices',
                                 """--active_validation=True""",
                                 """--autosyncperiod=0""",
                                 """--ccouser='string'""",
                                 """--expiry=0""",
                                 """--lastsync=0""",
                                 """--payload=None""",
                                 """--profile='{"addressFqdn": "string", "addressIpV4": "string", "cert": "string", "makeDefault": true, "name": "string", "port": 0, "profileId": "string", "proxy": true}'""",
                                 """--smartaccountid='string'""",
                                 """--syncresult='{"syncList": [{"deviceSnList": ["string"], "syncType": "Add"}], "syncMsg": "string"}'""",
                                 """--syncresultstr='string'""",
                                 """--syncstarttime=0""",
                                 """--syncstatus='NOT_SYNCED'""",
                                 """--tenantid='string'""",
                                 """--token='string'""",
                                 """--virtualaccountid='string'"""])
    assert not result.exception
    assert is_valid_sync_virtual_account_devices(result)


def is_valid_reset_device(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_reset_device(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'reset-device',
                                 """--active_validation=True""",
                                 """--deviceresetlist='{"configList": [{"configId": "string", "configParameters": [{"key": "string", "value": "string"}]}], "deviceId": "string", "licenseLevel": "string", "licenseType": "string", "topOfStackSerialNumber": "string"}'""",
                                 """--payload=None""",
                                 """--projectid='string'""",
                                 """--workflowid='string'"""])
    assert not result.exception
    assert is_valid_reset_device(result)


def is_valid_delete_workflow_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_delete_workflow_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'delete-workflow-by-id',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_delete_workflow_by_id(result)


def is_valid_delete_device_by_id_from_pnp(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_delete_device_by_id_from_pnp(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'delete-device-by-id-from-pnp',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_delete_device_by_id_from_pnp(result)


def is_valid_get_workflows(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_get_workflows(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'get-workflows',
                                 """--limit=0""",
                                 """--name='value1,value2'""",
                                 """--offset=0""",
                                 """--sort='value1,value2'""",
                                 """--sort_order='string'""",
                                 """--type='value1,value2'"""])
    assert not result.exception
    assert is_valid_get_workflows(result)


def is_valid_get_device_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_get_device_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'get-device-by-id',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_get_device_by_id(result)


def is_valid_get_device_count(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_get_device_count(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'get-device-count',
                                 """--cm_state='value1,value2'""",
                                 """--last_contact=True""",
                                 """--name='value1,value2'""",
                                 """--onb_state='value1,value2'""",
                                 """--pid='value1,value2'""",
                                 """--project_id='value1,value2'""",
                                 """--project_name='value1,value2'""",
                                 """--serial_number='value1,value2'""",
                                 """--smart_account_id='value1,value2'""",
                                 """--source='value1,value2'""",
                                 """--state='value1,value2'""",
                                 """--virtual_account_id='value1,value2'""",
                                 """--workflow_id='value1,value2'""",
                                 """--workflow_name='value1,value2'"""])
    assert not result.exception
    assert is_valid_get_device_count(result)


def is_valid_get_workflow_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_get_workflow_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'get-workflow-by-id',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_get_workflow_by_id(result)


def is_valid_get_device_history(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_get_device_history(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'get-device-history',
                                 """--serial_number='string'""",
                                 """--sort='value1,value2'""",
                                 """--sort_order='string'"""])
    assert not result.exception
    assert is_valid_get_device_history(result)


def is_valid_get_device_list(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_get_device_list(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'get-device-list',
                                 """--cm_state='value1,value2'""",
                                 """--last_contact=True""",
                                 """--limit=0""",
                                 """--name='value1,value2'""",
                                 """--offset=0""",
                                 """--onb_state='value1,value2'""",
                                 """--pid='value1,value2'""",
                                 """--project_id='value1,value2'""",
                                 """--project_name='value1,value2'""",
                                 """--serial_number='value1,value2'""",
                                 """--smart_account_id='value1,value2'""",
                                 """--sort='value1,value2'""",
                                 """--sort_order='string'""",
                                 """--source='value1,value2'""",
                                 """--state='value1,value2'""",
                                 """--virtual_account_id='value1,value2'""",
                                 """--workflow_id='value1,value2'""",
                                 """--workflow_name='value1,value2'"""])
    assert not result.exception
    assert is_valid_get_device_list(result)


def is_valid_preview_config(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_preview_config(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'preview-config',
                                 """--active_validation=True""",
                                 """--deviceid='string'""",
                                 """--payload=None""",
                                 """--siteid='string'""",
                                 """--type='Default'"""])
    assert not result.exception
    assert is_valid_preview_config(result)


def is_valid_add_device(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_add_device(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'add-device',
                                 """--_id='string'""",
                                 """--active_validation=True""",
                                 """--deviceinfo='{"aaaCredentials": {"password": "string", "username": "string"}, "addedOn": 0, "addnMacAddrs": ["string"], "agentType": "POSIX", "authStatus": "string", "authenticatedSudiSerialNo": "string", "capabilitiesSupported": ["string"], "cmState": "NotContacted", "description": "string", "deviceSudiSerialNos": ["string"], "deviceType": "string", "featuresSupported": ["string"], "fileSystemList": [{"freespace": 0, "name": "string", "readable": true, "size": 0, "type": "string", "writeable": true}], "firstContact": 0, "hostname": "string", "httpHeaders": [{"key": "string", "value": "string"}], "imageFile": "string", "imageVersion": "string", "ipInterfaces": [{"ipv4Address": {}, "ipv6AddressList": [{}], "macAddress": "string", "name": "string", "status": "string"}], "lastContact": 0, "lastSyncTime": 0, "lastUpdateOn": 0, "location": {"address": "string", "altitude": "string", "latitude": "string", "longitude": "string", "siteId": "string"}, "macAddress": "string", "mode": "string", "name": "string", "neighborLinks": [{"localInterfaceName": "string", "localMacAddress": "string", "localShortInterfaceName": "string", "remoteDeviceName": "string", "remoteInterfaceName": "string", "remoteMacAddress": "string", "remotePlatform": "string", "remoteShortInterfaceName": "string", "remoteVersion": "string"}], "onbState": "NotContacted", "pid": "string", "pnpProfileList": [{"createdBy": "string", "discoveryCreated": true, "primaryEndpoint": {"certificate": "string", "fqdn": "string", "ipv4Address": {}, "ipv6Address": {}, "port": 0, "protocol": "string"}, "profileName": "string", "secondaryEndpoint": {"certificate": "string", "fqdn": "string", "ipv4Address": {}, "ipv6Address": {}, "port": 0, "protocol": "string"}}], "populateInventory": true, "preWorkflowCliOuputs": [{"cli": "string", "cliOutput": "string"}], "projectId": "string", "projectName": "string", "reloadRequested": true, "serialNumber": "string", "smartAccountId": "string", "source": "string", "stack": true, "stackInfo": {"isFullRing": true, "stackMemberList": [{"hardwareVersion": "string", "licenseLevel": "string", "licenseType": "string", "macAddress": "string", "pid": "string", "priority": 0, "role": "string", "serialNumber": "string", "softwareVersion": "string", "stackNumber": 0, "state": "string", "sudiSerialNumber": "string"}], "stackRingProtocol": "string", "supportsStackWorkflows": true, "totalMemberCount": 0, "validLicenseLevels": ["string"]}, "state": "Unclaimed", "sudiRequired": true, "tags": {}, "userSudiSerialNos": ["string"], "virtualAccountId": "string", "workflowId": "string", "workflowName": "string"}'""",
                                 """--payload=None""",
                                 """--runsummarylist='{"details": "string", "errorFlag": true, "historyTaskInfo": {"addnDetails": [{"key": "string", "value": "string"}], "name": "string", "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}, "timestamp": 0}'""",
                                 """--systemresetworkflow='{"_id": "string", "addToInventory": true, "addedOn": 0, "configId": "string", "currTaskIdx": 0, "description": "string", "endTime": 0, "execTime": 0, "imageId": "string", "instanceType": "SystemWorkflow", "lastupdateOn": 0, "name": "string", "startTime": 0, "state": "string", "tasks": [{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}], "tenantId": "string", "type": "string", "useState": "string", "version": 0}'""",
                                 """--systemworkflow='{"_id": "string", "addToInventory": true, "addedOn": 0, "configId": "string", "currTaskIdx": 0, "description": "string", "endTime": 0, "execTime": 0, "imageId": "string", "instanceType": "SystemWorkflow", "lastupdateOn": 0, "name": "string", "startTime": 0, "state": "string", "tasks": [{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}], "tenantId": "string", "type": "string", "useState": "string", "version": 0}'""",
                                 """--tenantid='string'""",
                                 """--version=0""",
                                 """--workflow='{"_id": "string", "addToInventory": true, "addedOn": 0, "configId": "string", "currTaskIdx": 0, "description": "string", "endTime": 0, "execTime": 0, "imageId": "string", "instanceType": "SystemWorkflow", "lastupdateOn": 0, "name": "string", "startTime": 0, "state": "string", "tasks": [{"currWorkItemIdx": 0, "endTime": 0, "name": "string", "startTime": 0, "state": "string", "taskSeqNo": 0, "timeTaken": 0, "type": "string", "workItemList": [{"command": "string", "endTime": 0, "outputStr": "string", "startTime": 0, "state": "string", "timeTaken": 0}]}], "tenantId": "string", "type": "string", "useState": "string", "version": 0}'""",
                                 """--workflowparameters='{"configList": [{"configId": "string", "configParameters": [{"key": "string", "value": "string"}]}], "licenseLevel": "string", "licenseType": "string", "topOfStackSerialNumber": "string"}'"""])
    assert not result.exception
    assert is_valid_add_device(result)


def is_valid_claim_device(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.pnp
def test_claim_device(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '1.3.0', *auth_options,
                                 'pnp', 'claim-device',
                                 """--active_validation=True""",
                                 """--configfileurl='string'""",
                                 """--configid='string'""",
                                 """--deviceclaimlist='{"configList": [{"configId": "string", "configParameters": [{"key": "string", "value": "string"}]}], "deviceId": "string", "licenseLevel": "string", "licenseType": "string", "topOfStackSerialNumber": "string"}'""",
                                 """--fileserviceid='string'""",
                                 """--imageid='string'""",
                                 """--imageurl='string'""",
                                 """--payload=None""",
                                 """--populateinventory=True""",
                                 """--projectid='string'""",
                                 """--workflowid='string'"""])
    assert not result.exception
    assert is_valid_claim_device(result)
