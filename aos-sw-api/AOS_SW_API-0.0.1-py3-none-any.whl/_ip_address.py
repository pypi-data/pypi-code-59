import ipaddress

from aos_sw_api.enums import IpAddressVersion


class IpAddress:

    def __init__(self,
                 version: IpAddressVersion,
                 octets: str):
        self.version = version
        self.octets = octets

    def as_dict(self) -> dict:
        return dict(version=self.version, octets=self.octets)

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        if value not in IpAddressVersion:
            raise ValueError("IP version most be IpAddressVersion")
        self._version = value

    @property
    def octets(self):
        return self._octets

    @octets.setter
    def octets(self, value):
        ip_address = ipaddress.ip_address(value)
        if isinstance(ip_address, ipaddress.IPv4Address) and self.version != IpAddressVersion.IAV_IP_V4:
            raise ValueError("IP address must be IP_v4")
        if isinstance(ip_address, ipaddress.IPv6Address) and self.version != IpAddressVersion.IAV_IP_V6:
            raise ValueError("IP address must be IP_v6")
        self._octets = value
