#! /usr/bin/env python
__author__ = 'Tser'
__email__ = '807447312@qq.com'
__project__ = 'jicaiauto'
__script__ = 'jicaiautoTimer.py'
__create_time__ = '2020/7/21 9:36'

import sys
_cpath_ = sys.path[0]
sys.path.remove(_cpath_)
from jicaiauto.utils.jicaiautoTimer import main as jicaiauto_gui
sys.path.insert(0, _cpath_)

def main():
    jicaiauto_gui()