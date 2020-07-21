# @Time : 2020/7/21 10:05 
# @Author : XX
# @File : v.py
# @Software: PyCharm

#!/usr/bin/env python
# coding:utf-8

import requests
from hashlib import md5

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


def getcode(im):
    chaojiying = Chaojiying_Client()
    return chaojiying.PostPic(im, 1902)['pic_str']






























































































#
# """
# 1、目标达成率，完成百分比，提升百分比
# 2、核心数据走势图
# 3、流量分析
# 4、转化率分析
# 5、模块点击分析
# 6、改进及优化
# （答案不唯一）
# """
#
# """
# 1.日常运营报告
# 日常运营报告通常是指新媒体运营部门每天、每周或每月、每季度需要给主管领导进行汇报，
# 这其中包括《网站流量日报》、《微信公众号粉丝周报》以及《今日头条阅读量周报、粉丝月报》还有《网站转化率月报》等
# 2.专项研究报告
# 专项研究报告主要是指针对某个特定问题进行的相关数据汇总和分析，比如《粉丝增长来源报告》、
# 《流量异常分析报告》、《上周广告投放效果报告》等，专项研究报告的重点是深入挖掘问题，以及寻找解决问题方案。
# 这些报告是针对特别事件孕育而生的产物，所以是不定期报告
# 3.行业分析报告
# 行业分析报告是对整个新媒体行业的情况汇总报告，主要是分析当前新媒体的相关情况，
# 这样可以有助于掌握整个趋势，比如抖音风刚起，就能判断短视频平台即将到来的大佬们都获得了最高的流量支持。
# 行业分析报告主要分两点，一是整个行业的报告，一是同行竞争对手的报告，整个行业趋势可以通过大数据来获得相关数据，
# 而同行分析，则是通过分析竞争对手的微博数据、微信数据来了解他们的大概情况。
# """
#
# """
# 1.PCA 的思想是将 n 维特征映射到 k 维上（k<n），这 k 维是全新的正交特征。
# 这 k 维特征称为主成分，是重新构造出来的 k 维特征，而不是简单地从 n 维特征中去除其余 n-k 维特征。
# PCA 的目的是选择更少的主成分（与特征变量个数相较而言），那些选上的主成分能够解释数据集中最大方差。
# 通过正交变换，各主成分的相对位置不发生变化，它只能改变点的实际坐标。
# """
#
# """
# 解决不平衡分类问题的策略可以分为两大类：一类是从训练集入手 ,
#  通过改变训练集样本分布，降低不平衡程度；另一类是从学习算法入手 ,
#  根据算法在解决不平衡问题时的缺陷 , 适当地修改算法使之适应不平衡分类问题。
#  平衡训练集的方法主要有训练集重采样 (re-sampling)方法和训练集划分方法。
#  学习算法层面的策略包括分类器集成 、代价敏感学习和特征选择方法等。
# """

