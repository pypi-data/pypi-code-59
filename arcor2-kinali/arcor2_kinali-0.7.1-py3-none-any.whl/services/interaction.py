import os
from typing import FrozenSet, List

from arcor2 import rest
from arcor2.action import action
from arcor2.data.common import ActionMetadata
from arcor2.services.service import Service

from arcor2_kinali.data.interaction import DialogValue, NotificationLevelEnum, NotificationValue

URL = os.getenv("INTERACTION_SERVICE_URL", "http://127.0.0.1:17000")


class InteractionService(Service):
    """
    REST interface to the barcode service.
    """

    def __init__(self, configuration_id: str):

        super(InteractionService, self).__init__(configuration_id)

    @staticmethod
    def get_configuration_ids() -> FrozenSet[str]:
        return frozenset({"default"})

    @action
    def add_dialog(self, title: str, content: str, options: List[str]) -> None:
        """
        Logs value with the specified group and name.
        :param title:
        :param content:
        :param options:
        :return:
        """

        rest.put(f"{URL}/dialog", params={"title": title, "content": content}, data=options)

    @action
    def get_dialog(self) -> DialogValue:
        """
        Gets names of all tracked values stored in given group.
        :return:
        """

        return rest.get(f"{URL}/dialog", DialogValue)

    @action
    def add_dialog_resolve(self, option: str) -> None:
        """
        Logs value with the specified group and name.
        :param option:
        :return:
        """

        rest.put(f"{URL}/dialog/resolve", params={"option": option})

    @action
    def add_notification(self, message: str, level: NotificationLevelEnum) -> None:
        """
        Logs value with the specified group and name.
        :param message:
        :param level:
        :return:
        """

        rest.put(f"{URL}/notification", params={"message": message, "level": level})

    @action
    def delete_notifications(self) -> None:
        """
        Deletes all tracked values stored in given group.
        :return:
        """

        rest.delete(f"{URL}/notifications")

    @action
    def get_notifications(self, since_imestamp: int) -> List[NotificationValue]:
        """
        Gets names of all tracked values stored in given group.
        :param since_imestamp:
        :return:
        """
        return rest.get_list(f"{URL}/notifications", NotificationValue, params={"since_imestamp": since_imestamp})

    add_dialog.__action__ = ActionMetadata(free=True, blocking=True)
    get_dialog.__action__ = ActionMetadata(free=True, blocking=True)
    add_dialog_resolve.__action__ = ActionMetadata(free=True, blocking=True)
    add_notification.__action__ = ActionMetadata(free=True, blocking=True)
    delete_notifications.__action__ = ActionMetadata(free=True, blocking=True)
    get_notifications.__action__ = ActionMetadata(free=True, blocking=True)
