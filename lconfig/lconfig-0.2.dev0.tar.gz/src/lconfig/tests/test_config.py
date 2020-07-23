from lconfig.config import Config


def test_config_get():
    config = Config({'bar': 'baz'})
    assert config.get('foo') is None
    assert config.get('bar') == 'baz'
