import json
import time
import traceback

from .module import Module
from ..caller.knowledge_caller import KnowledgeGraphCaller
from ..entity.exception import BfEngineException
from ..logger import log


class KnowledgeGraph(Module):
    """
    知识图谱
    """

    def __init__(self, app_id):
        super().__init__(app_id, 'kg')
        self.caller = KnowledgeGraphCaller(app_id)

    def train(self, data_path: str) -> bool:
        """
        训练kg
        :param data_path: 训练数据路径
        :return: 训练是否成功
        """
        try:
            self._upload(data_path)
            self._train()
            self._sync()
            return True
        except BfEngineException as bfe:
            log.error(bfe)
            return False
        except Exception as e:
            log.error("kg: 训练异常")
            log.error(e)
            traceback.print_exc()
            return False

    def _upload(self, data_path):
        log.info("kg: 开始上传训练数据")
        data = json.load(open(data_path))
        self.caller.load_data(data)
        log.info("kg: 训练数据上传成功")

    def _train(self):
        log.info("kg: 开始训练数据")
        self.caller.trigger_train()
        completed = False
        while not completed:
            completed = self.caller.status('train')
            log.info('kg: 数据训练中...')
            time.sleep(1)

    def _sync(self):
        log.info("kg: 开始同步数据")
        self.caller.sync_sandbox()
        log.info("kg: 同步成功")
        time.sleep(2)
        completed = False
        while not completed:
            completed = self.caller.status('sync')
            log.info('kg: 数据同步中..')
            time.sleep(1)
        log.info("kg: 同步出话层数据")
        self.caller.sync_data()
        log.info("kg: 同步成功")
        time.sleep(2)

    # 预测出话
    def query(self, msg):
        """
        :param msg: 用户问
        :return: 机器人回答
        """
        return self.caller.call(msg)
