#!/usr/bin/env python3
#
# Copyright 2020 Graviti. All Rights Reserved.
#

"""This file defines class DataSet."""

import base64
import json
import os
import threading
import time
import uuid
from copy import deepcopy
from typing import Any, Dict, List, Optional, Tuple, Union

import filetype
from requests_toolbelt import MultipartEncoder

from .client import post
from .exceptions import GASException
from .label_set import LabelSet
from .multisensor import Frame, Sensor


class DataSet:
    """This class defines the concept of a data set and some operations on it."""

    PERMISSION_CATEGORY: str
    PUBLISH_STATUS = 7

    def __init__(self, data_set_id: str, gateway_url: str, access_key: str) -> None:
        self._data_set_id = data_set_id
        self._gateway_url = gateway_url
        self._access_key = access_key
        self._permission = {"expireAt": 0}
        self._permission_lock = threading.Lock()
        self._expired_in_second = 60

    def upload_description(
        self,
        description: Optional[str] = None,
        collection_time: Optional[str] = None,
        collection_location: Optional[str] = None,
    ) -> None:
        """Upload description of the data set.

        :param description: description of the data set to upload
        :param collection_time: collected time of the data set to upload
        :param collection_location: collected location of the data set to upload
        """
        post_data = {}
        if description:
            post_data["desc"] = description
        if collection_time:
            post_data["collectedAt"] = collection_time
        if collection_location:
            post_data["collectedLocation"] = collection_location

        if not post_data:
            return

        post_data["contentSetId"] = self._data_set_id
        self._data_set_post("updateContentSet", post_data)

    def get_data_set_id(self) -> str:
        """Get the id of this data set."""
        return self._data_set_id

    def create_label_set(
        self, remote_paths: List[str], label_set_type: int = LabelSet.TYPE_GROUND_TRUTH
    ) -> LabelSet:
        """Create a label set.

        :param remote_paths: A list of remote paths
        :param label_set_type: the type of the label set to be created
        :return: Created label set
        """
        post_data = {
            "contentSetId": self._data_set_id,
            "objectPaths": remote_paths,
            "type": label_set_type,
            "version": "v1.0.2",
        }
        data = self._label_set_post("createLabelSet", post_data)
        label_set_id = data["labelSetId"]
        return LabelSet(label_set_id, self._gateway_url, self._access_key)

    def delete_label_set(self, label_set_id: str) -> None:
        """Delete a label set according to a label set id.

        :param label_set_id: The id of the label set to be deleted
        """
        post_data = {"labelSetId": label_set_id}
        self._label_set_post("deleteLabelSet", post_data)

    def list_label_sets(self) -> List[str]:
        """List ids of all label sets of the data set.

        :return: A list of label sets ids
        """
        label_set_ids = []
        for summary in self._list_label_set_summaries():
            label_set_ids.append(summary["id"])
        return label_set_ids

    def publish(self) -> None:
        """Publish a data set."""
        post_data = {"contentSetId": self._data_set_id, "status": DataSet.PUBLISH_STATUS}
        self._data_set_post("updateContentSet", post_data)

    def _list_label_set_summaries(self) -> List[Any]:
        """List summaries of all label sets.

        :return: A list of dictionaries containing all the label set summaries.
        """
        post_data = {"contentSetId": self._data_set_id}
        data = self._label_set_post("listLabelSetSummaries", post_data)
        return data["labelSetSummaries"]  # type: ignore[no-any-return]

    def _get_upload_permission(self) -> Dict[str, Any]:
        with self._permission_lock:
            if int(time.time()) >= self._permission["expireAt"]:
                post_data = {
                    "id": self._data_set_id,
                    "category": self.PERMISSION_CATEGORY,
                    "expiredInSec": self._expired_in_second,
                }
                self._permission = self._data_set_post("getPutPermission", post_data)

            return deepcopy(self._permission)

    def _clear_upload_permission(self) -> None:
        with self._permission_lock:
            self._permission = {"expireAt": 0}

    def _data_set_post(self, method: str, post_data: Dict[str, Any]) -> Any:
        url = self._gateway_url + "content-store/" + method
        return post(url, json_data=post_data, access_key=self._access_key)

    @staticmethod
    def _post_multipart_formdata(url: str, data: Dict[str, Any]) -> None:
        multipart = MultipartEncoder(data)
        post(url, data=multipart, content_type=multipart.content_type)

    def _label_set_post(self, method: str, post_data: Dict[str, Any]) -> Any:
        url = self._gateway_url + "label-store/" + method
        return post(url, json_data=post_data, access_key=self._access_key)

    @staticmethod
    def _file_tuple(local_path: str, remote_path: str) -> Tuple[str, bytes, Optional[str]]:
        """Get the file tuple which 'multipart/form-data' needs.

        :param local_path: The local path of the data to upload
        :param remote_path: The path to save the data in data set
        :return: 3-tuple ('filename', fileobj, 'content_type') of the input file
        """
        with open(local_path, "rb") as file:
            return (remote_path, file.read(), filetype.guess_mime(local_path))


