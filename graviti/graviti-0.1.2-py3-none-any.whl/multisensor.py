#!/usr/bin/env python3
#
# Copyright 2020 Graviti. All Rights Reserved.
#

"""This file defines class Sensor, Frame and SensorType.
"""


from copy import deepcopy
from enum import Enum
from typing import Any, Dict, Optional

from .exceptions import GASParameterError

SensorType = Enum("SensorType", ("CAMERA", "FISHEYE_CAMERA", "LIDAR"))


class Sensor:
    """A class used to represent a type of sensor.
    Attributes of the sensor can be set through instance methods.

    :param name: The name to identify the sensor
    :param sensor_type: The type of the sensor indicating if it is a lidar or a camera
    """

    CAMERA = SensorType.CAMERA
    LIDAR = SensorType.LIDAR
    FISHEYE_CAMERA = SensorType.FISHEYE_CAMERA

    def __init__(self, name: str, sensor_type: SensorType) -> None:
        self._data: Dict[str, Any] = {
            "name": name,
            "type": sensor_type.name,
            "extrinsicParams": {},
            "intrinsicParams": {},
        }

    def set_description(self, description: str) -> None:
        """Set the description of the sensor.

        :param description: The description to be set for more detailed information of the sensor
        """
        self._data["desc"] = description

    # pylint: disable=invalid-name
    def set_translation(self, *, x: float, y: float, z: float) -> None:
        """Set the translation parameters of the sensor extrinsics.

        :param x: Translation along the x-axis
        :param y: Translation along the y-axis
        :param z: Translation along the z-axis
        """
        self._data["extrinsicParams"]["translation"] = {
            "x": x,
            "y": y,
            "z": z,
        }

    # pylint: disable=invalid-name
    def set_rotation(self, *, w: float, x: float, y: float, z: float) -> None:
        """Set the rotation parameters of the sensor extrinsics.
        Quaternion is used to describe the rotation of the sensor.

        :param w: W component of the quaternion
        :param x: X component of the quaternion
        :param y: Y component of the quaternion
        :param z: Z component of the quaternion
        """
        self._data["extrinsicParams"]["rotation"] = {
            "w": w,
            "x": x,
            "y": y,
            "z": z,
        }

    # pylint: disable=invalid-name
    def set_camera_matrix(
        self, *, fx: float, fy: float, cx: float, cy: float, skew: Optional[float] = 0
    ) -> None:
        """Set the camera_matrix parameters of sensor intrinsics.

        :param fx: fx parameter in camera matrix K
        :param fy: fy parameter in camera matrix K
        :param cx: cx parameter in camera matrix K
        :param cy: cy parameter in camera matrix K
        :param skew: skew parameter in camera matrix K
        """
        self._data["intrinsicParams"]["cameraMatrix"] = {
            "fx": fx,
            "fy": fy,
            "cx": cx,
            "cy": cy,
            "skew": skew,
        }

    # pylint: disable=invalid-name
    def set_distortion_coefficient(self, *, p1: float, p2: float, **kargs: float) -> None:
        """Set the distortion coefficients of the sensor intrinsics
        after checking the naming convention of radial distortion coefficients.

        :param p1: p1 parameter in tangential distortion coeffiecient
        :param p2: p2 parameter in tangential distortion coeffiecient
        :param kargs: Radial distortion coefficients with ['k1', 'k2', 'k3', ...] naming convention
        :raises GASParameterError: Radial distortion coefficients should have
                                   the correct naming convention
        """
        valid_key_number = 0
        for k_index in range(1, len(kargs) + 1):
            key = f"k{k_index}"
            if key in kargs:
                valid_key_number += 1
            else:
                break

        if valid_key_number != len(kargs):
            raise GASParameterError(
                f"Parameter {key} does not exist. Radial distortion coefficients "
                "should follow the ['k1', 'k2', 'k3', ...] naming convention."
            )

        self._data["intrinsicParams"]["distortionCoefficient"] = {
            "p1": p1,
            "p2": p2,
        }
        self._data["intrinsicParams"]["distortionCoefficient"].update(kargs)

    def dumps(self) -> Dict[str, Any]:
        """Returns all sensor information as a json formatted string.

        :return: A dictionary containing all the sensor information
        """
        return deepcopy(self._data)


class Frame:
    """A class used to represent a Frame consisting of multisensor data.
    """

    def __init__(self) -> None:
        """Constructor method
        """
        self._data: Dict[str, Dict[str, Any]] = {}

    # pylint: disable=too-many-arguments
    def add_data(
        self,
        sensor_name: str,
        local_path: str,
        remote_path: str,
        timestamp: float,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Add a frame of data acquired from a single sensor.

        :param sensor_name: The name of the sensor by which the data was acquired
        :param local_path: The local storage location of the data
        :param remote_path: The remote storage location of the data
        :param timestamp: The timestamp of the data as the acquisition time, specified in seconds
        :param metadata: A dict contains other information about the data
        """
        self._data[sensor_name] = {
            "objectPath": remote_path,
            "timestamp": timestamp,
            "filePath": local_path,
        }
        if metadata:
            self._data[sensor_name]["metadata"] = metadata

    def dumps(self) -> Dict[str, Dict[str, Any]]:
        """Returns all the data acquired from different sensors in this frame.

        :return: A dictionary containing all the frame information
        """
        return deepcopy(self._data)
