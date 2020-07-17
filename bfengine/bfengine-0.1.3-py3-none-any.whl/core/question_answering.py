import time
import traceback
import json
import os
from .module import Module
from ..caller.qa_caller import QACaller
from ..entity.answer import Answer
from ..entity.enums import QuestionType, QuestionMode
from ..entity.exception import BfEngineException
from ..logger import log


class QuestionAnswering(Module):
    """
    问答
    """
    tmp_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    faq_sq_empty_path = tmp_dir + "/data/问答上传模板.xlsx"
    faq_lq_empty_path = tmp_dir + "/data/语料上传模板.xlsx"

    def __init__(self, app_id):
        super().__init__(app_id, 'qa')
        self.caller = QACaller(app_id)

    def train(self, data: str = None, question_path: str = None, corpus_path: str = None):
        """
        :param data:
        :param question_path: 标准问路径
        :param corpus_path: 语料路径
        :return: 训练是否成功
        """
        try:
            if data:
                # 清空FAQ
                self._upload_question(self.faq_sq_empty_path, is_log=False)
                self._upload_corpus(self.faq_lq_empty_path, is_log=False)
                self._upload_json(data)
            else:
                log.info(self.app_id + ': 开始上传标准问和语料')
                self._upload_question(question_path)
                self._upload_corpus(corpus_path)
            self._train()
        except BfEngineException as bfe:
            log.error(bfe)
            return False
        except Exception as e:
            log.error('unknown exception')
            log.error(e)
            traceback.print_exc()
            return False
        return True

    def query(self, text: str) -> Answer:
        """
        :param text: 用户问
        :return: 机器人回答
        """
        return self.caller.call_module('faq', text)

    def _train(self):
        log.info(self.name + ': 开始训练')
        train_id = self.caller.train()
        progress = 0
        while progress < 100:
            progress = self.caller.train_status(train_id)
            time.sleep(1)
        time.sleep(5)

    def _upload_json(self, content):
        """
        获取从路径中json
        """
        try:
            data = content["data"]
            for item in data:
                data_id = self.caller.upload_json_sq(item)
                self.caller.upload_json_lq(data_id, item)
        except BfEngineException as bfe:
            log.error(bfe)
            return False
        except Exception:
            return None

    def _upload_corpus(self, corpus_path, is_log: bool = True):
        if is_log:
            log.info(self.app_id + ': 开始上传语料')
        data_id = self.caller.upload(QuestionType.LQ, QuestionMode.FULL, corpus_path)

        progress = 0
        while progress < 100:
            progress = self.caller.upload_status(data_id, is_log=is_log)
            time.sleep(1)

    def _upload_question(self, question_path, is_log=True):
        if is_log:
            log.info(self.app_id + ': 开始上传问题$答案')
        data_id = self.caller.upload(QuestionType.SQ_ANS, QuestionMode.FULL, question_path)

        progress = 0
        while progress < 100:
            progress = self.caller.upload_status(data_id, is_log=is_log)
            time.sleep(1)
