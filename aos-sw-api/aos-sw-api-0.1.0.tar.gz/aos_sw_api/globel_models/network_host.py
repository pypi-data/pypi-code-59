from pydantic import BaseModel

from .ip_address import IpAddressModel


class NetworkHostModel(BaseModel):
    ip_address: IpAddressModel
