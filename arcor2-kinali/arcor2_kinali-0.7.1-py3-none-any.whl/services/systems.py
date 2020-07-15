from typing import FrozenSet, Optional

from arcor2 import rest
from arcor2.exceptions import Arcor2Exception
from arcor2.services.service import Service


class SystemsException(Arcor2Exception):
    pass


@rest.handle_exceptions(SystemsException, "Failed to get available configurations.")
def systems(url: str) -> FrozenSet[str]:
    return frozenset(rest.get_data(f"{url}/systems"))


@rest.handle_exceptions(SystemsException, "Failed to initialize the service.")
def create(url: str, srv: Service) -> None:

    if active(url) == srv.configuration_id:
        return

    rest.put(f"{url}/systems/{srv.configuration_id}/create")


@rest.handle_exceptions(SystemsException, "Failed to destroy the service.")
def destroy(url: str) -> None:
    rest.put(f"{url}/systems/destroy")


@rest.handle_exceptions(SystemsException, "Failed to get current configuration.")
def active(url: str) -> Optional[str]:
    return rest.get_primitive(f"{url}/systems/active", str)
