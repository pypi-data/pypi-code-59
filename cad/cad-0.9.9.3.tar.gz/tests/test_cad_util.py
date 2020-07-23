#!/usr/bin/env python
# -*- coding:utf-8 _*-  
"""
@license : Copyright(C), WAYZ
@author  : Bruce Liu
@time    : 2020/2/4 10:39
@contact : bruce.liu@wayz.ai
"""
from cad.cad_util import CadUtil
from unittest import TestCase

ak_list = [
    '720a09b16e7f7f2c',
]


class TestCadUtil(TestCase):
    def test_get_ak(self):
        """

        :return:
        """
        client = CadUtil('172.3.0.28:6379/1', '123', 'midend_management_system:app_config')
        for ak in ak_list:
            data = client.get(ak)
            self.assertIsInstance(data, dict)
            print(data)


if __name__ == '__main__':
    client = CadUtil('172.3.0.28:6379/3', '123', 'midend_management_system:app_config')
    for ak in ak_list:
        data = client.get(ak)
        print(data)

