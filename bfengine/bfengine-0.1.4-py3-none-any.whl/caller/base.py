import json

import requests

from ..entity.answer import Answer
from ..config import Config


class CallerBase:
    """
    api调用
    """
    base_url = Config.base_url
    robot_url = '{}:{}/{}'.format(Config.base_url, Config.robot_port, Config.robot_url)

    def __init__(self, app_id):
        self.app_id = app_id

    def call_module(self, module: str, text: str) -> Answer:
        """
        robot接口访问
        :param module: 模块名称
        :param text: 用户问
        :return: 机器人回答
        """
        header = {
            "Content-Type": "application/json"
        }
        data = {
            "user_id": 'bf-engine',
            "method": "inquiry",
            "app_id": self.app_id,
            "question": text,
            "included_modules": [module],
            "request_data": {
                "online": False
            }
        }
        resp = requests.post(self.robot_url, headers=header, json=data)
        params = json.loads(resp.text)
        answers = params['results']
        if answers:
            answer = answers[0]
            return Answer(answer['answer'][0]['value'], answer['answer_score'])
        return Answer('我还在学习', 60)

    @staticmethod
    def _response_failed(response):
        return response is None or response.status_code != 200 or response.json() is None
