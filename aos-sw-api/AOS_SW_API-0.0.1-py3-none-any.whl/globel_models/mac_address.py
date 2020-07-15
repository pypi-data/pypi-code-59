from pydantic import BaseModel

from aos_sw_api.enums import MacAddressVersion


class MacAddress(BaseModel):
    version: MacAddressVersion
    octets: str
