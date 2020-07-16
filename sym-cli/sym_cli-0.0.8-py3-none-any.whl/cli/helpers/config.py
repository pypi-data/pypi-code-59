from pathlib import Path
from typing import Any, cast, Final, Iterator, Literal, MutableMapping, TypedDict
import yaml, os

ConfigKey = Literal["org"]


XDG_CONFIG_HOME = Path(os.getenv("XDG_CONFIG_HOME", str(Path.home() / ".config")))
SYM_CONFIG_HOME = XDG_CONFIG_HOME / "sym"


def sym_config_file(file_name: str) -> Path:
    return SYM_CONFIG_HOME / file_name


class ConfigSchema(TypedDict, total=False):
    org: str


class Config(MutableMapping[ConfigKey, Any]):
    __slots__ = ["path", "config"]

    path: Final[Path]
    config: Final[ConfigSchema]

    def __init__(self) -> None:
        self.path = sym_config_file("config.yml")
        self.path.parent.mkdir(parents=True, exist_ok=True)
        try:
            config = cast(
                ConfigSchema, yaml.load(self.path.open("r"), Loader=yaml.FullLoader)
            )
        except FileNotFoundError:
            config = ConfigSchema()
        self.config = config

    def __flush(self) -> None:
        yaml.dump(self.config, self.path.open("w"))

    def __getitem__(self, key: ConfigKey) -> Any:
        return self.config[key]

    def __delitem__(self, key: ConfigKey) -> None:
        del self.config[key]
        self.__flush()

    def __setitem__(self, key: ConfigKey, value: Any) -> None:
        self.config[key] = value
        self.__flush()

    def __iter__(self) -> Iterator[ConfigKey]:
        return cast(Iterator[ConfigKey], iter(self.config))

    def __len__(self) -> int:
        return len(self.config)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.path})"