class NormalDataSet(DataSet):
    """Normal data set has only one sensor, supporting upload_data method."""

    PERMISSION_CATEGORY = "contentSet"

    def upload_data(self, local_path: str, remote_path: str) -> None:
        """Upload data with local path to the data set.

        :param local_path: The local path of the data to upload
        :param remote_path: The path to save the data in data set
        """
        permission = self._get_upload_permission()
        post_data = permission["result"]
        post_data["key"] = permission["extra"]["objectPrefix"] + remote_path
        post_data["file"] = self._file_tuple(local_path, remote_path)

        try:
            self._post_multipart_formdata(permission["extra"]["host"], post_data)
        except GASException:
            self._clear_upload_permission()
            raise

    def delete_data(self, remote_path_list: List[str]) -> None:
        """Delete data with remote paths.

        :param remote_path_list: Remote path list you want to delete, eg: [test/os1.png]
        """
        post_data = {"contentSetId": self._data_set_id, "filePaths": remote_path_list}
        self._data_set_post("deleteObjects", post_data)

    def list_data(self) -> List[str]:
        """List all data in a data set.

        :return: A list of data path
        """
        post_data = {"contentSetId": self._data_set_id}
        data = self._data_set_post("listObjects", post_data)
        return data["objects"]  # type: ignore[no-any-return]


class MultiSensorDataSet(DataSet):
    """Multi-sensor data set has multiple sensors,
    supporting upload_sensor and upload_frame method.
    """

    PERMISSION_CATEGORY = "frame"

    def upload_sensor(self, sensor: Sensor) -> None:
        """Upload sensor to the data set.

        :param sensor: The sensor to upload
        """
        post_data = sensor.dumps()
        post_data["contentSetId"] = self._data_set_id
        self._data_set_post("createOrUpdateSensor", post_data)

    def delete_sensors(self, sensor_names: Union[str, List[str]]) -> None:
        """Delete sensors with a single name or a name list.

        :param sensor_names: A single sensor name or a list of sensor names
        """
        if not isinstance(sensor_names, list):
            sensor_names = [sensor_names]
        post_data = {"contentSetId": self._data_set_id, "sensorNames": sensor_names}
        self._data_set_post("deleteSensors", post_data)

    def list_sensors(self) -> List[str]:
        """List all sensor names in a data set.

        :return: A list of sensor name
        """
        post_data = {"contentSetId": self._data_set_id}
        data = self._data_set_post("listSensors", post_data)
        sensor_names: List[str] = []
        for sensor_info in data["sensors"]:
            sensor_names.append(sensor_info["name"])
        return sensor_names

    def upload_frame(self, frame: Frame) -> None:
        """Upload frame to the data set.

        :param frame: The frame to upload
        """

        frame_id = str(uuid.uuid4())

        for sensor_name, file_info in frame.dumps().items():
            permission = self._get_upload_permission()
            post_data = permission["result"]
            remote_path = os.path.join(sensor_name, file_info["objectPath"])

            post_data["key"] = permission["extra"]["objectPrefix"] + remote_path
            post_data["x:incidental"] = base64.urlsafe_b64encode(
                json.dumps(
                    {
                        "timestamp": file_info["timestamp"],
                        "sensorName": sensor_name,
                        "frameId": frame_id,
                        "objectPath": remote_path,
                    }
                ).encode()
            ).decode()

            post_data["file"] = self._file_tuple(file_info["filePath"], file_info["objectPath"])
            try:
                self._post_multipart_formdata(permission["extra"]["host"], post_data)
            except GASException:
                self._clear_upload_permission()
                raise

    # def list_frames(self) -> Any:
    #     """List all frames in a data set.
    #
    #     :return: A list of frames, each frame contains multiple sensors
    #     """
    #     post_data = json.dumps({
    #         "contentSetId": self._data_set_id,
    #     })
    #     data = self._data_set_post("listFrames", post_data)
    #     return data["frames"]
