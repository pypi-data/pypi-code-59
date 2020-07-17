import logging
import traceback

import requests

from bf_engine.entity.exception import BfEngineException, ErrorCode
from .base import CallerBase
from ..entity.answer import Answer
from ..logger import log as logging


class KnowledgeGraphCaller(CallerBase):
    """
    知识图谱
    """

    def __init__(self, app_id):
        super().__init__(app_id)
        # 导入数据
        self.app_id = app_id
        base_url = CallerBase.base_url
        self.data_load_url = '{}:18811/xeonKgDal/{}/importJson'.format(base_url, app_id)
        # 触发异步训练
        self.trigger_train_url = '{}:18811/xeonKgDal/{}/ftTrainTrigger?env=sandbox'.format(base_url, app_id)
        # 通知出话层更新数据
        self.sync_data_url = '{}:13508/api/v1/kbqa/syncData?appid={}'.format(base_url, app_id)
        # 线下数据同步到线上
        self.sync_sandbox_url = '{}:18811/xeonKgDal/{}/synchronizeSandbox'.format(base_url, app_id)
        # 预测出话接口
        self.predict_url = '{}:13508/api/v1/kbqa'.format(base_url)
        # 获取训练结果
        self.train_status_url = '{}:18811/xeonKgDal/syncHandler/{}/getSyncRecord'.format(base_url, app_id)

    def load_data(self, data: dict):
        """
        加载训练数据
        :param data: kg数据
        """
        try:
            response = requests.post(self.data_load_url, json=data)
            if self._response_failed(response):
                msg = "kg: 上传训练数据失败：原因: 上传数据接口异常。" + str(response.json()) if response is not None else ''
                raise BfEngineException(ErrorCode.kg_import_error, msg)
        except BfEngineException as bfe:
            raise bfe
        except Exception:
            msg = "kg: 上传数据失败， 原因: Exception When POST '{}' : {}".format(self.data_load_url, traceback.format_exc())
            raise BfEngineException(ErrorCode.kg_import_error, msg)

    def trigger_train(self):
        """
        触发训练 异步
        """
        try:
            response = requests.get(url=self.trigger_train_url)
            if self._response_failed(response):
                msg = "kg: 触发训练失败：原因: 接口异常。" + str(response.json()) if response is not None else ''
                raise BfEngineException(ErrorCode.kg_train_error, msg)
        except BfEngineException as bfe:
            raise bfe
        except Exception:
            msg = "kg: 触发训练失败， 原因: Exception When POST '{}' : {}".format(self.trigger_train_url, traceback.format_exc())
            raise BfEngineException(ErrorCode.kg_import_error, msg)

    def sync_data(self):
        """
        同步出话层数据
        """
        try:
            response = requests.get(url=self.sync_data_url)
            if self._response_failed(response):
                msg = "kg: 同步出话层数据：原因: 接口异常。" + str(response.json()) if response is not None else ''
                raise BfEngineException(ErrorCode.kg_train_error, msg)
        except BfEngineException as bfe:
            raise bfe
        except Exception:
            msg = "kg: 同步出话层数据， 原因: Exception When POST '{}' : {}".format(self.sync_data_url, traceback.format_exc())
            raise BfEngineException(ErrorCode.kg_train_error, msg)

    def sync_sandbox(self):
        """
        同步数据至线上
        """
        try:
            response = requests.post(url=self.sync_sandbox_url)
            if self._response_failed(response):
                msg = "kg: 同步数据失败：原因: 接口异常。" + str(response.json()) if response is not None else ''
                raise BfEngineException(ErrorCode.kg_train_error, msg)
        except BfEngineException as bfe:
            raise bfe
        except Exception:
            msg = "kg: 同步数据失败， 原因: Exception When POST '{}' : {}".format(self.trigger_train_url, traceback.format_exc())
            raise BfEngineException(ErrorCode.kg_train_error, msg)

    def status(self, wait_type):
        """
        等待中 并记录日志
        :param wait_type: train | sync
        :return: 是否成功
        """
        try:
            response = requests.get(url=self.train_status_url)
            if self._response_failed(response):
                msg = "kg: 获取状态失败：原因: 接口异常。" + str(response.json()) if response is not None else ''
                raise BfEngineException(ErrorCode.kg_train_error, msg)

            data = response.json().get('data')
            if data:
                train_status = data.get('trainingStatus')
                sync_status = data.get('syncStatus')
                if wait_type == 'train' and train_status == 2:
                    return True
                if wait_type == 'sync' and sync_status == 2:
                    return True
            return False
        except BfEngineException as bfe:
            raise bfe
        except Exception:
            msg = "kg: 获取状态失败， 原因: Exception When POST '{}' : {}".format(self.train_status_url, traceback.format_exc())
            raise BfEngineException(ErrorCode.kg_train_error, msg)

    def call(self, msg):
        """
        预测出话
        :param msg: 用户问
        :return: 机器人回答
        """
        answer = Answer('', 0)
        param = {
            "userid": "test",
            "sessionid": "test",
            "uniqueid": "test",
            "appid": self.app_id,
            "env": "production",
            "modeltype": "ft",
            "text": msg,
            "skg": "on"
        }
        try:
            response = requests.post(url=self.predict_url, json=param)
            if self._response_failed(response):
                logging.error("kg: 预测失败：原因: 接口异常。" + str(response.json()) if response is not None else '')
            else:
                response_json = response.json()
                if response_json.get('response'):
                    answer = Answer(response_json.get('response'), response_json.get('score'))
                else:
                    logging.warning('kg: 预测为空 [{}]'.format(msg))
        except Exception:
            msg = "Exception When POST '{}' : {}".format(self.trigger_train_url, traceback.format_exc())
            logging.error('kg: 对话失败， 原因: ' + msg)
        finally:
            return answer

    @staticmethod
    def _response_failed(response):
        return response is None or response.status_code != 200 or response.json() is None
