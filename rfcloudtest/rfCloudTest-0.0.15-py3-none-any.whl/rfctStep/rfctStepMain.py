'''
不支持for或者template
{
    "name": "测试步骤1",
    "type": "rft",
    "keyword":"关键字,string类型",
    "params":<string或者int等基础类型数组,非必填字段>
}
'''
from builtins import isinstance, dict, str, list

from rfCloudTest.utils import statusObj

_STEP_TYPE='rft'
_STEP_NAME='name'
_STEP_KEYWORD='keyword'
_STEP_PARAMS='params'
_BLOCK=" " * 4
_SEPERATE=" " * 2

def parse(file_path,suite_name,case_name,step_detail_json):
    content=''
    if not isinstance(step_detail_json, dict):
        return statusObj.get_step_content(file_path, statusObj.STATUS_NOK, suite_name, case_name, None, _STEP_TYPE, '测试步骤不是字典')
    if _STEP_NAME not in step_detail_json:
        return statusObj.get_step_content(file_path, statusObj.STATUS_NOK, suite_name, case_name, None,_STEP_TYPE, '测试步骤不存在' + _STEP_NAME)
    if not isinstance(step_detail_json[_STEP_NAME], str):
        return statusObj.get_step_content(file_path, statusObj.STATUS_NOK, suite_name, case_name, None,_STEP_TYPE, '测试步骤' + _STEP_NAME + '不是string类型')
    step_name = step_detail_json[_STEP_NAME]
    content+= _BLOCK + '${' + step_name + '}='
    if _STEP_KEYWORD not in step_detail_json:
        return statusObj.get_step_content(file_path, statusObj.STATUS_NOK, suite_name, case_name, step_name, _STEP_TYPE, '测试步骤[' + step_name + ']['+ _STEP_KEYWORD+"]不存在")
    if not isinstance(step_detail_json[_STEP_KEYWORD], str):
        return statusObj.get_step_content(file_path, statusObj.STATUS_NOK, suite_name, case_name, step_name, _STEP_TYPE, '测试步骤[' + step_name + ']['+ _STEP_KEYWORD+"]不是string类型")
    content+= _BLOCK + step_detail_json[_STEP_KEYWORD]
    if _STEP_PARAMS in step_detail_json:
        params = step_detail_json[_STEP_PARAMS]
        if not isinstance(params,list):
            return statusObj.get_step_content(file_path, statusObj.STATUS_NOK, suite_name, case_name, step_name, _STEP_TYPE,'测试步骤[' + step_name + '][' + _STEP_PARAMS + "]不是list类型")
        for param_item in params:
            if isinstance(param_item,list) or isinstance(param_item,dict):
                return statusObj.get_step_content(file_path, statusObj.STATUS_NOK, suite_name, case_name, step_name, _STEP_TYPE, '测试步骤[' + step_name + '][' + _STEP_PARAMS + "]中["+str(param_item)+"]是list或者dict类型")
            content+=_BLOCK + str(param_item)

    return statusObj.get_step_content(file_path, statusObj.STATUS_OK, suite_name, case_name, step_name,_STEP_TYPE, 'OK',content=content)

def get_settings_content():
    '''
    获取robot文件依赖。
    :return: content
    '''
    content = 'Library  Collections\n'
    content+= 'Library  DateTime\n'
    content+= 'Library  String\n'
    return content