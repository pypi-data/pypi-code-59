from pydantic import BaseModel

from .ip_address import IpAddressModel


class NetworkHost(BaseModel):
    ip_address: IpAddressModel
