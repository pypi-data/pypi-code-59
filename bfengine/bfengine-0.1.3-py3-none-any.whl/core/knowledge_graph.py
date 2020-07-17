import time
import traceback
import copy
import json

from .module import Module
from ..caller.knowledge_caller import KnowledgeGraphCaller
from ..entity.exception import BfEngineException
from ..logger import log


data_template = {
    "data": {
        "entities": [],
        "properties": [],
        "entity_properties": [],
        "synonyms": {"entity": [], "property": [], "value": []},
        "introductions": {"property": [], "entity": {"synonyms": [], "corpus": [], "introduction": []}},
        "values": []
    }
}

entity_template = {
    "name": "",
    "sub_entities": [
    ],
    "relation": "has_a"
}
property_template = {
    "name": "",
    "corpus": [
    ],
    "type": "文本",
    "unit": "",
    "speech": ""
}
value_template = {
    "entity": "",
    "property": "",
    "value": ""
}


class DataGenerator:
    @staticmethod
    def generate_data(raw_data: dict):
        kg_data = copy.deepcopy(data_template)
        entities = []
        entity_name_set = set()
        property_name_set = set()
        properties = []
        values = []
        kg_data['data']['entities'] = entities
        kg_data['data']['properties'] = properties
        kg_data['data']['values'] = values
        if raw_data and raw_data['data']:
            datas = raw_data['data']
            for data in datas:
                entity_name = data.get('entity')
                property_name = data.get('property')
                value = data.get('value')
                if entity_name not in entity_name_set:
                    entity_dict = DataGenerator._get_entity(entity_name)
                    entities.append(entity_dict)
                    entity_name_set.add(entity_name)

                if property_name not in property_name_set:
                    property_dict = DataGenerator._get_property(property_name)
                    properties.append(property_dict)
                    property_name_set.add(property_name)
                value_dict = DataGenerator._get_value(entity_name, property_name, value)
                values.append(value_dict)
        return kg_data

    @staticmethod
    def _get_property(property_name):
        property_dict = copy.deepcopy(property_template)
        property_dict['name'] = property_name
        property_dict['corpus'].append("的" + property_name)
        return property_dict

    @staticmethod
    def _get_entity(entity_name):
        entity_dict = copy.deepcopy(entity_template)
        entity_dict['name'] = entity_name
        return entity_dict

    @staticmethod
    def _get_value(entity_name, property_name, value):
        value_dict = copy.deepcopy(value_template)
        value_dict['entity'] = entity_name
        value_dict['property'] = property_name
        value_dict['value'] = value
        return value_dict


class KnowledgeGraph(Module):
    """
    知识图谱
    """

    def __init__(self, app_id):
        super().__init__(app_id, 'kg')
        self.caller = KnowledgeGraphCaller(app_id)

    def train(self, data: dict) -> bool:
        """
        训练kg
        :param data: 训练数据
        :return: 训练是否成功
        """
        try:
            data = DataGenerator.generate_data(data)
            self._upload(data)
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

    def train_by_path(self, data_path: str) -> bool:
        """
        训练kg
        :param data_path: 训练数据文件路径
        :return: 训练是否成功
        """
        try:
            data = json.load(open(data_path))
            return self.train(data)
        except BfEngineException as bfe:
            log.error(bfe)
            return False
        except Exception as e:
            log.error("kg: 上传数据异常")
            log.error(e)
            traceback.print_exc()
            return False

    def _upload(self, data):
        log.info("kg: 开始上传训练数据")
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
