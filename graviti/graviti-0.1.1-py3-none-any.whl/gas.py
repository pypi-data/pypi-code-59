#!/usr/bin/env python3
#
# Copyright 2020 Graviti. All Rights Reserved.
#

"""This file defines class GAS."""

from typing import Any, Dict, List, Optional, overload

from typing_extensions import Literal

from .client import post
from .data_set import DataSet, MultiSensorDataSet, NormalDataSet
from .exceptions import GASDataSetError, GASDataSetTypeError


class GAS:
    """This is a class defining the concept of a data center.
    It mainly defines some operations on data sets.

    :param user_name: user's name
    :param user_password: user'access_keyt_tag: client's tag
    :param url: the url of the gas website
    """

    def __init__(self, access_key: str, url: str = "https://gas.graviti.cn/") -> None:
        if url.endswith("/"):
            self._gateway_url = url + "gatewayv2/"
        else:
            self._gateway_url = url + "/gatewayv2/"

        self._access_key = access_key

    @overload
    def create_data_set(self, name: str, is_multisensor: Literal[False] = False) -> NormalDataSet:
        ...

    @overload
    def create_data_set(self, name: str, is_multisensor: Literal[True]) -> MultiSensorDataSet:
        ...

    @overload
    def create_data_set(self, name: str, is_multisensor: bool) -> DataSet:
        ...

    def create_data_set(self, name: str, is_multisensor: bool = False) -> DataSet:
        """Create a data set according to its name.

        :param name: Data set name, unique for a user
        :param is_multisensor: if True, create a MultiSensorDataSet;
            if False, create a NormalDataSet
        :return: Created data set
        """
        post_data = {
            "name": name,
            "contentSetType": int(is_multisensor),  # normal: 0, multisensor: 1
        }
        data = self._data_set_post("createContentSet", post_data)
        data_set_id = data["contentSetId"]
        ReturnType = MultiSensorDataSet if is_multisensor else NormalDataSet
        return ReturnType(data_set_id, self._gateway_url, self._access_key)

    @overload
    def get_data_set(self, name: str, is_multisensor: Literal[False] = False) -> NormalDataSet:
        ...

    @overload
    def get_data_set(self, name: str, is_multisensor: Literal[True]) -> MultiSensorDataSet:
        ...

    @overload
    def get_data_set(self, name: str, is_multisensor: bool) -> DataSet:
        ...

    def get_data_set(self, name: str, is_multisensor: bool = False) -> DataSet:
        """Get a data set according to its name.

        :param name: The name of the desired data set
        :param is_multisensor: if True, get a MultiSensorDataSet; if False, get a NormalDataSet
        :raises GASDataSetError: When the required data set does not exist
        :raises GASDataSetTypeError: When required data set type is inconsistent with actual type
        :return: The desired data set
        """
        data_sets_info = self._list_data_sets_info(name)
        if not data_sets_info:
            raise GASDataSetError(name)

        ReturnType = MultiSensorDataSet if is_multisensor else NormalDataSet

        if is_multisensor != data_sets_info[0]["contentSetResp"]["contentSetType"]:
            raise GASDataSetTypeError(name, str(ReturnType))

        data_set_id = data_sets_info[0]["contentSetResp"]["contentSetId"]
        return ReturnType(data_set_id, self._gateway_url, self._access_key)

    @overload
    def get_or_create_data_set(
        self, name: str, is_multisensor: Literal[False] = False
    ) -> NormalDataSet:
        ...

    @overload
    def get_or_create_data_set(
        self, name: str, is_multisensor: Literal[True]
    ) -> MultiSensorDataSet:
        ...

    @overload
    def get_or_create_data_set(self, name: str, is_multisensor: bool) -> DataSet:
        ...

    def get_or_create_data_set(self, name: str, is_multisensor: bool = False) -> DataSet:
        """Get a data set if 'name' exists. Create one otherwise.

        :param name: The name of a data set
        :return: class:`DataSet` object
        """
        try:
            return self.get_data_set(name, is_multisensor)
        except GASDataSetError:
            return self.create_data_set(name, is_multisensor)

    def list_data_sets(self) -> List[str]:
        """List names of all data sets.

        :return: A list of names of all data sets
        """
        data_sets_info = self._list_data_sets_info()
        data_set_names: List[str] = []
        for data_set_info in data_sets_info:
            data_set_name = data_set_info["contentSetResp"]["name"]
            data_set_names.append(data_set_name)
        return data_set_names

    def delete_data_set(self, name: str) -> None:
        """Delete a data set according to its name.

        :param name: The name of the data set to delete
        :raises GASDataSetError: When the required data set does not exist
        """
        data_sets_info = self._list_data_sets_info(name)
        if not data_sets_info:
            raise GASDataSetError(name)
        data_set_id = data_sets_info[0]["contentSetResp"]["contentSetId"]
        post_data = {"contentSetId": data_set_id, "name": name}
        self._data_set_post("deleteContentSets", post_data)

    def _list_data_sets_info(self, name: Optional[str] = None) -> List[Any]:
        """List info of all data sets.

        :param name: Data set name to list its info. If None, list info of all data sets
        :return: A list of dicts containing data set info. If name does not exist,
            return an empty list.
        """
        post_data = {"name": name}
        data = self._data_set_post("listContentSets", post_data)
        return data["contentSets"]  # type: ignore[no-any-return]

    def _data_set_post(self, method: str, post_data: Dict[str, Any]) -> Any:
        url = self._gateway_url + "content-store/" + method
        return post(url, json_data=post_data, access_key=self._access_key)
