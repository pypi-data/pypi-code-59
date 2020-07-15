from typing import List

from pydantic import BaseModel, Field

from aos_sw_api.enums import PortConfigModeEnum, PortTrunkTypeEnum, LacpStatusEnum


class PortStatistics(BaseModel):
    id: str
    name: str
    packets_tx: int
    packets_rx: int
    bytes_tx: int
    bytes_rx: int
    throughput_tx_bps: int
    throughput_rx_bps: int
    error_tx: int
    error_rx: int
    drop_tx: int
    port_speed_mbps: int


class PortStatisticsList(BaseModel):
    port_statistics_element: List[PortStatistics]


class PortElement(BaseModel):
    id: str
    name: str = Field(..., max_length=64)
    is_port_enabled: bool
    is_port_up: bool
    config_mode: PortConfigModeEnum
    trunk_mode: PortTrunkTypeEnum
    lacp_status: LacpStatusEnum
    trunk_group: str
    is_flow_control_enabled: bool
    is_dsnoop_port_trusted: bool


class SetPortElement(BaseModel):
    id: str
    name: str = Field(None, max_length=64)
    is_port_enabled: bool = None
    config_mode: PortConfigModeEnum = None
    lacp_status: LacpStatusEnum = None
    is_flow_control_enabled: bool = None
    is_dsnoop_port_trusted: bool = None


class PortElementList(BaseModel):
    port_element: List[PortElement]
