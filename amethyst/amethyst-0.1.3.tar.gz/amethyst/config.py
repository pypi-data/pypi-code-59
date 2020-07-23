"""Module dedicated to the Amy Config."""

import logging
import os
import os.path as op
from shutil import copyfile
from typing import Dict, Any

import yaml

from amethyst import consts

PREDEFINED_CONFIG_VALUES = {
    'window_size': [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
    'outer_size': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
    'inner_size': [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
    'key_delay': [0.03, 0.06, 0.09, 0.12, 0.15, 0.18, 0.21, 0.24],
    'color_scheme': ['solarized_dark']
}


class Config:
    """
    A config method used to load user's configuration file.
    """
    def __init__(self):
        if not op.isfile(consts.USER_CONFIG_FILE_PATH):
            self.create_user_config_folder()

        raw_config = self.check_attributes(self.get_raw_config())
        config = self.preprocess_config(raw_config)

        self.window_size_ratio: float = config['window_size']
        self.outer_size_ratio: float = config['outer_size']
        self.inner_size_ratio: float = config['inner_size']
        self.key_delay: float = config['key_delay']
        self.color_scheme: str = config['color_scheme']

    @staticmethod
    def create_user_config_folder() -> None:
        """Create the user config folder."""

        logging.info('%s not found, creating it from default config file.', consts.USER_CONFIG_FILE_PATH)
        if not op.isdir(consts.USER_CONFIG_PATH):
            os.makedirs(consts.USER_CONFIG_PATH)

        copyfile(consts.DEFAULT_CONFIG_FILE_PATH, consts.USER_CONFIG_FILE_PATH)

    @staticmethod
    def get_raw_config() -> Dict[str, int]:
        """Get the raw configuration values."""

        try:
            with open(consts.USER_CONFIG_FILE_PATH) as config_file:
                raw_config = yaml.safe_load(config_file)
        except FileNotFoundError:
            logging.warning('Config file is not found, using default config.')
            with open(consts.DEFAULT_CONFIG_FILE_PATH) as default_config_file:
                raw_config = yaml.safe_load(default_config_file)
        except yaml.YAMLError as error:
            logging.error(error)
            logging.warning('Config file is not valid, using default config.')
            with open(consts.DEFAULT_CONFIG_FILE_PATH) as default_config_file:
                raw_config = yaml.safe_load(default_config_file)

        logging.info('Loaded raw config file: %s', ''.join(['\n- %s: %s' % (k, v) for k, v in raw_config.items()]))
        return raw_config

    @staticmethod
    def check_attributes(raw_config: Dict[str, int]) -> Dict[str, int]:
        """Compare the config attributes with the default config, add missing attributes if necessary."""

        with open(consts.DEFAULT_CONFIG_FILE_PATH) as default_config_file:
            default_raw_config = yaml.safe_load(default_config_file)

        config_unknown = [value for value in raw_config if value not in PREDEFINED_CONFIG_VALUES]
        config_unset = [value for value in PREDEFINED_CONFIG_VALUES if value not in raw_config]

        if config_unknown:
            logging.warning('The following config attributes are unrecognised and will be ignored:')
            for item in config_unknown:
                logging.warning('- %s', item)
                raw_config.pop(item)

        if config_unset:
            logging.warning('The following config attributes are not defined and will be set to default:')
            for item in config_unset:
                logging.warning('- %s', item)
                raw_config[item] = default_raw_config[item]

        return raw_config

    @staticmethod
    def preprocess_config(raw_config: Dict[str, int]) -> Dict[str, Any]:
        """Return actual config values, using the PREDEFINED_CONFIG_VALUES dictionary."""

        config: dict = {}
        for config_key, raw_value in raw_config.items():
            try:
                config[config_key] = PREDEFINED_CONFIG_VALUES[config_key][raw_value - 1]
            except (KeyError, TypeError) as error:
                logging.error(error)
                logging.info('%s config value is not valid, using default config for this attribute.', config_key)
                with open(consts.DEFAULT_CONFIG_FILE_PATH) as default_config_file:
                    default_raw_value = yaml.safe_load(default_config_file)[config_key]
                    config[config_key] = PREDEFINED_CONFIG_VALUES[config_key][default_raw_value - 1]

        logging.info('Pre-processed config values: %s', ''.join(['\n- %s: %s' % (k, v) for k, v in config.items()]))

        return config
