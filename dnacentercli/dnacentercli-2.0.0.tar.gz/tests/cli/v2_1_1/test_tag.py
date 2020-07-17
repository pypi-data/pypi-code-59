# -*- coding: utf-8 -*-
"""DNACenterAPI Tag API fixtures and tests.

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


def is_valid_add_members_to_the_tag(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.tag
def test_add_members_to_the_tag(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'tag', 'add-members-to-the-tag',
                                 """--active_validation=True""",
                                 """--id='string'""",
                                 """--payload=None"""])
    assert not result.exception
    assert is_valid_add_members_to_the_tag(result)


def is_valid_create_tag(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.tag
def test_create_tag(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'tag', 'create-tag',
                                 """--active_validation=True""",
                                 """--description='string'""",
                                 """--dynamicrules='{"memberType": "string", "rules": {"values": ["string"], "items": ["string"], "operation": "string", "name": "string", "value": "string"}}'""",
                                 """--id='string'""",
                                 """--instancetenantid='string'""",
                                 """--name='string'""",
                                 """--payload=None""",
                                 """--systemtag=True"""])
    assert not result.exception
    assert is_valid_create_tag(result)


def is_valid_get_tag_member_count(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.tag
def test_get_tag_member_count(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'tag', 'get-tag-member-count',
                                 """--id='string'""",
                                 """--level='0'""",
                                 """--member_association_type='string'""",
                                 """--member_type='string'"""])
    assert not result.exception
    assert is_valid_get_tag_member_count(result)


def is_valid_delete_tag(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.tag
def test_delete_tag(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'tag', 'delete-tag',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_delete_tag(result)


def is_valid_updates_tag_membership(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.tag
def test_updates_tag_membership(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'tag', 'updates-tag-membership',
                                 """--active_validation=True""",
                                 """--membertotags='{"key": ["string"]}'""",
                                 """--membertype='string'""",
                                 """--payload=None"""])
    assert not result.exception
    assert is_valid_updates_tag_membership(result)


def is_valid_get_tag_resource_types(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.tag
def test_get_tag_resource_types(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'tag', 'get-tag-resource-types',
                                 """--"""])
    assert not result.exception
    assert is_valid_get_tag_resource_types(result)


def is_valid_update_tag(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.tag
def test_update_tag(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'tag', 'update-tag',
                                 """--active_validation=True""",
                                 """--description='string'""",
                                 """--dynamicrules='{"memberType": "string", "rules": {"values": ["string"], "items": ["string"], "operation": "string", "name": "string", "value": "string"}}'""",
                                 """--id='string'""",
                                 """--instancetenantid='string'""",
                                 """--name='string'""",
                                 """--payload=None""",
                                 """--systemtag=True"""])
    assert not result.exception
    assert is_valid_update_tag(result)


def is_valid_get_tag_count(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.tag
def test_get_tag_count(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'tag', 'get-tag-count',
                                 """--attribute_name='string'""",
                                 """--level='string'""",
                                 """--name='string'""",
                                 """--name_space='string'""",
                                 """--size='string'""",
                                 """--system_tag='string'"""])
    assert not result.exception
    assert is_valid_get_tag_count(result)


def is_valid_get_tag_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.tag
def test_get_tag_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'tag', 'get-tag-by-id',
                                 """--id='string'"""])
    assert not result.exception
    assert is_valid_get_tag_by_id(result)


def is_valid_remove_tag_member(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.tag
def test_remove_tag_member(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'tag', 'remove-tag-member',
                                 """--id='string'""",
                                 """--member_id='string'"""])
    assert not result.exception
    assert is_valid_remove_tag_member(result)


def is_valid_get_tag_members_by_id(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.tag
def test_get_tag_members_by_id(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'tag', 'get-tag-members-by-id',
                                 """--id='string'""",
                                 """--level='0'""",
                                 """--limit='string'""",
                                 """--member_association_type='string'""",
                                 """--member_type='string'""",
                                 """--offset='string'"""])
    assert not result.exception
    assert is_valid_get_tag_members_by_id(result)


def is_valid_get_tag(result):
    data = result.output.strip()
    return True if data else False


@pytest.mark.tag
def test_get_tag(runner, cli, auth_options):
    result = runner.invoke(cli, ['-v', '2.1.1', *auth_options,
                                 'tag', 'get-tag',
                                 """--additional_info_attributes='string'""",
                                 """--additional_info_name_space='string'""",
                                 """--field='string'""",
                                 """--level='string'""",
                                 """--limit='string'""",
                                 """--name='string'""",
                                 """--offset='string'""",
                                 """--order='string'""",
                                 """--size='string'""",
                                 """--sort_by='string'""",
                                 """--system_tag='string'"""])
    assert not result.exception
    assert is_valid_get_tag(result)
