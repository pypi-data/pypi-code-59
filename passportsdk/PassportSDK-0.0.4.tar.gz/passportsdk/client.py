from passportsdk.traits import AuthTrait
from passportsdk.traits import AdminTrait


class AppClient(object):
    """
    通行证微服务客户端
    """

    def __init__(self, _app):
        """
        初始化
        :param _app:
        """
        config = _app.config
        self.passport_service_url = config['PASSPORT_SERVICE_URL']
        self.app_url = config['DEFAULT_APP_URL']
        self.access_key_id = config['DEFAULT_APP_ACCESS_KEY_ID']
        self.access_key_secret = config['DEFAULT_APP_ACCESS_KEY_SECRET']
        self.access_token = ''

    def post(self, url, json_data):
        """
        发送POST请求
        :param url:
        :param json_data:
        :return:
        """
        from .common import app_post
        return app_post(client=self, url=url, json_data=json_data)

    def get_access_token(self):
        """
        获取access_token
        """
        return AuthTrait.get_access_token(self)

    def user_register(self, username, password):
        """
        用户注册
        """
        return AuthTrait.user_register(self, username, password)

    def user_login(self, username, password):
        """
        用户登录
        """
        return AuthTrait.user_login(self, username, password)

    def user_logout(self, user_token):
        """
        用户登出
        """
        return AuthTrait.user_logout(self, user_token)

    def user_info(self, user_token):
        """
        用户信息
        """
        return AuthTrait.user_info(self, user_token)

    def admin_user_list(self, user_token, request_data):
        """
        [后台]用户列表
        """
        return AdminTrait.admin_user_list(self, user_token, request_data)

    def admin_user_info(self, user_token, user_uuid):
        """
        [后台]用户信息
        """
        return AdminTrait.admin_user_info(self, user_token, user_uuid)

    def admin_user_modify(self, user_token, user_uuid, modify_user_info):
        """
        [后台]用户编辑(创建)
        """
        return AdminTrait.admin_user_modify(self, user_token, user_uuid, modify_user_info)

    def admin_user_delete(self, user_token, user_uuid):
        """
        [后台]用户编辑(创建)
        """
        return AdminTrait.admin_user_delete(self, user_token, user_uuid)

    def admin_permission_list(self, user_token):
        """
        [后台]权限列表
        """
        return AdminTrait.admin_permission_list(self, user_token)

    def admin_permission_info(self, user_token, permission_id):
        """
        [后台]权限信息
        """
        return AdminTrait.admin_permission_info(self, user_token, permission_id)

    def admin_permission_modify(self, user_token, permission_id, modify_permission_info):
        """
        [后台]权限编辑(创建)
        """
        return AdminTrait.admin_permission_modify(self, user_token, permission_id, modify_permission_info)

    def admin_role_list(self, user_token):
        """
        [后台]角色列表
        """
        return AdminTrait.admin_role_list(self, user_token)

    def admin_role_info(self, user_token, role_id):
        """
        [后台]角色信息
        """
        return AdminTrait.admin_role_info(self, user_token, role_id)

    def admin_role_modify(self, user_token, role_id, modify_role_info):
        """
        [后台]角色编辑(创建)
        """
        return AdminTrait.admin_role_modify(self, user_token, role_id, modify_role_info)

    def admin_group_list(self, user_token):
        """
        [后台]用户组列表
        """
        return AdminTrait.admin_group_list(self, user_token)

    def admin_group_info(self, user_token, group_id):
        """
        [后台]用户组信息
        """
        return AdminTrait.admin_group_info(self, user_token, group_id)

    def admin_group_modify(self, user_token, group_id, modify_group_info):
        """
        [后台]用户组编辑(创建)
        """
        return AdminTrait.admin_group_modify(self, user_token, group_id, modify_group_info)

    def admin_app_list(self, user_token):
        """
        [后台]应用列表
        """
        return AdminTrait.admin_app_list(self, user_token)

    def admin_app_info(self, user_token, app_id):
        """
        [后台]应用信息
        """
        return AdminTrait.admin_app_info(self, user_token, app_id)

    def admin_app_modify(self, user_token, app_id, modify_app_info):
        """
        [后台]应用编辑(创建)
        """
        return AdminTrait.admin_app_modify(self, user_token, app_id, modify_app_info)
