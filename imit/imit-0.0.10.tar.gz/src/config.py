import configparser
import ast

from pathlib import Path

config_path = str(Path.home()) + '/.imitrc.ini'
group = 'user'


def Write(key, value):
    config = configparser.ConfigParser()
    config.read(config_path, encoding="utf-8")

    config[group][key] = value
    with open(config_path, 'w') as configfile:
        config.write(configfile)


def Get(key):
    config = configparser.ConfigParser()
    config.read(config_path, encoding="utf-8")
    if config.has_option(group, key):
        return config.get(group, key)
    return ''
