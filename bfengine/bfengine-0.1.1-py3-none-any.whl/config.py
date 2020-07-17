import os


class Config:
    default_app_id = os.environ.get('BF_ENGINE_DEFAULT_APP_ID', 'emotibotisthebestrobotoftheworld')
    base_url = os.environ.get('BF_ENGINE_BASE_URL', 'http://11.0.0.148')
    default_user_id = os.environ.get('BF_ENGINE_DEFAULT_USER_ID', 'bf-engine-user')
    robot_url = os.environ.get('BF_ENGINE_ROBOT_URL', 'openapi/v1/robot')
    robot_port = os.environ.get('BF_ENGINE_ROBOT_PORT', 8080)
    ssm_port = os.environ.get('BF_ENGINE_SSM_PORT', 8686)
