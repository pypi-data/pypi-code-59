"""Many constant definitions used elsewhere in the project."""

import os.path as op
import tempfile

import appdirs

# The application name, used for instance for the config folder name in the user config directory (ie. ~/.config/xxx).
APP_NAME = 'amethyst'

DEFAULT_COLOR_SCHEME = 'solarized_dark'

# The path of the Amethyst root folder.
PROJECT_PATH = op.dirname(op.dirname(op.abspath(__file__)))

# The path of the source code folder.
SRC_PATH = op.join(PROJECT_PATH, 'amethyst')

# The path of the assets folder.
ASSETS_FOLDER_PATH = op.join(PROJECT_PATH, 'assets')

# The path of the resources folder.
RESOURCES_PATH = op.join(PROJECT_PATH, 'resources')

# The path of the built-in color scheme folder.
COLOR_SCHEMES_PATH = op.join(RESOURCES_PATH, 'color_schemes')

# The path of the built-in modules folder.
MODULES_PATH = op.join(RESOURCES_PATH, 'modules')

# The path of the default configuration file.
DEFAULT_CONFIG_FILE_PATH = op.join(RESOURCES_PATH, 'default_config.yml')

# The path of the user configuration folder.
USER_CONFIG_PATH = appdirs.user_config_dir(APP_NAME)

# The path of the user configuration file.
USER_CONFIG_FILE_PATH = op.join(USER_CONFIG_PATH, 'config.yaml')

# The path of the user color scheme folder.
USER_COLOR_SCHEMES_PATH = op.join(USER_CONFIG_PATH, 'color_schemes')

# The path of the user modules folder.
USER_MODULES_PATH = op.join(USER_CONFIG_PATH, 'modules')

# The path of the user modules folder.
LOG_FILE_PATH = op.join(tempfile.gettempdir(), 'amethyst.log')
