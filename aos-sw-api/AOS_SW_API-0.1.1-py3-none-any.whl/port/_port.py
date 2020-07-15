from typing import Union

import httpx

from aos_sw_api._validate import validate_200
from aos_sw_api.enums import PortConfigModeEnum, LacpStatusEnum
from ._model import PortElementList, PortElement, PortStatisticsList, PortStatistics


class Port:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return PortSync(session=session)
        elif isinstance(session, httpx.AsyncClient):
            return PortAsync(session=session)


class PortBase:
    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient]):
        self._session = session
        self._port_base_url = "ports"
        self._port_statistics_base_url = "port-statistics"


class PortSync(PortBase):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def get_all_ports(self) -> PortElementList:
        r = self._session.get(url=self._port_base_url)
        validate_200(r)
        return PortElementList(**r.json())

    def get_one_port(self, port_id: str) -> PortElement:
        r = self._session.get(url=f"{self._port_base_url}/{port_id}")
        validate_200(r)
        return PortElement(**r.json())

    def update_one_port(self,
                        port_id: str,  # renamed from id
                        name: str = None,
                        is_port_enabled: bool = None,
                        config_mode: PortConfigModeEnum = None,
                        lacp_status: LacpStatusEnum = None,
                        is_flow_control_enabled: bool = None,
                        is_dsnoop_port_trusted: bool = None) -> PortElement:
        pass
        # TODO

    def get_all_ports_statistics(self) -> PortStatisticsList:
        r = self._session.get(url=self._port_statistics_base_url)
        validate_200(r)
        return PortStatisticsList(**r.json())

    def get_one_port_statistics(self, port_id: str) -> PortStatistics:
        r = self._session.get(url=f"{self._port_statistics_base_url}/{port_id}")
        validate_200(r)
        return PortStatistics(**r.json())


class PortAsync(PortBase):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def get_all_ports(self) -> PortElementList:
        r = await self._session.get(url=self._port_base_url)
        validate_200(r)
        return PortElementList(**r.json())

    async def get_one_port(self, port_id: str) -> PortElement:
        r = await self._session.get(url=f"{self._port_base_url}/{port_id}")
        validate_200(r)
        return PortElement(**r.json())

    async def update_one_port(self,
                              port_id: str,  # renamed from id
                              name: str = None,
                              is_port_enabled: bool = None,
                              config_mode: PortConfigModeEnum = None,
                              lacp_status: LacpStatusEnum = None,
                              is_flow_control_enabled: bool = None,
                              is_dsnoop_port_trusted: bool = None) -> PortElement:
        pass
        # TODO

    async def get_all_ports_statistics(self) -> PortStatisticsList:
        r = await self._session.get(url=self._port_statistics_base_url)
        validate_200(r)
        return PortStatisticsList(**r.json())

    async def get_one_port_statistics(self, port_id: str) -> PortStatistics:
        r = await self._session.get(url=f"{self._port_statistics_base_url}/{port_id}")
        validate_200(r)
        return PortStatistics(**r.json())
