from ipaddress import IPv4Address, IPv6Address
from typing import Union

from pydantic import BaseModel

from aos_sw_api.enums import IpAddressVersion


class IpAddressModel(BaseModel):
    version: IpAddressVersion
    octets: Union[IPv4Address, IPv6Address]
