import requests

from .base import CallerBase
from ..config import Config
from ..entity.enums import QuestionType, QuestionMode
from ..entity.exception import BfEngineException
from ..logger import log


class QACaller(CallerBase):
    """
    QA api调用
    """
    dac_url = '{}:{}'.format(Config.base_url, Config.ssm_port)
    upload_faq_upload_url = dac_url + "/ssm/dac/upload"
    upload_faq_upload_status_url = dac_url + "/ssm/dac/upload/"
    upload_faq_train_url = dac_url + "/ssm/dac/train"
    upload_faq_train_status_url = dac_url + "/ssm/dac/trainhistory"
    upload_faq_json_sq_url = dac_url + "/ssm/dac/sq"
    upload_faq_json_lq_url = dac_url + "/ssm/dac/lq"

    def __init__(self, app_id):
        super().__init__(app_id)
        self.app_id = app_id
        self.module = 'qa'
        self.header = {
            "X-locale": "zh-cn",
            "app_id": app_id,
            "user_id": "bf-engine-sdk",
            "Authorization": "Bearer EMOTIBOTDEBUGGER",
            "Accept": "application/json,text/plain, */*"
        }

    def upload(self, data_type: QuestionType, data_model: QuestionMode, file_path: str) -> str:
        """
        上传标注问/语料
        :param data_type: 上传类型 (SQ_ANS|LQ|TQ)
        :param data_model: 上传模型 (全量|增量)
        :param file_path: 上传文件路径
        :return 上传id
        """
        # 上传问题$答案
        files = {"file": (self.app_id + ".xlsx", open(file_path, 'rb'))}
        data = {"type": data_type, "mode": data_model, "comment": "全量"}
        resp = requests.request("POST", self.upload_faq_upload_url, headers=self.header, data=data, files=files).json()

        # 问题$答案上传进度
        code = int(resp["code"])
        msg = str(resp["message"])
        if code != 0:
            raise BfEngineException(code=code, msg=msg)
        return str(resp["data"])

    def upload_json_sq(self, data: dict) -> str:
        """
        上传标准问
        :param data: 上传数据
        :return id
        """
        data = {
            "sq": data["sq"],
            "category_id": -1,
            "tag_id_list": [],
            "answers": [
                {
                    "answer": data["answer"],
                    "property": {
                        "dimension_id_list": []
                    },
                    "start_time": "",
                    "end_time": "",
                    "period_type": 0,
                    "related_sq_id_list": []
                }
            ]
        }
        resp = requests.post(self.upload_faq_json_sq_url, headers=self.header, json=data).json()
        code = int(resp["code"])
        msg = str(resp["message"])
        if code != 0:
            raise BfEngineException(code=code, msg=msg)
        return resp["data"]["id"]

    def upload_json_lq(self, data_id: str, data: dict) -> str:
        """
        上传标准问
        :param data_id: 上传id
        :return 上传进度
        """
        data = {
            "records": [
                {
                    "sq_id": data_id,
                    "lq_list": list(map(lambda lq: {'lq': lq}, data["lq"]))
                }
            ]
        }
        resp = requests.post(self.upload_faq_json_lq_url, headers=self.header, json=data).json()
        code = int(resp["code"])
        msg = str(resp["message"])
        if code != 0:
            raise BfEngineException(code=code, msg=msg)
        return resp["data"]["id"]

    def upload_status(self, data_id: str, is_log: bool = True) -> int:
        """
        查询上传状态
        :param is_log: 是否打日志
        :param data_id: 上传id
        :return 上传进度
        """
        resp = requests.get(self.upload_faq_upload_status_url + "/" + data_id, headers=self.header, json={}).json()
        code = int(resp["code"])
        msg = str(resp["message"])
        if code != 0:
            raise BfEngineException(code=code, msg=msg)
        progress = resp["data"]["progress"]
        if is_log:
            log.info(self.module + ": 上传进度==" + str(progress) + "%")
        return progress

    def train(self):
        """
        训练标准问题
        :return 训练id
        """
        resp = requests.get(self.upload_faq_train_url, headers=self.header, json={}).json()
        code = int(resp["code"])
        msg = str(resp["message"])
        if code != 0:
            raise BfEngineException(code=code, msg=msg)
        return str(resp["data"])

    def train_status(self, train_id):
        """
        查询训练状态
        :param train_id: 训练id
        :return 训练进度
        """
        resp = requests.get(self.upload_faq_train_status_url + "/" + train_id, headers=self.header, json={}).json()
        code = int(resp["code"])
        msg = str(resp["message"])
        if code != 0:
            raise BfEngineException(code=code, msg=msg)
        progress = resp["data"]["progress"]
        log.info(self.module + ": 训练进度==" + str(progress) + "%")
        return progress
