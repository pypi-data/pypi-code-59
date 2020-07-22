"""Module dedicated to the ColorScheme class."""

import logging
import os.path as op
import shutil
from typing import Dict

import yaml

from amethyst import consts


class ColorScheme:
    """
    Defines the colors to be used in the user interface.
    Set them to the values defined in the given color scheme, or to the default color scheme if errors happen.
    """
    # pylint: disable=too-many-instance-attributes

    def __init__(self, color_scheme_name: str):
        if not op.isdir(consts.USER_COLOR_SCHEMES_PATH):
            logging.info('User color scheme folder does not exist, importing default themes...')
            shutil.copytree(consts.COLOR_SCHEMES_PATH, consts.USER_COLOR_SCHEMES_PATH)

        color_scheme = self.get_color_scheme(color_scheme_name)

        self.background_main: str = color_scheme['background_main']
        self.background_alternate: str = color_scheme['background_alternate']
        self.gem_text: str = color_scheme['gem_text']
        self.gem_special_text: str = color_scheme['gem_special_text']
        self.gem_important_text: str = color_scheme['gem_important_text']
        self.key_text: str = color_scheme['key_text']
        self.border: str = color_scheme['border']
        self.key_background: str = color_scheme['key_background']
        self.gem_icon: str = color_scheme['gem_icon']
        self.gem_background: str = color_scheme['gem_background']
        self.gem_home_background: str = color_scheme['gem_home_background']
        self.gem_special_background: str = color_scheme['gem_special_background']
        self.gem_alternate_background: str = color_scheme['gem_alternate_background']
        self.gem_important_background: str = color_scheme['gem_important_background']
        self.gem_static_background: str = color_scheme['gem_static_background']
        self.gem_submodule_background: str = color_scheme['gem_submodule_background']

    def get_color_scheme(self, color_scheme_name: str) -> Dict[str, str]:
        """Get the color scheme according to user config, use the default one as callback."""

        color_scheme_path = op.join(consts.USER_COLOR_SCHEMES_PATH, '%s.yml' % color_scheme_name)
        default_color_scheme_path = op.join(consts.COLOR_SCHEMES_PATH, '%s.yml' % consts.DEFAULT_COLOR_SCHEME)
        with open(default_color_scheme_path) as default_color_scheme:
            default_color_scheme = yaml.safe_load(default_color_scheme)

        try:
            with open(color_scheme_path) as color_scheme_file:
                color_scheme = yaml.safe_load(color_scheme_file)
        except FileNotFoundError:
            logging.warning('Color scheme %s can not be found, using default color scheme.')
            color_scheme = default_color_scheme
        except yaml.YAMLError as error:
            logging.error(error)
            logging.warning('Color scheme %s is not valid, using default color scheme.')
            color_scheme = default_color_scheme

        logging.info('Loaded color scheme: %s', ''.join(['\n- %s: %s' % (k, v) for k, v in color_scheme.items()]))
        return self.check_attributes(color_scheme, default_color_scheme)

    @staticmethod
    def check_attributes(color_scheme: Dict[str, str], default_color_scheme: Dict[str, str]) -> Dict[str, str]:
        """Compare the color scheme attributes with the default color scheme, add missing colors if necessary."""

        unknown_colors = [value for value in color_scheme if value not in default_color_scheme]
        unset_colors = [value for value in default_color_scheme if value not in color_scheme]

        if unknown_colors:
            logging.warning('The following colors are unrecognised and will be ignored:')
            for item in unknown_colors:
                logging.warning('- %s', item)
                color_scheme.pop(item)

        if unset_colors:
            logging.warning('The following colors are not defined and will be set to their corresponding value in the '
                            'default color scheme:')
            for item in unset_colors:
                logging.warning('- %s', item)
                color_scheme[item] = default_color_scheme[item]

        return color_scheme
