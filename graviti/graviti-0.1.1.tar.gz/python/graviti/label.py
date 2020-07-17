#!/usr/bin/env python3
#
# Copyright 2020 Graviti. All Rights Reserved.
#

"""This file defines class ValueType, TaskType, Label and LabelTable
"""

from copy import deepcopy
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from .shape import Shape

ValueType = Enum("ValueType", ("BOOL", "INT", "FLOAT", "STRING"))
TaskType = Enum(
    "TaskType",
    (
        "TASK_2D_BOX",
        "TASK_2D_BOX_TRACKING",
        "TASK_2D_POLYGON",
        "TASK_2D_CLASSIFICATION",
        "TASK_2D_KEYPOINT",
        "TASK_2D_LINE",
        "TASK_2D_CUBOID",
        "TASK_3D_BOX",
        "TASK_3D_BOX_TRACKING",
        "TASK_3D_SEGMENTATION",
        "TASK_FUSION_BOX",
        "TASK_FUSION_BOX_TRACKING",
    ),
)


class Label:
    """A class used to represent labels.

    :param remote_path: The remote location of the labels
    """

    def __init__(self, remote_path: str) -> None:
        self._data: Dict[str, Any] = {}
        self._data["objectPath"] = remote_path
        self._data["labelValues"] = {}

    def add_shape(
        self,
        shape: Shape,
        category: str,
        attributes: Dict[str, Any],
        instance: Optional[str] = None,
    ) -> None:
        """Add a label with certain shape to the Labels.

        :param shape: The shape information of the added label
        :param category: The category of the labeled object
        :param attributes: The attributes of the label
        :param instance: Instance ID of the labeled object in tracking tasks
        """
        shape_info = {shape.NAME: shape.dumps(), "category": category, "attributes": attributes}
        if instance:
            shape_info["instance"] = instance
        key = f"labels_{shape.NAME}"
        self._data["labelValues"].setdefault(key, []).append(shape_info)

    def add_classification(self, category: str, attributes: Dict[str, Any]) -> None:
        """Add classification label to the list.

        :param category: The category of the classification label
        :param attributes: The attributes of the label
        """
        self._data["labelValues"]["labels_classification"] = {
            "category": category,
            "attributes": attributes,
        }

    def dumps(self) -> Dict[str, Any]:
        """Returns the information of all the labels.

        :return: A dictionary containing all the information of the labels
        """
        return deepcopy(self._data)


class LabelTable:
    """A class used to represent the standard of the labels in a certain task.
    """

    def __init__(self) -> None:
        self._data: Dict[str, Any] = {}
        self._data["label_namespace"] = "Graviti"
        self._data["categories"] = []
        self._data["attributes"] = []

    def set_label_namespace(self, namespace: str) -> None:
        """Set the namespace of the label table.

        :param namespace: The namespace of the label table
        """
        self._data["label_namespace"] = namespace

    def set_task_type(self, task_type: TaskType) -> None:
        """Set the task type of the label table.

        :param task_type: The task_type of the label table
        """
        self._data["task_type"] = task_type.name

    def set_description(self, description: str) -> None:
        """Set the description of the label table.

        :param description: More detailed description of the label table
        """
        self._data["desciption"] = description

    def add_category(self, name: str, *, description: Optional[str]) -> None:
        """Add a label category to the table.

        :param name: The name of the label to be added
        :param description: The description of the label category
        """
        category_info = {"name": name}
        if description:
            category_info["description"] = description
        self._data["categories"].append(category_info)

    def add_attribute(
        self,
        name: str,
        values: Union[ValueType, List[str]],
        *,
        description: Optional[str] = None,
        parent_categories: Union[None, str, List[str]] = None,
    ) -> None:
        """Add the label attribute to the label table.

        :param name: The name of the attribute to be added
        :param values: The values that the attribute can be set
        :param description: The description of the attribute
        :param parent_categories: The name of the category which the attribute belongs to
        """
        attributes_info: Dict[str, Union[str, List[str]]] = {
            "name": name,
        }
        # pylint: disable=isinstance-second-argument-not-valid-type
        if isinstance(values, ValueType):
            attributes_info["values"] = values.name
        else:
            attributes_info["values"] = values
        if description:
            attributes_info["description"] = description
        if isinstance(parent_categories, list):
            attributes_info["parent_categories"] = parent_categories
        elif parent_categories:
            attributes_info["parent_categories"] = [parent_categories]
        self._data["attributes"].append(attributes_info)

    def dumps(self) -> Dict[str, Any]:
        """Returns all the information of the label table.

        :return: A dictionary containing all the label table information
        """
        return deepcopy(self._data)
