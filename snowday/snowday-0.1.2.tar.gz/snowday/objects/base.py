from dataclasses import dataclass
from snowday.exceptions import InvalidWhitespaceException
from snowday.util import get_resource_type, settings_str_from


@dataclass
class BaseSnowflakeObject:

    name: str

    def __post_init__(self):
        if " " in self.name:
            raise InvalidWhitespaceException(
                f"Invalid whitespace in name: {self.name}\n\nPlease make it {self.name.replace(' ', '')} instead."
            )

    @property
    def _settings_str(self):
        return settings_str_from(self)

    @property
    def fqn(self):
        return self.name

    @property
    def resource_type(self):
        return get_resource_type(self)

    @property
    def describe(self):
        return f"describe {self.resource_type} {self.fqn};"

    @property
    def drop(self):
        return f"drop {self.resource_type} {self.fqn};"

    @property
    def drop_if_exists(self):
        return f"drop {self.resource_type} if exists {self.fqn};"

    @property
    def create(self):
        if hasattr(self, "__base__"):  # FIXME: figure out a way to do this better
            raise NotImplementedError("create is not implemented on base classes")
        return f"create {self.resource_type} " f"{self.fqn} " f"{self._settings_str};"

    @property
    def create_if_not_exists(self):
        return (
            f"create {self.resource_type} if not exists "
            f"{self.fqn} "
            f"{self._settings_str};"
        )

    @property
    def create_or_replace(self):
        return (
            f"create or replace {self.resource_type} "
            f"{self.fqn} "
            f"{self._settings_str};"
        )
