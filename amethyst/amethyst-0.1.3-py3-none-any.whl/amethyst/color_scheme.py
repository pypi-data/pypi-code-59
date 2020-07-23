"""Module dedicated to the ColorScheme class."""

import logging
import os.path as op
import shutil
from typing import Dict
from typing import NamedTuple

import yaml

from amethyst import consts


class ColorScheme(NamedTuple):
    """Defines the colors to be used in the user interface."""

    background_main: str
    background_alternate: str
    gem_text: str
    gem_special_text: str
    gem_important_text: str
    key_text: str
    border: str
    key_background: str
    gem_icon: str
    gem_background: str
    gem_home_background: str
    gem_special_background: str
    gem_alternate_background: str
    gem_important_background: str
    gem_static_background: str
    gem_submodule_background: str

    @classmethod
    def from_name(cls, color_scheme_name: str) -> 'ColorScheme':
        """Get the color scheme according to user config, use the default one as callback."""

        if not op.isdir(consts.USER_COLOR_SCHEMES_PATH):
            logging.info('User color scheme folder does not exist, importing default themes...')
            shutil.copytree(consts.COLOR_SCHEMES_PATH, consts.USER_COLOR_SCHEMES_PATH)

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

        color_scheme = cls._check_attributes(color_scheme, default_color_scheme)
        logging.info('Loaded color scheme: %s', ''.join(['\n- %s: %s' % (k, v) for k, v in color_scheme.items()]))

        return ColorScheme(background_main=color_scheme['background_main'],
                           background_alternate=color_scheme['background_alternate'],
                           gem_text=color_scheme['gem_text'],
                           gem_special_text=color_scheme['gem_special_text'],
                           gem_important_text=color_scheme['gem_important_text'],
                           key_text=color_scheme['key_text'],
                           border=color_scheme['border'],
                           key_background=color_scheme['key_background'],
                           gem_icon=color_scheme['gem_icon'],
                           gem_background=color_scheme['gem_background'],
                           gem_home_background=color_scheme['gem_home_background'],
                           gem_special_background=color_scheme['gem_special_background'],
                           gem_alternate_background=color_scheme['gem_alternate_background'],
                           gem_important_background=color_scheme['gem_important_background'],
                           gem_static_background=color_scheme['gem_static_background'],
                           gem_submodule_background=color_scheme['gem_submodule_background'])

    @classmethod
    def _check_attributes(cls, color_scheme: Dict[str, str], default_color_scheme: Dict[str, str]) -> Dict[str, str]:
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
