# coding=utf-8

import os, traceback
from datetime import datetime
from auto_runner.log import logger
from auto_runner.resultCollect import ResultCollect
from uiautomator import Adb as ADB
import requests
import json


def getConnectedPort(adb):
    '''auto assign port'''
    local_port = 9008
    try:  # first we will try to use the local port already adb forwarded
        for s, lp, rp in adb.forward_list():
            if s == adb.device_serial() and rp == 'tcp:%d' % 9008:
                local_port = int(lp[4:])
                return local_port
    except:
        pass
    return local_port



class ResultHandler(object):
    '''deal case test result by info'''
    
    @classmethod
    def handle(cls, info=None, path=None):
        # load test setting
        if info is None:
            return
        if info[0] == "addError":
            if 'self.tearDown()' == traceback.extract_tb(info[1][2][2], 1)[0][-1]:
                logger.warning(traceback.format_exc(3))
                return
        adb_list = [ADB(os.getenv('ANDROID_SERIAL'))]
        try:
            errImag = cls._sortTestCaseResult(info, adb_list)
            errImag = errImag[0] if errImag else ""
            ResultCollect.getInstance().addInfo(info, errImag)
        except:
            logger.error(traceback.format_exc(3))
            
    @classmethod       
    def _sortTestCaseResult(cls,info, adblist):
        """Sort test case result from "all" folder.
        Keyword arguments:
        info -- tuple of test case object description.(should not be none)
        """
        if info[0] == 'startTest' \
                or (not info[0] in ['addFailure', 'addError', 'addSuccess']):
            return
        imageName = None
        try:        
            src = info[1][1].store.getWorkDir()
        except Exception, e:
            logger.warning('case module error: setupclass or teardownclass error' + str(e))
        if info[0] == 'addFailure' or info[0] == 'addError':
            logger.info('Get error screenshot')
            imageName = cls._takeImage(src, adblist)  # wether all device takeshot,current 
            cls._take_xml(src, adblist)
        return imageName
    
    @classmethod
    def _takeImage(cls, target, adblist):
        '''take image to target dir'''
        errimgs =[]
        for adb in adblist:
            try:
                timestr = str(datetime.now()).replace(' ', '=').replace(':', '-')
                erroimg = 'error_img-%s-%s.png'%(adb.device_serial(), timestr)
                logger.info('takshot to %s'%erroimg)
                cls.screenshot(adb, os.path.join(target, erroimg))
                errimgs.append(erroimg)
            except:
                logger.warning(traceback.format_exc(3))
        return errimgs
    
    @classmethod
    def _take_xml(cls, target, adblist):
        cls._take_xml_uiautomator(target, adblist)
                
    @classmethod            
    def _take_xml_uiautomator(cls, target, adblist):
        for adb in adblist:
            timestr = str(datetime.now()).replace(' ', '=').replace(':', '-')
            erroimg = 'error_xml-%s-%s.xml'%(adb.device_serial(), timestr)
            logger.info('take xml to %s'%erroimg)
            try:
                port = getConnectedPort(adb)
                if port:
                    r=requests.post("http://127.0.0.1:%s"%port, data=json.dumps({"params": [True, None], "jsonrpc": "2.0", "method": "dumpWindowHierarchy", "id": "4ce7ef2b829bebf63b8a3001344e406c"}), headers={"Content-Type": "application/json"}, timeout=10)
                    data = json.loads(r.content)
                    with open(os.path.join(target, erroimg),'w+') as f:
                        f.write(data)
            except:
                cls._take_xml_cmd(adb, os.path.join(target, erroimg))
    
    
    @classmethod            
    def _take_xml_cmd(cls, adb, target_file):
        try:
            adb.shell('uiautomator dump')
            adb.cmd('pull', '/sdcard/window_dump.xml', target_file).wait()
        except:
            pass
        
        
    @classmethod    
    def screenshot(cls, adb, filename):
        '''take screenshot.'''
        try:
            png = "/data/local/tmp/screen_shot.png"
            adb.cmd("shell", "screencap", "-p", png).wait()
            adb.cmd("pull", png, filename).wait()
            adb.cmd("shell", "rm", png).wait()
        except:
            pass