# -*- coding: utf-8 -*-
"""DNACenterAPI Configuration Templates API fixtures and tests.

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


def is_valid_gets_the_templates_available(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.configuration_templates
def test_gets_the_templates_available(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'configuration-templates', 'gets-the-templates-available',
                                 """--filter_conflicting_templates=True""",
                                 """--product_family='string'""",
                                 """--product_series='string'""",
                                 """--product_type='string'""",
                                 """--project_id='string'""",
                                 """--software_type='string'""",
                                 """--software_version='string'"""])
    assert not result.exception
    assert is_valid_gets_the_templates_available(result)


def is_valid_create_project(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.configuration_templates
def test_create_project(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'configuration-templates', 'create-project',
                                 """--active_validation=True""",
                                 """--createtime=0""",
                                 """--description='string'""",
                                 """--id='string'""",
                                 """--lastupdatetime=0""",
                                 """--name='string'""",
                                 """--payload=None""",
                                 """--tags='string'""",
                                 """--templates='{}'"""])
    assert not result.exception
    assert is_valid_create_project(result)


def is_valid_get_projects(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.configuration_templates
def test_get_projects(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'configuration-templates', 'get-projects',
                                 """--name='string'"""])
    assert not result.exception
    assert is_valid_get_projects(result)


def is_valid_deploy_template(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.configuration_templates
def test_deploy_template(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'configuration-templates', 'deploy-template',
                                 """--active_validation=True""",
                                 """--forcepushtemplate=True""",
                                 """--iscomposite=True""",
                                 """--maintemplateid='string'""",
                                 """--membertemplatedeploymentinfo='string'""",
                                 """--payload=None""",
                                 """--targetinfo='{"hostName": "string", "id": "string", "params": {}, "type": "MANAGED_DEVICE_IP"}'""",
                                 """--templateid='string'"""])
    assert not result.exception
    assert is_valid_deploy_template(result)


def is_valid_version_template(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.configuration_templates
def test_version_template(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'configuration-templates', 'version-template',
                                 """--active_validation=True""",
                                 """--comments='string'""",
                                 """--payload=None""",
                                 """--templateid='string'"""])
    assert not result.exception
    assert is_valid_version_template(result)


def is_valid_update_template(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.configuration_templates
def test_update_template(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'configuration-templates', 'update-template',
                                 """--active_validation=True""",
                                 """--author='string'""",
                                 """--composite=True""",
                                 """--containingtemplates='{"composite": true, "id": "string", "name": "string", "version": "string"}'""",
                                 """--createtime=0""",
                                 """--description='string'""",
                                 """--devicetypes='{"productFamily": "string", "productSeries": "string", "productType": "string"}'""",
                                 """--failurepolicy='ABORT_ON_ERROR'""",
                                 """--id='string'""",
                                 """--lastupdatetime=0""",
                                 """--name='string'""",
                                 """--parenttemplateid='string'""",
                                 """--payload=None""",
                                 """--projectid='string'""",
                                 """--projectname='string'""",
                                 """--rollbacktemplatecontent='string'""",
                                 """--rollbacktemplateparams='{"binding": "string", "dataType": "STRING", "defaultValue": "string", "description": "string", "displayName": "string", "group": "string", "id": "string", "instructionText": "string", "key": "string", "notParam": true, "order": 0, "paramArray": true, "parameterName": "string", "provider": "string", "range": [{"id": "string", "maxValue": 0, "minValue": 0}], "required": true, "selection": {"id": "string", "selectionType": "SINGLE_SELECT", "selectionValues": {}}}'""",
                                 """--softwaretype='string'""",
                                 """--softwarevariant='string'""",
                                 """--softwareversion='string'""",
                                 """--tags='string'""",
                                 """--templatecontent='string'""",
                                 """--templateparams='{"binding": "string", "dataType": "STRING", "defaultValue": "string", "description": "string", "displayName": "string", "group": "string", "id": "string", "instructionText": "string", "key": "string", "notParam": true, "order": 0, "paramArray": true, "parameterName": "string", "provider": "string", "range": [{"id": "string", "maxValue": 0, "minValue": 0}], "required": true, "selection": {"id": "string", "selectionType": "SINGLE_SELECT", "selectionValues": {}}}'""",
                                 """--version='string'"""])
    assert not result.exception
    assert is_valid_update_template(result)


def is_valid_get_template_details(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.configuration_templates
def test_get_template_details(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'configuration-templates', 'get-template-details',
                                 """--latest_version=True""",
                                 """--template_id='string'"""])
    assert not result.exception
    assert is_valid_get_template_details(result)


def is_valid_update_project(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.configuration_templates
def test_update_project(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'configuration-templates', 'update-project',
                                 """--active_validation=True""",
                                 """--createtime=0""",
                                 """--description='string'""",
                                 """--id='string'""",
                                 """--lastupdatetime=0""",
                                 """--name='string'""",
                                 """--payload=None""",
                                 """--tags='string'""",
                                 """--templates='{}'"""])
    assert not result.exception
    assert is_valid_update_project(result)


def is_valid_get_template_deployment_status(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.configuration_templates
def test_get_template_deployment_status(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'configuration-templates', 'get-template-deployment-status',
                                 """--deployment_id='string'"""])
    assert not result.exception
    assert is_valid_get_template_deployment_status(result)


def is_valid_delete_template(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.configuration_templates
def test_delete_template(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'configuration-templates', 'delete-template',
                                 """--template_id='string'"""])
    assert not result.exception
    assert is_valid_delete_template(result)


def is_valid_get_template_versions(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.configuration_templates
def test_get_template_versions(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'configuration-templates', 'get-template-versions',
                                 """--template_id='string'"""])
    assert not result.exception
    assert is_valid_get_template_versions(result)


def is_valid_delete_project(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.configuration_templates
def test_delete_project(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'configuration-templates', 'delete-project',
                                 """--project_id='string'"""])
    assert not result.exception
    assert is_valid_delete_project(result)


def is_valid_preview_template(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.configuration_templates
def test_preview_template(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'configuration-templates', 'preview-template',
                                 """--active_validation=True""",
                                 """--params='{}'""",
                                 """--payload=None""",
                                 """--templateid='string'"""])
    assert not result.exception
    assert is_valid_preview_template(result)


def is_valid_create_template(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.configuration_templates
def test_create_template(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'configuration-templates', 'create-template',
                                 """--active_validation=True""",
                                 """--author='string'""",
                                 """--composite=True""",
                                 """--containingtemplates='{"composite": true, "id": "string", "name": "string", "version": "string"}'""",
                                 """--createtime=0""",
                                 """--description='string'""",
                                 """--devicetypes='{"productFamily": "string", "productSeries": "string", "productType": "string"}'""",
                                 """--failurepolicy='ABORT_ON_ERROR'""",
                                 """--id='string'""",
                                 """--lastupdatetime=0""",
                                 """--name='string'""",
                                 """--parenttemplateid='string'""",
                                 """--payload=None""",
                                 """--projectid='string'""",
                                 """--projectname='string'""",
                                 """--project_id='string'""",
                                 """--rollbacktemplatecontent='string'""",
                                 """--rollbacktemplateparams='{"binding": "string", "dataType": "STRING", "defaultValue": "string", "description": "string", "displayName": "string", "group": "string", "id": "string", "instructionText": "string", "key": "string", "notParam": true, "order": 0, "paramArray": true, "parameterName": "string", "provider": "string", "range": [{"id": "string", "maxValue": 0, "minValue": 0}], "required": true, "selection": {"id": "string", "selectionType": "SINGLE_SELECT", "selectionValues": {}}}'""",
                                 """--softwaretype='string'""",
                                 """--softwarevariant='string'""",
                                 """--softwareversion='string'""",
                                 """--tags='string'""",
                                 """--templatecontent='string'""",
                                 """--templateparams='{"binding": "string", "dataType": "STRING", "defaultValue": "string", "description": "string", "displayName": "string", "group": "string", "id": "string", "instructionText": "string", "key": "string", "notParam": true, "order": 0, "paramArray": true, "parameterName": "string", "provider": "string", "range": [{"id": "string", "maxValue": 0, "minValue": 0}], "required": true, "selection": {"id": "string", "selectionType": "SINGLE_SELECT", "selectionValues": {}}}'""",
                                 """--version='string'"""])
    assert not result.exception
    assert is_valid_create_template(result)
