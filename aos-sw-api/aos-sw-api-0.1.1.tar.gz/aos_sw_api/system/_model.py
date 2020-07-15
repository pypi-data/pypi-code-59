from typing import List

from pydantic import BaseModel, Field

from aos_sw_api.enums import DeviceOperationModeEnum, TimeServerProtocolEnum
from aos_sw_api.globel_models import IpAddressModel, MacAddress, NetworkHostModel


class RollbackToGoodCfg(BaseModel):
    is_config_rollbacked: bool
    is_rollback_supported: bool


class SystemModel(BaseModel):
    name: str = Field(..., max_length=32)
    location: str = Field(..., max_length=64)
    contact: str = Field(..., max_length=64)
    device_operation_mode: DeviceOperationModeEnum
    default_gateway: IpAddressModel
    rollback_to_good_config: RollbackToGoodCfg = Field(None, description="This is not supported on 2620 and 3800")


class SetSystemModel(BaseModel):
    name: str = Field(None, max_length=32)
    location: str = Field(None, max_length=64)
    contact: str = Field(None, max_length=64)
    device_operation_mode: DeviceOperationModeEnum = None
    default_gateway: IpAddressModel = None
    rollback_to_good_config: RollbackToGoodCfg = Field(None, description="This is not supported on 2620 and 3800")


class SystemStatusModel(BaseModel):
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
    local_utc_offset_in_seconds: int = Field(..., ge=-43200, le=50400)
    auto_adjust_dst: bool
    time_server_protocol: TimeServerProtocolEnum
    time_servers: List[NetworkHostModel] = Field(..., max_items=3)
    use_sntp_unicast: bool


class SetSystemTimeModel(BaseModel):
    local_utc_offset_in_seconds: int = Field(None, ge=-43200, le=50400)
    auto_adjust_dst: bool = None
    time_server_protocol: TimeServerProtocolEnum
    time_servers: List[NetworkHostModel] = Field(max_items=3)
    use_sntp_unicast: bool
