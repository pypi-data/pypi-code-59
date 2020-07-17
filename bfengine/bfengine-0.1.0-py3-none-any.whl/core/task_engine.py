import json

import requests
from requests import Session, Request
import logging
from .module import Module
from ..config import Config
import traceback
# from .module import Module
# coding=UTF-8

API_PORT = "80"
TE_PORT = "14101"
USERID = "csbot"


class TaskEngine(Module):
    """
    任务引擎
    """

    def __init__(self, app_id):
        super().__init__(app_id, 'te')
        self.app_id = app_id
        self.sess = Session()
        self.api_server = Config.base_url
        # 获取scenario列表
        self.query_scenarios_url = '{}:{}/php/api/ApiKey/task_engine_app.php'.format(
                self.api_server, API_PORT)
        # 获取scenario详细信息
        self.query_scenario_info_url = '{}:{}/php/api/ApiKey/task_engine_scenario.php'.format(
                self.api_server, API_PORT)
                # 获取scenario详细信息
        self.query_url = '{}:{}/task_engine/ET'.format(self.api_server, TE_PORT)

    """
    查询scenario列表
    """
    def query_scenarios(self):
        try:
            logging.info("te: 查询scenario列表开始。")
            params = {}
            headers = {}
            params["appid"] = self.app_id
            params["type"] = 0
            headers['X-Appid'] = self.app_id
            req = Request('GET', self.query_scenarios_url, headers=headers, params=params)
            resp = self.sess.send(req.prepare(), verify=False, timeout=2)
            rtjs = json.loads(resp.text)
            logging.info("te: 查询scenario列表完毕")
            return rtjs['msg']
        except Exception :
            msg = "Exception When POST '{}' : {}".format(self.query_scenarios_url, traceback.format_exc())
            logging.error('te: 查询scenario列表失败， 原因: ' + msg)
        return []
    """
    查询scenario详细信息
    """
    def query_scenario_info(self,scenario_id, user_id=USERID):
        try:
            logging.info("te: 查询scenario【"+scenario_id+"】信息开始。")
            params = {}
            headers = {}
            params["scenarioid"] = scenario_id
            headers['X-Appid'] = self.app_id
            headers['X-Userid'] = USERID
            req = Request('GET', self.query_scenario_info_url, headers=headers, params=params)
            resp = self.sess.send(req.prepare(), verify=False, timeout=2)
            rtjs = json.loads(resp.text)
            logging.info("te: 查询scenario【"+scenario_id+"】信息完毕。")
            return rtjs
        except Exception :
            msg = "Exception When POST '{}' : {}".format(self.query_scenario_info_url, traceback.format_exc())
            logging.error('te: 查询scenario【'+scenario_id+'】信息， 原因: ' + msg)
        return []
    """
    导入scenario
    """
    def add_scenarios(self,scenario_json):
        try:
            logging.info("te: 导入scenario开始。")
            headers = {}
            metadata = None
            scenario_id,scenario_name = self.get_scenario_info(scenario_json)
            scenario_lists = self.query_scenarios()
            for  scenario in scenario_lists:
                if 'scenarioID' in scenario and scenario['scenarioID'] == scenario_id:
                    logging.info("te: 导入scenario【"+scenario_id+"】存在重复scenario，进行新增导入。")
                    metadata = self.create_scenario(scenario_name)
                    if metadata == None:
                        logging.info("te: 导入scenario【"+scenario_id+"】存在重复scenario，新增失败")
                        return None,None
                    break
            content = scenario_json['taskScenario']
            params = {}
            if metadata != None:
                content['metadata'] = metadata
                scenario_id = metadata['scenario_id']
                scenario_name = metadata['scenario_name']
                logging.info("te: 导入scenario【"+scenario_id+"】存在重复scenario，新增scenarioid为【"+scenario_id+"】")
            else:
                params['upload'] = 1
                params['type'] = 0
            layout = scenario_json['taskLayouts']
            params['content'] = json.dumps(content)
            params['scenarioid'] = scenario_id
            params["appid"] = self.app_id
            params['layout'] = json.dumps(layout)
            params['method'] = 'PUT'
            headers['X-Appid'] = self.app_id
            headers['X-Userid'] = USERID
            resp = requests.post(url=self.query_scenario_info_url,data=params,headers=headers)
            if resp is None or resp.status_code != 200 :
                return None,None
            logging.info("te: 导入scenario【"+scenario_id+"】完毕。")
            return scenario_id,scenario_name
        except Exception :
            msg = "Exception When POST '{}' : {}".format(self.query_scenario_info_url, traceback.format_exc())
            logging.error('te: 导入scenario失败， 原因: ' + msg)

        return None,None
    """
    获取scenario配置信息
    """
    def get_scenario_info(self,scenario_json):
        try:
            return scenario_json["taskScenario"]["metadata"]["scenario_id"],scenario_json["taskScenario"]["metadata"]["scenario_name"]
        except Exception :
            pass
        return None,None
    """
    启动scenario
    """
    def enable_scenario(self,scenario_id):
        try:
            logging.info("te: 启用scenario【"+scenario_id+"】开始。")
            headers = {}
            params = {}
            params['scenarioid'] = scenario_id
            params["appid"] = self.app_id
            params['enable'] = 'true'
            headers['X-Appid'] = self.app_id
            headers['X-Userid'] = USERID
            req = Request('POST', self.query_scenarios_url, headers=headers, params=params)
            resp = self.sess.send(req.prepare(), verify=False, timeout=2)
            if resp is None or resp.status_code != 200 :
                logging.info("te: 启用scenario【"+scenario_id+"】失败。")
                return False
            logging.info("te: 启用scenario【"+scenario_id+"】完毕。")

            return True
        except Exception :
            msg = "Exception When POST '{}' : {}".format(self.query_scenarios_url, traceback.format_exc())
            logging.error('te: 启用scenario【'+scenario_id+'】失败， 原因: ' + msg)
        return False
    """
    停用scenario
    """
    def disable_scenario(self,scenario_id):
        try:
            logging.info("te: 停用scenario【"+scenario_id+"】开始。")

            headers = {}
            params = {}
            params['scenarioid'] = scenario_id
            params["appid"] = self.app_id
            params['enable'] = 'false'
            headers['X-Appid'] = self.app_id
            headers['X-Userid'] = USERID
            req = Request('POST', self.query_scenarios_url, headers=headers, params=params)
            resp = self.sess.send(req.prepare(), verify=False, timeout=2)
            if resp is None or resp.status_code != 200 :
                logging.info("te: 停用scenario【"+scenario_id+"】失败。")
                return False
            logging.info("te: 停用scenario【"+scenario_id+"】完毕。")
            return True
        except Exception :
            msg = "Exception When POST '{}' : {}".format(self.query_scenarios_url, traceback.format_exc())
            logging.error('te: 停用scenario【'+scenario_id+'】失败， 原因: ' + msg)
        return False
    """
    发布scenario
    """
    def public_scenario(self,scenario_id):
        try:
            logging.info("te: 发布scenario【"+scenario_id+"】开始。")
            headers = {}
            params = {}
            params['scenarioid'] = scenario_id
            params["appid"] = self.app_id
            params['publish'] = 1
            headers['X-Appid'] = self.app_id
            headers['X-Userid'] = USERID
            req = Request('PUT', self.query_scenario_info_url, headers=headers, params=params)
            resp = self.sess.send(req.prepare(), verify=False, timeout=2)
            if resp is None or resp.status_code != 200 :
                logging.info("te: 发布scenario【"+scenario_id+"】失败。")
                return False
            logging.info("te: 发布scenario【"+scenario_id+"】完毕。")

            return True
        except Exception :
            msg = "Exception When POST '{}' : {}".format(self.query_scenario_info_url, traceback.format_exc())
            logging.error('te: 发布scenario【'+scenario_id+'】失败， 原因: ' + msg)
        return False
    """
    新建scenario
    """
    def create_scenario(self,scenario_name,):
        try:
            logging.info("te: 新建scenario【"+scenario_name+"】开始。")
            params = {}
            headers = {}
            params["scenarioName"] = scenario_name
            params["template"] = ''
            params["appid"] = self.app_id
            params["type"] = 0

            headers['X-Appid'] = self.app_id
            headers['X-Userid'] = USERID
            req = Request('POST', self.query_scenario_info_url, headers=headers, params=params)
            resp = self.sess.send(req.prepare(), verify=False, timeout=2)
            rtjs = json.loads(resp.text)
            logging.info("te: 新建scenario【"+scenario_name+"】完毕。")

            return rtjs['template']['metadata']
        except Exception :
            msg = "Exception When POST '{}' : {}".format(self.query_scenario_info_url, traceback.format_exc())
            logging.error('te: 新建scenario【'+scenario_name+'】失败， 原因: ' + msg)
        return None
    """
    删除scenario
    """
    def del_scenarios(self,scenario_id, user_id=USERID):
        try:
            logging.info("te: 删除scenario【"+scenario_id+"】开始。")

            params = {}
            headers = {}
            params["scenarioid"] = scenario_id
            params["delete"] = 1
            headers['X-Appid'] = self.app_id
            headers['X-Userid'] = USERID
            req = Request('PUT', self.query_scenario_info_url, headers=headers, params=params)
            resp = self.sess.send(req.prepare(), verify=False, timeout=2)
            if resp is None or resp.status_code != 200 :
                logging.info("te: 删除scenario【"+scenario_id+"】失败。")
                return False
            logging.info("te: 删除scenario【"+scenario_id+"】完毕。")
            return True
        except Exception :
            msg = "Exception When POST '{}' : {}".format(self.query_scenario_info_url, traceback.format_exc())
            logging.error('te: 删除scenario【'+scenario_id+'】失败， 原因: ' + msg)

        return False
    """
    获取从路径中json
    """
    def get_scenariojson_from_path(self,path):
        try:
            with open(path,encoding='utf-8-sig', errors='ignore') as f:
                data = json.load(f, strict=False)
                return data[0]
        except Exception :
            return None
    """
    获取对话信息
    """
    def query(self,txt, user_id=USERID, session_id=''):
        try:
            logging.info("te: 对话开始，传入语句："+txt)
            taskengion_json = get_taskengine_json(
                txt, self.app_id, user_id, session_id)
            headers = {'Content-Type': 'application/json;charset=UTF-8'}
            resp = requests.post(self.query_url, json=taskengion_json, headers=headers)
            rtjs = json.loads(resp.text)
            logging.info("te: 对话结束，返回："+rtjs["TTSText"])
            return rtjs["TTSText"]
        except Exception :
            msg = "Exception When POST '{}' : {}".format(self.query_url, traceback.format_exc())
            logging.error('te: 对话失败， 原因: ' + msg)
        return ""
    """
    生成scenario对话json
    """
