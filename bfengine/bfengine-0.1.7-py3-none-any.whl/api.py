from .config import Config
from .core.bot import Bot


def init():
    """
    创建整个BF Engine系统环境，包含初始化数据库及核心模块
    """
    pass


def create_bot(app_id: str = None, is_local=False) -> Bot:
    """
    创建bot，并返回实例
    """
    if not app_id:
        app_id = Config.default_app_id

    if is_local:
        Config.base_url = 'http://127.0.0.1'
    else:
        Config.base_url = Config.remote_url

    return Bot(app_id)
