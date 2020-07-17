import yaml

from fxq.commons import dict_merge


class Environment:
    PROPERTY_FILE_PREFIX = 'app'

    def __init__(self, active_profiles=[], base_dir=""):
        self._base_dir = base_dir
        self.active_profiles = active_profiles
        self._properties = {}
        self._load_properties()

    def get_property(self, key):
        try:
            retval = self._properties
            for k in key.split("."):
                retval = retval.get(k)
            return retval
        except AttributeError:
            raise EnvironmentError(
                f"Property: {key} not found! Please define {key} in your {Environment.PROPERTY_FILE_PREFIX}.yml files, "
                f"currently active profiles are {self.active_profiles}"
            ) from None

    def _load_properties(self):
        # Load Initial no-profile file
        base_dir = f"{self._base_dir}/" if self._base_dir != "" else ""
        self._properties = yaml.load(open(f"{base_dir}{Environment.PROPERTY_FILE_PREFIX}.yml").read(),
                                     Loader=yaml.SafeLoader)

        # Load profile files if any active profiles are set
        for p in self.active_profiles:
            dict_merge(
                self._properties,
                yaml.load(open(f"{base_dir}{Environment.PROPERTY_FILE_PREFIX}.{p}.yml").read(), Loader=yaml.SafeLoader)
            )


class EnvironmentError(Exception):
    pass
