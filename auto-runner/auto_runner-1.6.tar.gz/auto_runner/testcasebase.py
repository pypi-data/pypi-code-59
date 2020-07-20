# coding=utf-8

import unittest,time
from auto_runner.assertion import Assertion
from auto_runner.log import logger
from auto_runner.store import Store
from auto_runner.ftpDownload import FtpDownLoad


class TestCaseBase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(TestCaseBase, cls).setUpClass()  
        cls.logger = logger
        cls.store = Store.getInstance()
    
    def setUp(self):
        super(TestCaseBase, self).setUp()
        self.assertion = Assertion()
        self.starttime = time.strftime('%Y.%m.%d-%H.%M.%S', time.localtime(time.time()))
        self.store.createOutDirs(self)
    
    def tearDown(self):
        super(TestCaseBase, self).tearDown()
        self.logger.info("tearDown".center(40,"*"))
    
    @staticmethod  
    def downLoadPreResourceFile(remoteFile, localFile, host=None):
        '''下载远程服务器资源 文件'''
        ftpconncet = FtpDownLoad(host)
        ftpconncet.downLoadFile(remoteFile, localFile)
        
    @staticmethod  
    def downLoadPreResourceDir(remoteDir, localdir, host=None):
        '''下载远程服务器资源 目录'''
        ftpconncet = FtpDownLoad(host)
        ftpconncet.downLoadDir(remoteDir, localdir)
