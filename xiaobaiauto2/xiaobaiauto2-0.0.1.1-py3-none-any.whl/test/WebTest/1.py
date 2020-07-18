#! /usr/bin/env python
__author__ = 'Tser'
__email__ = '807447312@qq.com'
__project__ = 'jicaiauto'
__script__ = '1.py'
__create_time__ = '2020/7/18 9:46'

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from jicaiauto.config.config import EMAILCONFIG
from datetime import datetime
from os.path import splitext, splitdrive, split



print(split('E:\\a/b\\c/d.html'))