import pytest
from lconfig.config_file import ConfigFile


def test_file_does_not_exist(fs):
    with pytest.raises(FileNotFoundError):
        ConfigFile('not_existing.yml')


def test_empty_file(fs):
    fs.create_file('test.yml')
    file = ConfigFile('test.yml')
    assert file.config == {}


def test_find(fs):
    file_contents = """
    foo:
        bar: "baz"
    """
    fs.create_file('test.yml', contents=file_contents)
    file = ConfigFile('test.yml')
    with pytest.raises(KeyError):
        file.find('not_existent_key')
    assert file.find('foo.bar') == 'baz'
    assert file.find('foo') == {'bar': 'baz'}
