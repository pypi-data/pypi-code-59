from configparser import ConfigParser
from os import unlink
from pathlib import Path
from typing import Final, Iterator, Tuple

from ..decorators import require_bins, run_subprocess
from ..errors import CliError
from .config import sym_config_file
from .contexts import push_env
from .params import get_okta_section, get_profile


class AwsOkta:
    __slots__ = ["resource"]
    aws_okta_cfg: Final[Path] = sym_config_file("aws-okta.cfg")
    debug: bool = False

    resource: Final[str]

    def __init__(self, resource: str) -> None:
        self.resource = resource

    @run_subprocess
    @require_bins("aws-okta")
    def exec(self, *args: str, **kwargs: str) -> Iterator[Tuple[str, ...]]:
        debug = ["--debug"] if self.debug else []
        options = [
            arg
            for (key, value) in kwargs.items()
            for arg in ("--" + key.replace("_", "-"), value)
        ]
        self.write_aws_okta_config()
        with push_env("AWS_CONFIG_FILE", str(self.aws_okta_cfg)):
            yield "aws-okta", *debug, "exec", "sym", "--", *args, *options

    def write_aws_okta_config(self) -> None:
        try:
            profile = get_profile(self.resource)
        except KeyError:
            raise CliError(f"Invalid resource: {self.resource}")

        config = ConfigParser(default_section="okta")
        config.read_dict(
            {
                "okta": get_okta_section(),
                "profile sym": {"region": profile.region, "role_arn": profile.arn},
            }
        )

        # To prevent symlink attacks, it is important to use exclusive
        # creation mode (`x` in the `open` mode). To allow the code to
        # work even if the file already exists, remove it first.
        try:
            unlink(self.aws_okta_cfg)
        except FileNotFoundError:
            pass
        with open(self.aws_okta_cfg, "x") as f:
            config.write(f)
