#  Copyright (c) 2020 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Device class for a SST Luminox Oxygen sensor. This device can measure the oxygen
concentration between 0 % and 25 %.

Furthermore, it measures the barometric pressure and internal temperature.
The device supports two operating modes: in streaming mode the device measures all
parameters every second, in polling mode the device measures only after a query.

Technical specification and documentation for the device can be found a the
manufacturer's page:
https://www.sstsensing.com/product/luminox-optical-oxygen-sensors-2/
"""

import logging
import re
from enum import Enum
from time import sleep
from typing import Union, Tuple, List, cast

from .base import SingleCommDevice
from ..comm import SerialCommunication, SerialCommunicationConfig
from ..comm.serial import (
    SerialCommunicationParity,
    SerialCommunicationStopbits,
    SerialCommunicationBytesize,
)
from ..configuration import configdataclass
from ..utils.enum import ValueEnum

Number = Union[int, float]


class LuminoxOutputModeError(Exception):
    """
    Wrong output mode for requested data
    """
    pass


class LuminoxOutputMode(Enum):
    """
    output mode.
    """
    streaming = 0
    polling = 1


class LuminoxMeasurementTypeError(Exception):
    """
    Wrong measurement type for requested data
    """
    pass


class LuminoxMeasurementType(ValueEnum):
    """
    measurement type.
    """
    _init_ = "value cast_type value_re"
    partial_pressure_o2 = "O", float, r'[0-9]{4}.[0-9]'
    percent_o2 = "%", float, r'[0-9]{3}.[0-9]{2}'
    temperature_sensor = "T", float, r'[+-][0-9]{2}.[0-9]'
    barometric_pressure = "P", int, r'[0-9]{4}'
    sensor_status = "e", int, r'[0-9]{4}'
    date_of_manufacture = "# 0", str, r'[0-9]{5} [0-9]{5}'
    serial_number = "# 1", str, r'[0-9]{5} [0-9]{5}'
    software_revision = "# 2", str, r'[0-9]{5}'

    @property
    def command(self) -> str:
        return self.value.split(" ")[0]

    def parse_read_measurement_value(
        self, read_txt: str
    ) -> Union[float, int, str]:

        parsed_data: List[str] = re.findall(f"{self.command} {self.value_re}", read_txt)
        if len(parsed_data) != 1:
            err_msg = (
                f"Expected measurement value for {self.name.replace('_', ' ')} of type "
                f"f{self.cast_type}; instead tyring to parse: \"{parsed_data}\""
            )
            logging.error(err_msg)
            raise LuminoxMeasurementTypeError(err_msg)

        parsed_measurement: str = parsed_data[0]
        try:
            parsed_value = self.cast_type(
                # don't check for empty match - we know already that there is one
                re.search(self.value_re, parsed_measurement).group()  # type: ignore
            )
        except ValueError:
            err_msg = (
                f"Expected measurement value for {self.name.replace('_', ' ')} of "
                f"type {self.cast_type}; instead tyring to parse: \"{parsed_data}\""
            )
            logging.error(err_msg)
            raise LuminoxMeasurementTypeError(err_msg)

        return parsed_value


@configdataclass
class LuminoxSerialCommunicationConfig(SerialCommunicationConfig):
    #: Baudrate for SST Luminox is 9600 baud
    baudrate: int = 9600

    #: SST Luminox does not use parity
    parity: Union[str, SerialCommunicationParity] = SerialCommunicationParity.NONE

    #: SST Luminox does use one stop bit
    stopbits: Union[int, SerialCommunicationStopbits] = SerialCommunicationStopbits.ONE

    #: One byte is eight bits long
    bytesize: Union[
        int, SerialCommunicationBytesize
    ] = SerialCommunicationBytesize.EIGHTBITS

    #: The terminator is CR LF
    terminator: bytes = b"\r\n"

    #: use 3 seconds timeout as default
    timeout: Number = 3


class LuminoxSerialCommunication(SerialCommunication):
    """
    Specific communication protocol implementation for the SST Luminox oxygen sensor.
    Already predefines device-specific protocol parameters in config.
    """

    @staticmethod
    def config_cls():
        return LuminoxSerialCommunicationConfig


@configdataclass
class LuminoxConfig:
    """
    Configuration for the SST Luminox oxygen sensor.
    """

    # wait between set and validation of output mode
    wait_sec_post_activate: Number = 0.5

    def clean_values(self):
        if self.wait_sec_post_activate <= 0:
            raise ValueError(
                "Wait time post output mode activation must be a positive value (in "
                "seconds)."
            )


class Luminox(SingleCommDevice):
    """
    Luminox oxygen sensor device class.
    """
    output: Union[None, LuminoxOutputMode] = None

    def __init__(self, com, dev_config=None):

        # Call superclass constructor
        super().__init__(com, dev_config)

    @staticmethod
    def config_cls():
        return LuminoxConfig

    @staticmethod
    def default_com_cls():
        return LuminoxSerialCommunication

    def start(self) -> None:
        """
        Start this device. Opens the communication protocol.
        """

        logging.info(f"Starting device {self}")
        super().start()

    def stop(self) -> None:
        """
        Stop the device. Closes also the communication protocol.
        """

        logging.info(f"Stopping device {self}")
        super().stop()

    def _write(self, value: str) -> None:
        """
        Write given `value` string to `self.com`.

        :param value: String value to send.
        :raises SerialCommunicationIOError: when communication port is not opened
        """

        self.com.write_text(value)

    def _read(self) -> str:
        """
        Read a string value from `self.com`.

        :return: Read text from the serial port, without the trailing terminator,
            as defined in the communcation protocol configuration.
        :raises SerialCommunicationIOError: when communication port is not opened
        """
        return self.com.read_text().rstrip(self.com.config.terminator_str())

    def activate_output(self, mode: LuminoxOutputMode) -> None:
        """
        activate the selected output mode of the Luminox Sensor.
        :param mode: polling or streaming
        """
        self._write(f"M {mode.value}")
        # needs a little bit of time ot activate
        sleep(self.config.wait_sec_post_activate)

        if not self.com.read_text() == (
            f'M 0{mode.value}{self.com.config.terminator_str()}'
        ):
            err_msg = f"Stream mode activation was not possible {self}"
            logging.warning(err_msg)
            raise LuminoxOutputModeError(err_msg)

        self.output = mode
        logging.info(f"{mode.name} mode activated {self}")

    _read_stream_measurements_keys: Tuple[LuminoxMeasurementType, ...] = (
        LuminoxMeasurementType.partial_pressure_o2,  # type: ignore
        LuminoxMeasurementType.temperature_sensor,  # type: ignore
        LuminoxMeasurementType.barometric_pressure,  # type: ignore
        LuminoxMeasurementType.percent_o2,  # type: ignore
        LuminoxMeasurementType.sensor_status,  # type: ignore
    )

    def read_stream(self) -> dict:
        """
        read values of Luminox in stream mode. Convert the single string
        into sepearate numbers

        :return: dictionary with all values
        :raises LuminoxOutputModeError: when streaming mode is not activated
        :raises LuminoxMeasurementTypeError: when any of expected measurement values is
            not read
        """
        if not self.output == LuminoxOutputMode.streaming:
            err_msg = f"Streaming mode not activated {self}"
            logging.warning(err_msg)
            raise LuminoxOutputModeError(err_msg)

        read_txt = self._read()
        read_values_dict = {}
        for measurement in self._read_stream_measurements_keys:
            read_value = measurement.parse_read_measurement_value(read_txt)
            read_values_dict[measurement] = read_value
        return read_values_dict

    def query_single_measurement(
        self, measurement: Union[str, LuminoxMeasurementType],
    ) -> Union[float, int, str]:
        """
        query one single measurement value in polling mode.

        :param measurement: type of measurement
        :return: value of requested measurement
        :raises ValueError: when a wrong key for LuminoxMeasurementType is provided
        :raises LuminoxOutputModeError: when polling mode is not activated
        :raises LuminoxMeasurementTypeError: when expected measurement value is not read
        """
        if not isinstance(measurement, LuminoxMeasurementType):
            try:
                measurement = cast(
                    LuminoxMeasurementType,
                    LuminoxMeasurementType[measurement]  # type: ignore
                )
            except KeyError:
                measurement = cast(
                    LuminoxMeasurementType,
                    LuminoxMeasurementType(measurement)
                )

        if not self.output == LuminoxOutputMode.polling:
            err_msg = f"Polling mode not activated {self}"
            logging.warning(err_msg)
            raise LuminoxOutputModeError(err_msg)

        self._write(str(measurement))
        read_txt = self._read()
        read_value = measurement.parse_read_measurement_value(read_txt)
        return read_value
