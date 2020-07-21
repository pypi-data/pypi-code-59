#! /usr/bin/env python
__author__ = 'Tser'
__email__ = '807447312@qq.com'
__project__ = 'jicaiauto'
__script__ = 'config.py'
__create_time__ = '2020/7/6 14:11'
'''  UI自动化可以使用该文件，其他测试可以移除防止对测试有干扰   '''
from selenium import webdriver
from jicaiauto.data.GLO_VARS import PUBLIC_VARS
import pytest

b = None

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot():
    '''
    截图保存为base64，展示到html中
    :return:
    '''
    if b:
        return b.get_screenshot_as_base64()
    else:
        return '未截图'

@pytest.fixture(scope='session', autouse=True)
def mobile():
    global b
    '''
        'platformName': 'Android',
        'platformVersion': '5.1',  
        'deviceName': '',  
        'noReset': True,  
        'allowClearUserData' = 'true',      #用户可自行选择清除数据
        'fullReset' = "false",              #卸载程序，默认为false
        'exported'="true",                  #是否支持其他应用调用当前组件
        'appPackage': '',  
        'appActivity': '',  
        'unicodeKeyboard': True,            #使用unicode编码方式发送字符串  
        'resetKeyboard': True               #将键盘隐藏起来，输入中文就要增加这两个参数
        'udid':'设备UDID'
        'bundleId':'应用包名'
    '''
    PUBLIC_VARS['android_caps'] = {
        'platformName': 'Android',
        'platformVersion': '5.1',
        'deviceName': '设备名',
        'noReset': True,
        'allowClearUserData': 'true',
        'fullReset': "false",
        'exported': "true",
        'appPackage': '应用包名',
        'appActivity': '应用Activity名',
        'unicodeKeyboard': True,
        'resetKeyboard': True
    }
    PUBLIC_VARS['ios_caps'] = {
        'platformName': 'iOS',
        'platformVersion': '11.4',
        'deviceName': '设备名',
        'udid': '设备UDID',
        'bundleId': '应用包名',
        'noReset': True,
    }
    if b is None:
        b = webdriver.Remote('http://127.0.0.1:4723/wd/hub', PUBLIC_VARS['android_caps'])
    return b