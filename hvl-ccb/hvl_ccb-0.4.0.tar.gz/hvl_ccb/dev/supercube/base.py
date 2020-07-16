#  Copyright (c) 2019-2020 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Base classes for the Supercube device.
"""

import logging
import time
from collections import deque
from concurrent.futures import ThreadPoolExecutor, Future
from datetime import datetime
from itertools import cycle
from threading import Event
from time import sleep
from typing import Callable, List, Optional, Sequence, Tuple, Union

from opcua import Node

from . import constants
from ..base import SingleCommDevice
from ...comm import (
    OpcUaCommunication,
    OpcUaCommunicationConfig,
    OpcUaSubHandler,
)
from ...configuration import configdataclass

Number = Union[int, float]


class SupercubeEarthingStickOperationError(Exception):
    pass


class SupercubeSubscriptionHandler(OpcUaSubHandler):
    """
    OPC Subscription handler for datachange events and normal events specifically
    implemented for the Supercube devices.
    """

    def datachange_notification(self, node: Node, val, data):
        """
        In addition to the standard operation (debug logging entry of the datachange),
        alarms are logged at INFO level using the alarm text.

        :param node: the node object that triggered the datachange event
        :param val: the new value
        :param data:
        """

        super().datachange_notification(node, val, data)

        # assume an alarm datachange
        try:
            alarm_number = constants.Alarms(node.nodeid.Identifier).number
            alarm_text = constants.AlarmText.get(alarm_number)
            alarm_log_prefix = "Coming" if val else "Going"
            logging.getLogger(__name__).info(
                f"{alarm_log_prefix} Alarm {alarm_number}: {str(alarm_text)}"
            )
            return
        except ValueError:
            # not any of Alarms node IDs
            pass

        id_ = node.nodeid.Identifier

        # assume a status datachange
        if id_ == str(constants.Safety.status):
            new_status = str(constants.SafetyStatus(val))
            logging.getLogger(__name__).info(f"Safety: {new_status}")
            return

        # assume an earthing stick status datachange
        if id_ in constants.EarthingStick.statuses():
            new_status = str(constants.EarthingStickStatus(val))
            logging.getLogger(__name__).info(
                f"Earthing {constants.EarthingStick(id_).number}: {new_status}"
            )
            return


class Poller:
    """
    Poller class wrapping `concurrent.futures.ThreadPoolExecutor` which enables passing
    of results and errors out of the polling thread.
    """

    def __init__(
        self,
        spoll_handler: Callable,
        polling_delay_sec: Number = 0,
        polling_interval_sec: Number = 1,
        polling_timeout_sec: Optional[Number] = None,
    ):
        """
        Initialize the polling helper.

        :param spoll_handler: Polling function.
        :param polling_delay_sec: Delay before starting the polling, in seconds.
        :param polling_interval_sec: Polling interval, in seconds.
        """
        self.spoll_handler: Callable = spoll_handler
        self.polling_delay_sec: Number = polling_delay_sec
        self.polling_interval_sec: Number = polling_interval_sec
        self.polling_timeout_sec: Optional[Number] = polling_timeout_sec
        self._polling_future: Optional[Future] = None
        self._polling_stop_event: Optional[Event] = None

    def is_polling(self) -> bool:
        """
        Check if device status is being polled.

        :return: `True` when polling thread is set and alive
        """
        return self._polling_future is not None and self._polling_future.running()

    def _if_poll_again(
        self, stop_event: Event, delay_sec: Number, stop_time: Optional[Number]
    ) -> bool:
        """
        Check if to poll again.

        :param stop_event: Polling stop event.
        :param delay_sec: Delay time (in seconds).
        :param stop_time: Absolute stop time.
        :return: `True` if another polling handler call is due, `False` otherwise.
        """
        not_stopped = not stop_event.wait(delay_sec)
        not_timeout = stop_time is None or time.time() < stop_time
        return not_stopped and not_timeout

    def _poll_until_stop_or_timeout(self, stop_event: Event) -> Optional[object]:
        """
        Thread for polling until stopped or timed-out.

        :param stop_event: Event used to stop the polling
        :return: Last result of the polling function call
        """
        start_time = time.time()
        stop_time = (
            (start_time + self.polling_timeout_sec)
            if self.polling_timeout_sec
            else None
        )
        last_result = None

        if self._if_poll_again(stop_event, self.polling_delay_sec, stop_time):
            last_result = self.spoll_handler()

        while self._if_poll_again(stop_event, self.polling_interval_sec, stop_time):
            last_result = self.spoll_handler()

        return last_result

    def start_polling(self) -> bool:
        """
        Start polling.

        :return: `True` if was not polling before, `False` otherwise
        """
        was_not_polling = not self.is_polling()

        if was_not_polling:
            logging.info("Start polling")
            self._polling_stop_event = Event()
            pool = ThreadPoolExecutor(max_workers=1)
            self._polling_future = pool.submit(
                self._poll_until_stop_or_timeout, self._polling_stop_event
            )

        return was_not_polling

    def stop_polling(self) -> Tuple[bool, Optional[object]]:
        """
        Stop polling.

        Wait for until polling function returns a result as well as any exception that
        might have been raised within a thread.

        :return: `True` if was polling before, `False` otherwise, and last result of
            the polling function call.
        :raises: polling function exceptions
        """
        was_polling = self.is_polling()
        results = None

        if was_polling:
            logging.info("Stop polling")
            if self._polling_stop_event is None:
                raise RuntimeError("Was polling but stop event is missing.")
            self._polling_stop_event.set()
            if self._polling_future is None:
                raise RuntimeError("Was polling but polling future is missing.")
            results = self._polling_future.result()

        return was_polling, results


@configdataclass
class SupercubeConfiguration:
    """
    Configuration dataclass for the Supercube devices.
    """

    #: Namespace of the OPC variables, typically this is 3 (coming from Siemens)
    namespace_index: int = 3

    polling_delay_sec: Number = 5.0
    polling_interval_sec: Number = 1.0

    def clean_values(self):
        if self.namespace_index < 0:
            raise ValueError(
                "Index of the OPC variables namespace needs to be a positive integer."
            )
        if self.polling_interval_sec <= 0:
            raise ValueError("Polling interval needs to be positive.")
        if self.polling_delay_sec < 0:
            raise ValueError("Polling delay needs to be not negative.")


@configdataclass
class SupercubeOpcUaCommunicationConfig(OpcUaCommunicationConfig):
    """
    Communication protocol configuration for OPC UA, specifications for the Supercube
    devices.
    """

    #: Subscription handler for data change events
    sub_handler: OpcUaSubHandler = SupercubeSubscriptionHandler()


class SupercubeOpcUaCommunication(OpcUaCommunication):
    """
    Communication protocol specification for Supercube devices.
    """

    @staticmethod
    def config_cls():
        return SupercubeOpcUaCommunicationConfig


class SupercubeBase(SingleCommDevice):
    """
    Base class for Supercube variants.
    """

    def __init__(self, com, dev_config=None):
        """
        Constructor for Supercube base class.

        :param com: the communication protocol or its configuration
        :param dev_config: the device configuration
        """

        super().__init__(com, dev_config)

        self.status_poller = Poller(
            self._spoll_handler,
            polling_delay_sec=self.config.polling_delay_sec,
            polling_interval_sec=self.config.polling_interval_sec,
        )
        self.toggle = cycle([False, True])
        self.logger = logging.getLogger(__name__)
        self.message_len = len(constants.MessageBoard)
        self.status_board = [""] * self.message_len
        self.message_board = deque([""] * self.message_len, maxlen=self.message_len)

    @staticmethod
    def default_com_cls():
        return SupercubeOpcUaCommunication

    def start(self) -> None:
        """
        Starts the device. Sets the root node for all OPC read and write commands to
        the Siemens PLC object node which holds all our relevant objects and variables.
        """

        self.logger.info("Starting Supercube Base device")
        super().start()

        self.logger.debug("Add monitoring nodes")
        self.com.init_monitored_nodes(
            map(  # type: ignore
                str, constants.GeneralSockets
            ),
            self.config.namespace_index,
        )
        self.com.init_monitored_nodes(
            map(  # type: ignore
                str, constants.GeneralSupport
            ),
            self.config.namespace_index,
        )
        self.com.init_monitored_nodes(
            map(  # type: ignore
                str, constants.Safety
            ),
            self.config.namespace_index,
        )
        self.com.init_monitored_nodes(
            str(constants.Errors.message), self.config.namespace_index
        )
        self.com.init_monitored_nodes(
            str(constants.Errors.warning), self.config.namespace_index
        )
        self.com.init_monitored_nodes(
            str(constants.Errors.stop), self.config.namespace_index
        )
        self.com.init_monitored_nodes(
            map(str, constants.Alarms), self.config.namespace_index
        )
        self.com.init_monitored_nodes(
            map(  # type: ignore
                str, constants.EarthingStick
            ),
            self.config.namespace_index,
        )

        self.set_remote_control(True)
        self.logger.debug("Finished starting")

    def stop(self) -> None:
        """
        Stop the Supercube device. Deactivates the remote control and closes the
        communication protocol.
        """
        try:
            self.set_remote_control(False)
        finally:
            super().stop()

    def _spoll_handler(self) -> None:
        """
        Supercube poller handler; change one byte on a SuperCube.
        """
        self.write(constants.OpcControl.live, next(self.toggle))

    @staticmethod
    def config_cls():
        return SupercubeConfiguration

    def read(self, node_id: str):
        """
        Local wrapper for the OPC UA communication protocol read method.

        :param node_id: the id of the node to read.
        :return: the value of the variable
        """

        self.logger.debug(f"Read from node ID {node_id} ...")
        result = self.com.read(str(node_id), self.config.namespace_index)
        self.logger.debug(f"Read from node ID {node_id}: {result}")
        return result

    def write(self, node_id, value) -> None:
        """
        Local wrapper for the OPC UA communication protocol write method.

        :param node_id: the id of the node to read
        :param value: the value to write to the variable
        """
        self.logger.debug(f"Write to node ID {node_id}: {value}")
        self.com.write(str(node_id), self.config.namespace_index, value)

    def set_remote_control(self, state: bool) -> None:
        """
        Enable or disable remote control for the Supercube. This will effectively
        display a message on the touchscreen HMI.

        :param state: desired remote control state
        """
        can_write = False
        try:
            self.write(constants.OpcControl.active, bool(state))
            can_write = True
        finally:
            if state:
                if not can_write:
                    self.logger.warning("Remote control cannot be enabled")
                else:
                    was_not_polling = self.status_poller.start_polling()
                    if not was_not_polling:
                        self.logger.warning("Remote control already enabled")
            else:
                # ignore result (is None)
                was_polling = self.status_poller.stop_polling()[0]
                if not was_polling:
                    self.logger.warning("Remote control already disabled")

    def get_support_input(self, port: int, contact: int) -> bool:
        """
        Get the state of a support socket input.

        :param port: is the socket number (1..6)
        :param contact: is the contact on the socket (1..2)
        :return: digital input read state
        :raises ValueError: when port or contact number is not valid
        """

        return bool(self.read(constants.GeneralSupport.input(port, contact)))

    def get_support_output(self, port: int, contact: int) -> bool:
        """
        Get the state of a support socket output.

        :param port: is the socket number (1..6)
        :param contact: is the contact on the socket (1..2)
        :return: digital output read state
        :raises ValueError: when port or contact number is not valid
        """

        return bool(self.read(constants.GeneralSupport.output(port, contact)))

    def set_support_output(self, port: int, contact: int, state: bool) -> None:
        """
        Set the state of a support output socket.

        :param port: is the socket number (1..6)
        :param contact: is the contact on the socket (1..2)
        :param state: is the desired state of the support output
        :raises ValueError: when port or contact number is not valid
        """

        self.write(constants.GeneralSupport.output(port, contact), bool(state))

    def set_support_output_impulse(
        self, port: int, contact: int, duration: float = 0.2, pos_pulse: bool = True
    ) -> None:
        """
        Issue an impulse of a certain duration on a support output contact. The polarity
        of the pulse (On-wait-Off or Off-wait-On) is specified by the pos_pulse
        argument.

        This function is blocking.

        :param port: is the socket number (1..6)
        :param contact: is the contact on the socket (1..2)
        :param duration: is the length of the impulse in seconds
        :param pos_pulse: is True, if the pulse shall be HIGH, False if it shall be LOW
        :raises ValueError: when port or contact number is not valid
        """

        self.set_support_output(port, contact, pos_pulse)
        sleep(duration)
        self.set_support_output(port, contact, not pos_pulse)

    def get_t13_socket(self, port: int) -> bool:
        """
        Read the state of a SEV T13 power socket.

        :param port: is the socket number, one of `constants.T13_SOCKET_PORTS`
        :return: on-state of the power socket
        :raises ValueError: when port is not valid
        """

        if port not in constants.T13_SOCKET_PORTS:
            raise ValueError(f"port not in {constants.T13_SOCKET_PORTS}: {port}")

        return bool(self.read(getattr(constants.GeneralSockets, f"t13_{port}")))

    def set_t13_socket(self, port: int, state: bool) -> None:
        """
        Set the state of a SEV T13 power socket.

        :param port: is the socket number, one of `constants.T13_SOCKET_PORTS`
        :param state: is the desired on-state of the socket
        :raises ValueError: when port is not valid or state is not of type bool
        """

        if not isinstance(state, bool):
            raise ValueError(f"state is not <bool>: {state}")

        if port not in constants.T13_SOCKET_PORTS:
            raise ValueError(f"port not in {constants.T13_SOCKET_PORTS}: {port}")

        self.write(getattr(constants.GeneralSockets, f"t13_{port}"), state)

    def get_cee16_socket(self) -> bool:
        """
        Read the on-state of the IEC CEE16 three-phase power socket.

        :return: the on-state of the CEE16 power socket
        """

        return bool(self.read(constants.GeneralSockets.cee16))

    def set_cee16_socket(self, state: bool) -> None:
        """
        Switch the IEC CEE16 three-phase power socket on or off.

        :param state: desired on-state of the power socket
        :raises ValueError: if state is not of type bool
        """

        if not isinstance(state, bool):
            raise ValueError(f"state is not <bool>: {state}")

        self.write(constants.GeneralSockets.cee16, state)

    def get_status(self) -> constants.SafetyStatus:
        """
        Get the safety circuit status of the Supercube.
        :return: the safety status of the supercube's state machine.
        """

        return constants.SafetyStatus(self.read(constants.Safety.status))

    def ready(self, state: bool) -> None:
        """
        Set ready state. Ready means locket safety circuit, red lamps, but high voltage
        still off.

        :param state: set ready state
        """

        self.write(constants.Safety.switch_to_ready, state)

    def operate(self, state: bool) -> None:
        """
        Set operate state. If the state is RedReady, this will turn on the high
        voltage and close the safety switches.

        :param state: set operate state
        """

        self.write(constants.Safety.switch_to_operate, state)

    def get_measurement_ratio(self, channel: int) -> float:
        """
        Get the set measurement ratio of an AC/DC analog input channel. Every input
        channel has a divider ratio assigned during setup of the Supercube system.
        This ratio can be read out.

        :param channel: number of the input channel (1..4)
        :return: the ratio
        :raises ValueError: when channel is not valid
        """

        return float(self.read(constants.MeasurementsDividerRatio.input(channel)))

    def get_measurement_voltage(self, channel: int) -> float:
        """
        Get the measured voltage of an analog input channel. The voltage read out
        here is already scaled by the configured divider ratio.

        :param channel: number of the input channel (1..4)
        :return: measured voltage
        :raises ValueError: when channel is not valid
        """

        return float(self.read(constants.MeasurementsScaledInput.input(channel)))

    def get_earthing_stick_status(self, number: int) -> constants.EarthingStickStatus:
        """
        Get the status of an earthing stick, whether it is closed, open or undefined
        (moving).

        :param number: number of the earthing stick (1..6)
        :return: earthing stick status
        :raises ValueError: when earthing stick number is not valid
        """

        return constants.EarthingStickStatus(
            self.read(constants.EarthingStick.status(number))
        )

    def get_earthing_stick_operating_status(
        self, number: int
    ) -> constants.EarthingStickOperatingStatus:
        """
        Get the operating status of an earthing stick.

        :param number: number of the earthing stick (1..6)
        :return: earthing stick operating status (auto == 0, manual == 1)
        :raises ValueError: when earthing stick number is not valid
        """
        return constants.EarthingStickOperatingStatus(
            self.read(constants.EarthingStick.operating_status(number))
        )

    def get_earthing_stick_manual(
        self, number: int
    ) -> constants.EarthingStickOperation:
        """
        Get the manual status of an earthing stick. If an earthing stick is set to
        manual, it is closed even if the system is in states RedReady or RedOperate.

        :param number: number of the earthing stick (1..6)
        :return: operation of the earthing stick in a manual operating mode (open == 0,
            close == 1)
        :raises ValueError: when earthing stick number is not valid
        """
        return constants.EarthingStickOperation(
            int(self.read(constants.EarthingStick.manual(number)))
        )

    def operate_earthing_stick(
        self, number: int, operation: constants.EarthingStickOperation
    ) -> None:
        """
        Operation of an earthing stick, which is set to manual operation. If an earthing
        stick is set to manual, it stays closed even if the system is in states
        RedReady or RedOperate.

        :param number: number of the earthing stick (1..6)
        :param operation: earthing stick manual status (close or open)
        :raises SupercubeEarthingStickOperationError: when operating status of given
            number's earthing stick is not manual
        """

        if (
            self.get_earthing_stick_operating_status(number)
            == constants.EarthingStickOperatingStatus.manual
        ):
            self.write(constants.EarthingStick.manual(number), bool(operation.value))
        else:
            raise SupercubeEarthingStickOperationError

    def quit_error(self) -> None:
        """
        Quits errors that are active on the Supercube.
        """

        self.write(constants.Errors.quit, True)
        sleep(0.1)
        self.write(constants.Errors.quit, False)

    def get_door_status(self, door: int) -> constants.DoorStatus:
        """
        Get the status of a safety fence door. See :class:`constants.DoorStatus` for
        possible returned door statuses.

        :param door: the door number (1..3)
        :return: the door status
        """

        return constants.DoorStatus(self.read(constants.Door.status(door)))

    def set_status_board(
        self, msgs: List[str],
        pos: List[int] = None,
        clear_board: bool = True,
        display_board: bool = True,
    ) -> None:
        """
        Sets and displays a status board. The messages and the position of the message
        can be defined.

        :param msgs: list of strings
        :param pos: list of integers [0...14]
        :param clear_board: clear unspecified lines if `True` (default), keep otherwise
        :param display_board: display new status board if `True` (default)
        :raises ValueError: if there are too many messages or the positions indices are
            invalid.
        """
        # validate inputs
        if len(msgs) > self.message_len:
            raise ValueError(
                f"Too many message: {len(msgs)} given, max. {self.message_len} allowed."
            )
        if pos and not all(0 < p < self.message_len for p in pos):
            raise ValueError(f"Messages positions out of 0...{self.message_len} range")

        if clear_board:
            self.status_board = [""] * self.message_len

        # update status board
        if not pos:
            pos = list(range(len(msgs)))
        for num, msg in zip(pos, msgs):
            self.status_board[num] = msg
        if display_board:
            self.display_status_board()

    def display_status_board(self) -> None:
        """
        Display status board.
        """
        return self._display_messages(self.status_board)

    def set_message_board(self, msgs: List[str], display_board: bool = True) -> None:
        """
        Fills messages into message board that display that 15 newest messages with
        a timestamp.

        :param msgs: list of strings
        :param display_board: display 15 newest messages if `True` (default)
        :raises ValueError: if there are too many messages or the positions indices are
            invalid.
        """
        # validate inputs
        if len(msgs) > self.message_len:
            raise ValueError(
                f"Too many message: {len(msgs)} given, max. {self.message_len} allowed."
            )

        timestamp = datetime.now().time().strftime("%H:%M:%S")
        # append messages in the same order as given, not reversed
        self.message_board.extendleft(
            f"{timestamp}: {msg}" for msg in reversed(msgs)
        )

        if display_board:
            self.display_message_board()

    def display_message_board(self) -> None:
        """
        Display 15 newest messages
        """
        return self._display_messages(self.message_board)

    def _display_messages(self, messages: Sequence[str]) -> None:
        """
        Display given messages on message board

        :param messages: sequence of messages to display
        """
        # Note: cannot zip(constants.MessageBoard, messages) as enum instances are
        #       sorted by name, hence after after `line_1` comes `line_10`, not `line_2`
        for n, msg in enumerate(messages):
            line = constants.MessageBoard.line(n+1)
            self.write(line, msg)
