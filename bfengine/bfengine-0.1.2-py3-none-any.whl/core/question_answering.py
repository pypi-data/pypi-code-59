import time
import traceback

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

    def __init__(self, app_id):
        super().__init__(app_id, 'qa')
        self.caller = QACaller(app_id)

    def train(self, question_path, corpus_path):
        """
        :param question_path: 标准问路径
        :param corpus_path: 语料路径
        :return: 训练是否成功
        """
        try:
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
        time.sleep(2)

    def _upload_corpus(self, corpus_path):
        log.info(self.app_id + ': 开始上传语料')
        data_id = self.caller.upload(QuestionType.LQ, QuestionMode.FULL, corpus_path)

        progress = 0
        while progress < 100:
            progress = self.caller.upload_status(data_id)
            time.sleep(1)

    def _upload_question(self, question_path):
        log.info(self.app_id + ': 开始上传问题$答案')
        data_id = self.caller.upload(QuestionType.SQ_ANS, QuestionMode.FULL, question_path)

        progress = 0
        while progress < 100:
            progress = self.caller.upload_status(data_id)
            time.sleep(1)
