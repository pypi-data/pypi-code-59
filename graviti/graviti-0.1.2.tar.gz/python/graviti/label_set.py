#!/usr/bin/env python3
#
# Copyright 2020 Graviti. All Rights Reserved.
#

"""This file defines the class LabelSet.
"""

from typing import Any, Dict, Optional

from .client import post
from .label import Label, LabelTable


class LabelSet:
    """A class used to respresent label set.

    :param label_set_id: The id of the label set
    :param label_set_client: The client of the label set
    """

    PUBLISH_STATUS = 2
    TYPE_GROUND_TRUTH = 3

    def __init__(self, label_set_id: str, gateway_url: str, access_key: str) -> None:
        self._label_set_id = label_set_id
        self._gateway_url = gateway_url
        self._access_key = access_key

    def get_label_set_id(self) -> str:
        """Return the id of the label set.

        :return: The id of the label set
        """
        return self._label_set_id

    def upload_label_table(self, label_table: LabelTable) -> None:
        """Upload label table to the label set.

        :param label_table: The label table to be uploaded
        """
        post_data = {
            "labelSetId": self._label_set_id,
            "meta": label_table.dumps(),
        }
        self._label_set_post("updateLableSet", post_data)

    def upload_label(self, label: Label, metadata: Optional[Dict[str, Any]] = None) -> None:
        """Upload label to the label set.

        :param label: The label to be uploaded
        :param metadata: Some additional data of the label
        """
        post_data = label.dumps()
        post_data["labelSetId"] = self._label_set_id
        if metadata:
            post_data["labelMeta"] = metadata
        self._label_set_post("putLabel", post_data)

    def publish(self) -> None:
        """Publish the label set.
        """
        post_data = {"labelSetId": self._label_set_id, "status": LabelSet.PUBLISH_STATUS}
        self._label_set_post("updateLabelSetStatus", post_data)

    def _label_set_post(self, method: str, post_data: Dict[str, Any]) -> Any:
        url = self._gateway_url + "label-store/" + method
        return post(url, json_data=post_data, access_key=self._access_key)
