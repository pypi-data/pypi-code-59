from pydantic import BaseModel

from aos_sw_api.enums import IpAddressVersionEnum


class IpAddressModel(BaseModel):
    version: IpAddressVersionEnum
    octets: str
