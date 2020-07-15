import os
from typing import FrozenSet, List

from arcor2 import rest
from arcor2.action import action
from arcor2.data.common import ActionMetadata
from arcor2.services.service import Service


from arcor2_kinali.data.statistic import StatisticValue


URL = os.getenv("STATISTIC_SERVICE_URL", "http://127.0.0.1:16000")


class StatisticService(Service):
    """
    Statistic Web API Reference.
    """

    def __init__(self, configuration_id: str):

        super(StatisticService, self).__init__(configuration_id)

    @staticmethod
    def get_configuration_ids() -> FrozenSet[str]:
        return frozenset({"default"})

    @action
    def get_names(self, group_id: str) -> List[str]:
        """
        Gets names of all tracked values stored in given group.
        :param group_id:
        :return:
        """
        return rest.get_list_primitive(f"{URL}/values/{group_id}", str)

    @action
    def add_value(self, group_id: str, name: str, value: float) -> None:
        """
        Logs value with the specified group and name.
        :param group_id:
        :param name:
        :param value:
        :return:
        """

        rest.put(f"{URL}/values", params={"group_id": group_id, "name": name, "value": value})

    @action
    def get_groups(self) -> List[str]:
        """
        Gets Ids of all stored groups.
        :param name:
        :return:
        """

        return rest.get_list_primitive(f"{URL}/values", str)

    @action
    def get_values(self, group_id: str, name: str, since_timestamp: int = 0) -> List[StatisticValue]:
        """
        Gets tracked values with the specified name. Values are sorted as were added to service.
        :param group_id: Logged value name.
        :param name: Logged value name.
        :param since_timestamp: The date and time, as a UNIX timestamp in nanoseconds, after which created values
                                are returned.
        :return:
        """

        return rest.get_list(f"{URL}/values/{group_id}/{name}", StatisticValue,
                             params={"since_timestamp": since_timestamp})

    @action
    def delete_group(self, group_id: str) -> None:
        """
        Deletes all tracked values stored in given group.
        :param group_id:
        :return:
        """

        rest.delete(f"{URL}/values/{group_id}")

    get_names.__action__ = ActionMetadata(free=True, blocking=True)
    add_value.__action__ = ActionMetadata(free=True, blocking=True)
    get_groups.__action__ = ActionMetadata(free=True, blocking=True)
    get_values.__action__ = ActionMetadata(free=True, blocking=True)
    delete_group.__action__ = ActionMetadata(free=True, blocking=True)