def get_taskengine_json(txt,app_id, user_id, session_id):
    tejson = {}
    textconversion = {}
    textconversion['text_simplified'] = txt
    textconversion['text_traditional'] = txt
    tejson["TextConversion"] = textconversion
    tejson["Text"] = txt
    tejson["UserID"] = user_id
    tejson["ExtendData"] = {}
    tejson["SessionID"] = session_id
    tejson["UniqueID"] = user_id+session_id
    tejson["AppID"] = app_id
    config = {}
    config["webapi_timeout"] = 1000
    tejson["Config"] = config
    return tejson
if __name__ == '__main__':
    
    ss = TaskEngine("8ec2eb5a7d0c4ae589f04d71f392b784")
    scenariojson = ss.get_scenariojson_from_path("/Users/test/Desktop/666.json")
    print('查询te scenario数目开始')
    lists = ss.query_scenarios()
    print('查询te scenario数目完毕，共有'+str(len(lists))+"个")
    
    print('导入te scenario')
    scenario_id,scenario_name = ss.add_scenarios(scenariojson)
    if scenario_id == None:
        print('导入失败')
    else:
        print('导入成功,开始发布')
    print('导入后，查询te scenario数目开始')
    lists = ss.query_scenarios()
    print('查询te scenario数目完毕，共有'+str(len(lists))+"个")


    sa = ss.enable_scenario(scenario_id)
    sa = ss.public_scenario(scenario_id)
    print('发布完毕，测试对话。输入内容：测试新导入的对话')
    sa = ss.query('测试新导入的对话')
    print ('te输出：'+sa)
    print('删除刚才导入的task。')

    sa= ss.del_scenarios(scenario_id)

    print('删除后，查询te scenario数目开始')
    lists = ss.query_scenarios()
    print('查询te scenario数目完毕，共有'+str(len(lists))+"个")

