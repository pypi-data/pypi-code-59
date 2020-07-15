from typing import Union

import httpx

from aos_sw_api.enums import DeviceOperationMode
from aos_sw_api._ip_address import IpAddress
from aos_sw_api.globel_models import IpAddressModel
from aos_sw_api.validate import validate_200
from ._model import SystemModel, SetSystemModel, SystemStatusModel, SystemTimeModel


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


class SystemSync(SystemBase):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def get_system(self) -> SystemModel:
        r = self._session.get(url=self._system_base_url)
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

    def update_system(self,
                      name: str = None,
                      location: str = None,
                      contact: str = None,
                      default_gateway: IpAddress = None,
                      device_operation_mode: DeviceOperationMode = None) -> SystemModel:
        input_data = dict(name=name,
                          location=location,
                          contact=contact,
                          device_operation_mode=device_operation_mode,
                          default_gateway=default_gateway)

        data_to_send = SystemBase._update_system_validate_input_and_return_data_to_send(input_data=input_data)

        r = self._session.put(url=self._system_base_url, json=data_to_send)
        validate_200(r)
        return SystemModel(**r.json())


class SystemAsync(SystemBase):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def get_system(self) -> SystemModel:
        r = await self._session.get(url=self._system_base_url)
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

    async def update_system(self,
                            name: str = None,
                            location: str = None,
                            contact: str = None,
                            default_gateway: IpAddress = None,
                            device_operation_mode: DeviceOperationMode = None) -> SystemModel:
        input_data = dict(name=name,
                          location=location,
                          contact=contact,
                          device_operation_mode=device_operation_mode,
                          default_gateway=default_gateway)

        data_to_send = SystemBase._update_system_validate_input_and_return_data_to_send(input_data=input_data)

        r = await self._session.put(url=self._system_base_url, json=data_to_send)
        validate_200(r)
        return SystemModel(**r.json())
