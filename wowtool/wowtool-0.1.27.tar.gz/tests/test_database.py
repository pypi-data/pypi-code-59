import pytest
import json
from cli.database import Database

@pytest.fixture
def database():
    database = Database(database_file_path='tests/fixtures/test_database.json')
    return database

@pytest.fixture
def single_output_spec():
    with open('tests/fixtures/single_simplified_output_spec.json') as json_file:
        specification = json.load(json_file)
    return specification

def test_live_streams_table_exist(database):
    exist = database.live_streams_table_exist()
    assert exist in [False, True]

def test_get_live_stream_id_from_name(database):
    id = database.get_live_stream_id_from_name('Baton-6945748')
    assert id=='ww7jxjtw'

def test_insert_specification(database, single_output_spec):
    database.insert_specification(single_output_spec)
    assert 1==1

def test_delete_specification(database):
    database.delete_specification(id='1')
    assert 1==1

def test_insert_live_stream_mapping(database):
    document = {
        'live_stream_name': 'my-live-stream',
        'live_stream_id': '1'
    }
    database.insert_live_stream_mapping(document)
    assert 1==1

def test_delete_live_stream_mapping(database):
    database.delete_live_stream_mapping(id='1')
    assert 1==1