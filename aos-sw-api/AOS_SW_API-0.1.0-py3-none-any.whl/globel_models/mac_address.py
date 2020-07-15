from pydantic import BaseModel

from aos_sw_api.enums import MacAddressVersionEnum


class MacAddress(BaseModel):
    version: MacAddressVersionEnum
    octets: str
