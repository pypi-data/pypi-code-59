from mysqlmapper.manager.session.sql_session_factory import MySQLSessionFactory

from yuma.model import Permission, PermissionGroup
from yuma.permission import PermissionHolder


def get_permission_holder(factory: MySQLSessionFactory) -> PermissionHolder:
    """
    Get permission holder from mysql
    :param factory: MySQLSessionFactory
    :return: PermissionHolder
    """
    holder = PermissionHolder()
    _get_permissions(holder, factory)
    _get_group(holder, factory)
    return holder.build_tree()


def _get_permissions(holder: PermissionHolder, factory: MySQLSessionFactory):
    """
    Get permissions from mysql
    :param holder: PermissionHolder
    :param factory: MySQLSessionFactory
    """
    # get service
    yuma_permission_service = factory.get_simple_service("yuma_permission")
    # get data
    data = yuma_permission_service.get_list({"Start": -1})
    for item in data:
        holder.add_permission(Permission(item["id"], item["permission_key"], item["memo"], item["father_id"]))


def _get_group(holder: PermissionHolder, factory: MySQLSessionFactory):
    """
    Get group from mysql
    :param holder: PermissionHolder
    :param factory: MySQLSessionFactory
    """
    # get service
    yuma_group_service = factory.get_simple_service("yuma_group")
    yuma_group_permission_service = factory.get_simple_service("yuma_group_permission")
    # get data
    group_list = yuma_group_service.get_list({"Start": -1})
    # build data
    for group in group_list:
        key = group["group_key"]
        permission_group = PermissionGroup(key)
        permission_list = yuma_group_permission_service.get_list({"group_key": key, "Start": -1})
        for permission in permission_list:
            permission_group.add_id(permission["permission_id"])
        holder.add_permission_group(permission_group)
