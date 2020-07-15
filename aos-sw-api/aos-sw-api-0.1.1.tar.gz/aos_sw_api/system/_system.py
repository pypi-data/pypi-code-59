from typing import Union, List

import httpx

from aos_sw_api._ip_address import IpAddress
from aos_sw_api.enums import DeviceOperationModeEnum, TimeServerProtocolEnum
from aos_sw_api.globel_models import IpAddressModel, NetworkHostModel
from aos_sw_api.validate import validate_200
from ._model import SystemModel, SetSystemModel, SystemStatusModel, SystemTimeModel, SetSystemTimeModel


class System:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return SystemSync(session=session)
        elif isinstance(session, httpx.AsyncClient):
            return SystemAsync(session=session)


class SystemBase:
    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient]):
        self._session = session
        self._system_base_url = "system"

    @staticmethod
    def _update_system_validate_input_and_return_data_to_send(input_data: dict) -> dict:
        data_to_send = {}
        data_to_validate = {}

        for k, v in input_data.items():
            if v is None:
                continue
            if isinstance(v, IpAddress):
                data_to_send["default_gateway"] = v.as_dict()
                data_to_validate["default_gateway"] = IpAddressModel(**data_to_send["default_gateway"])
            else:
                data_to_send[k] = v
                data_to_validate[k] = v

        SetSystemModel(**data_to_validate)
        return data_to_send

    @staticmethod
    def _update_system_time_validate_input_and_return_data_to_send(input_data: dict) -> dict:
        data_to_send = {}
        data_to_validate = {}

        for k, v in input_data.items():
            if v is None:
                continue
            elif isinstance(v, list):
                data_to_send["time_servers"] = []
                data_to_validate["time_servers"] = []
                for host in v:
                    data_to_send["time_servers"].append({"ip_address": host.as_dict()})
                    data_to_validate["time_servers"].append(NetworkHostModel(ip_address=host.as_dict()))
            else:
                data_to_send[k] = v
                data_to_validate[k] = v

        SetSystemTimeModel(**data_to_validate)
        return data_to_send


class SystemSync(SystemBase):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def get_system(self) -> SystemModel:
        r = self._session.get(url=self._system_base_url)
        validate_200(r)
        return SystemModel(**r.json())

    def update_system(self,
                      name: str = None,
                      location: str = None,
                      contact: str = None,
                      default_gateway: IpAddress = None,
                      device_operation_mode: DeviceOperationModeEnum = None) -> SystemModel:
        if device_operation_mode:
            device_operation_mode = device_operation_mode.value

        input_data = dict(name=name,
                          location=location,
                          contact=contact,
                          default_gateway=default_gateway,
                          device_operation_mode=device_operation_mode)

        data_to_send = SystemBase._update_system_validate_input_and_return_data_to_send(input_data=input_data)
        print(data_to_send)
        r = self._session.put(url=self._system_base_url, json=data_to_send)
        validate_200(r)
        return SystemModel(**r.json())

    def get_system_status(self) -> SystemStatusModel:
        r = self._session.get(url=f"{self._system_base_url}/status")
        validate_200(r)
        return SystemStatusModel(**r.json())

    def get_system_time(self) -> SystemTimeModel:
        r = self._session.get(url=f"{self._system_base_url}/time")
        validate_200(r)
        return SystemTimeModel(**r.json())

    def update_system_time(self,
                           time_server_protocol: TimeServerProtocolEnum,
                           time_servers: List[IpAddress],
                           use_sntp_unicast: bool,
                           local_utc_offset_in_seconds: int = None,
                           auto_adjust_dst: bool = None) -> SystemTimeModel:

        if time_server_protocol:
            time_server_protocol = time_server_protocol.value

        input_data = dict(local_utc_offset_in_seconds=local_utc_offset_in_seconds,
                          auto_adjust_dst=auto_adjust_dst,
                          time_server_protocol=time_server_protocol,
                          time_servers=time_servers,
                          use_sntp_unicast=use_sntp_unicast)

        data_to_send = SystemBase._update_system_time_validate_input_and_return_data_to_send(input_data=input_data)
        print(data_to_send)
        r = self._session.put(url=f"{self._system_base_url}/time", json=data_to_send)
        validate_200(r)
        return SystemTimeModel(**r.json())


class SystemAsync(SystemBase):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def get_system(self) -> SystemModel:
        r = await self._session.get(url=self._system_base_url)
        validate_200(r)
        return SystemModel(**r.json())

    async def update_system(self,
                            name: str = None,
                            location: str = None,
                            contact: str = None,
                            default_gateway: IpAddress = None,
                            device_operation_mode: DeviceOperationModeEnum = None) -> SystemModel:
        input_data = dict(name=name,
                          location=location,
                          contact=contact,
                          device_operation_mode=device_operation_mode,
                          default_gateway=default_gateway)

        data_to_send = SystemBase._update_system_validate_input_and_return_data_to_send(input_data=input_data)

        r = await self._session.put(url=self._system_base_url, json=data_to_send)
        validate_200(r)
        return SystemModel(**r.json())

    async def get_system_status(self) -> SystemStatusModel:
        r = await self._session.get(url=f"{self._system_base_url}/status")
        validate_200(r)
        return SystemStatusModel(**r.json())

    async def get_system_time(self) -> SystemTimeModel:
        r = await self._session.get(url=f"{self._system_base_url}/time")
        validate_200(r)
        return SystemTimeModel(**r.json())

    async def update_system_time(self,
                                 time_server_protocol: TimeServerProtocolEnum,
                                 time_servers: List[IpAddress],
                                 use_sntp_unicast: bool,
                                 local_utc_offset_in_seconds: int = None,
                                 auto_adjust_dst: bool = None) -> SystemTimeModel:
        if time_server_protocol:
            time_server_protocol = time_server_protocol.value

        input_data = dict(local_utc_offset_in_seconds=local_utc_offset_in_seconds,
                          auto_adjust_dst=auto_adjust_dst,
                          time_server_protocol=time_server_protocol,
                          time_servers=time_servers,
                          use_sntp_unicast=use_sntp_unicast)

        data_to_send = SystemBase._update_system_time_validate_input_and_return_data_to_send(input_data=input_data)
        print(data_to_send)
        r = await self._session.put(url=f"{self._system_base_url}/time", json=data_to_send)
        validate_200(r)
        return SystemTimeModel(**r.json())
