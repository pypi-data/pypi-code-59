# -*- coding: utf-8 -*-
"""DNACenterAPI Software Image Management (SWIM) API fixtures and tests.

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


def is_valid_get_software_image_details(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.software_image_management_swim
def test_get_software_image_details(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'software-image-management-swim', 'get-software-image-details',
                                 """--application_type='string'""",
                                 """--created_time=0""",
                                 """--family='string'""",
                                 """--image_integrity_status='string'""",
                                 """--image_name='string'""",
                                 """--image_series='string'""",
                                 """--image_size_greater_than=0""",
                                 """--image_size_lesser_than=0""",
                                 """--image_uuid='string'""",
                                 """--is_cco_latest=True""",
                                 """--is_cco_recommended=True""",
                                 """--is_tagged_golden=True""",
                                 """--limit=0""",
                                 """--name='string'""",
                                 """--offset=0""",
                                 """--sort_by='string'""",
                                 """--sort_order='asc'""",
                                 """--version='string'"""])
    assert not result.exception
    assert is_valid_get_software_image_details(result)


def is_valid_import_local_software_image(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.software_image_management_swim
def test_import_local_software_image(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'software-image-management-swim', 'import-local-software-image',
                                 """--file='./tests/test-1592357065255.csv'""",
                                 """--filename='test-1592357065255.csv'""",
                                 """--is_third_party=True""",
                                 """--third_party_application_type='string'""",
                                 """--third_party_image_family='string'""",
                                 """--third_party_vendor='string'"""])
    assert not result.exception
    assert is_valid_import_local_software_image(result)


def is_valid_trigger_software_image_distribution(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.software_image_management_swim
def test_trigger_software_image_distribution(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'software-image-management-swim', 'trigger-software-image-distribution',
                                 """--active_validation=True""",
                                 """--payload='{"deviceUuid": "string", "imageUuid": "string"}'"""])
    assert not result.exception
    assert is_valid_trigger_software_image_distribution(result)


def is_valid_import_software_image_via_url(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.software_image_management_swim
def test_import_software_image_via_url(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'software-image-management-swim', 'import-software-image-via-url',
                                 """--active_validation=True""",
                                 """--payload='{"applicationType": "string", "imageFamily": "string", "sourceURL": "string", "thirdParty": true, "vendor": "string"}'""",
                                 """--schedule_at='string'""",
                                 """--schedule_desc='string'""",
                                 """--schedule_origin='string'"""])
    assert not result.exception
    assert is_valid_import_software_image_via_url(result)


def is_valid_trigger_software_image_activation(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.software_image_management_swim
def test_trigger_software_image_activation(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'software-image-management-swim', 'trigger-software-image-activation',
                                 """--active_validation=True""",
                                 """--payload='{"activateLowerImageVersion": true, "deviceUpgradeMode": "string", "deviceUuid": "string", "distributeIfNeeded": true, "imageUuidList": ["string"], "smuImageUuidList": ["string"]}'""",
                                 """--schedule_validate=True"""])
    assert not result.exception
    assert is_valid_trigger_software_image_activation(result)
