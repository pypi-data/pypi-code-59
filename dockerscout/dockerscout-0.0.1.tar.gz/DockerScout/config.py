import os
import yaml
import platform

from .utils import space_suffix


CONFIG_DIR = ".docker-scout"
HISTORY_FILE = "images.json"
CONFIG_FILE = "limits.yml"


def config_dir():
    """
    Get the config folder
    :return:
    """
    override = os.getenv("DOCKERSCOUT_DIR", None)
    if override is not None:
        if not os.path.exists(override):
            os.makedirs(override)
        return override

    if platform.system() == "Windows":
        appdata = os.getenv("LOCALAPPDATA",
                            os.getenv("USERPROFILE",
                                      os.getenv("TMP")))
        cfg = os.path.join(appdata, CONFIG_DIR)
    else:
        home = os.getenv("HOME", "/tmp")
        cfg = os.path.join(home, CONFIG_DIR)

    if not os.path.exists(cfg):
        os.makedirs(cfg)
    return cfg


def config_path():
    """
    Get the config file path
    :return:
    """
    # try some system-wide places first
    if platform.system() == "Windows":
        cfg = os.getenv("windir", None)
    if platform.system() == "Linux":
        cfg = "/etc/"
    local_cfg = os.path.join(config_dir(), CONFIG_FILE)
    if not os.path.exists(local_cfg):
        global_cfg = os.path.join(cfg, CONFIG_FILE)
        if os.path.exists(global_cfg):
            return global_cfg

    return os.path.join(cfg, CONFIG_FILE)


class ScoutConfigV1(object):
    DEFAULT_MIN_DISK_FREE = "10g"

    def __init__(self, data):
        if data is not None:
            self.data = data["scout"]["v1"]
        else:
            self.data = {}

    def min_disk(self):
        """
        Return the point at which we start cleaning old images
        :return:
        """
        return space_suffix(self.data.get("min-disk-free", self.DEFAULT_MIN_DISK_FREE))


def read_config(filename):
    """
    Read the docker scout configuration. If no config exist, use defaults
    :param filename:
    :return:
    """
    if os.path.exists(filename):
        with open(filename, "r") as configfile:
            data = yaml.load(configfile, Loader=yaml.SafeLoader)
    else:
        data = None

    return ScoutConfigV1(data)
