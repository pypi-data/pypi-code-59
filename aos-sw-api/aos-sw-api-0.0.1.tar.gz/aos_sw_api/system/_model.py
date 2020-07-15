from typing import List

from pydantic import BaseModel, Field

from aos_sw_api.enums import DeviceOperationMode, TimeServerProtocol
from aos_sw_api.globel_models import IpAddressModel, MacAddress, NetworkHost


class RollbackToGoodCfg(BaseModel):
    is_config_rollbacked: bool
    is_rollback_supported: bool


class SystemModel(BaseModel):
    uri: str
    name: str = Field(..., max_length=32)
    location: str = Field(..., max_length=64)
    contact: str = Field(..., max_length=64)
    device_operation_mode: DeviceOperationMode
    default_gateway: IpAddressModel
    rollback_to_good_config: RollbackToGoodCfg = Field(None, description="This is not supported on 2620 and 3800")


class SetSystemModel(BaseModel):
    name: str = Field(None, max_length=32)
    location: str = Field(None, max_length=64)
    contact: str = Field(None, max_length=64)
    device_operation_mode: DeviceOperationMode = None
    default_gateway: IpAddressModel = None
    rollback_to_good_config: RollbackToGoodCfg = Field(None, description="This is not supported on 2620 and 3800")


class SystemStatusModel(BaseModel):
    uri: str
    name: str = Field(..., max_length=32)
    serial_number: str
    firmware_version: str
    hardware_revision: str
    product_model: str
    base_ethernet_address: MacAddress
    total_memory_in_bytes: int
    total_poe_consumption: int = Field(None, description="This is not supported on switch without POE")
    sys_temp: int = Field(None, description="This is supported on 3800 and 3810M")
    sys_temp_threshold: int = Field(None, description="This is supported on 3800 and 3810M")
    sys_fan_status: bool = Field(None, description="This is not supported on switch without fan")


class SystemTimeModel(BaseModel):
    uri: str
    local_utc_offset_in_seconds: int = Field(..., ge=-43200, le=50400)
    auto_adjust_dst: bool
    time_server_protocol: TimeServerProtocol
    time_servers: List[NetworkHost] = Field(..., max_items=3)
    use_sntp_unicast: bool
