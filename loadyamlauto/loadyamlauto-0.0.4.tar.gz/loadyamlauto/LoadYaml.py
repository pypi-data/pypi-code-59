

from __future__ import print_function

import io
import os

import yaml

'''
此函数使用递归调用方式，一层一层遍历yaml文件逻辑结构，并返回一个生成器，便于在大文件形式下
遍历
'''


def dict_generator(indict, pre=None):
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict):
                if len(value) == 0:
                    yield pre + [key, '{}']
                else:
                    for d in dict_generator(value, pre + [key]):
                        yield d
            elif isinstance(value, list):
                if len(value) == 0:
                    yield pre + [key, '[]']
                else:
                    for v in value:
                        for d in dict_generator(v, pre + [key]):
                            yield d
            elif isinstance(value, tuple):
                if len(value) == 0:
                    yield pre + [key, '()']
                else:
                    for v in value:
                        for d in dict_generator(v, pre + [key]):
                            yield d
            else:
                yield pre + [key, value]
    else:
        yield pre + [indict]


'''
这里将遍历的key值用＿连接起来就是yaml的层次逻辑结构，然后通过os.enviro获取本地计算机环境变量，
通过遍历yaml所有key与本地环境变量列表进行匹配，key值匹配成功，本地环境变量覆盖yaml读入内存
的数据
'''

def loadyaml(config_file):
    global conf
    conf_file = io.open(config_file, 'r', encoding="utf-8")
    conf_data = conf_file.read()
    conf_file.close()
    conf = yaml.load(conf_data)
    for item in dict_generator(conf):
        #item这里遍历出一个一个列表，附带yaml的层级结构
        # 这里通过load加载yaml文件json字典格式数据，通过遍历本地环境变量方式赋值给conf["key"]，［0:-1］表示列表第一个元素到倒数第二个元素
        env_key = '_'.join(item[0:-1]).upper()
        env_value = os.environ.get(env_key)
        #print(type(env_value))
        #print('%s=%s' % (env_key, env_value))
        #None表示一个空对象，''表示为一个空字符，空字符还用默认值，什么都不做,后面都是在本地计算机找到了环境变量
        if env_value is None or env_value == '':
            continue
        # 非法项
        if len(item) == 0:
            return
        # 单层配置,此时只有key值，没有value值
        if len(item) == 1:
            conf[item[0]] = env_value
        # 获取最后一层 dict/array，这里使用对象引用，改变变量，tmp改变,conf也会随之改变,此时已经遍历找到了最后一层，保存了层次结构，可以直接通过列表下标访问与之对应的值
        tmp = conf
        #此时已经表示找到了最后一层,遍历后存的就为最后一层
        for i in range(0, len(item) - 2):
            tmp = tmp[item[i]]

        if isinstance(tmp[item[-2]],list):
             if isinstance(item[-1],int):
                 tmp[item[-2]]=env_value
                 converttmp=tmp[item[-2]].lstrip('[').rstrip(']').split(',')
                 tmp[item[-2]]= list(map(int, converttmp))

             if isinstance(item[-1],float):
                 tmp[item[-2]]=env_value
                 converttmp=tmp[item[-2]].lstrip('[').rstrip(']').split(',')
                 tmp[item[-2]]= list(map(float, converttmp))

             if isinstance(item[-1],bool):
                 tmp[item[-2]]=env_value
                 converttmp=tmp[item[-2]].lstrip('[').rstrip(']').split(',')
                 tmp[item[-2]]= list(map(bool, converttmp))

             if isinstance(item[-1],str):
                tmp[item[-2]]=env_value
                converttmp=tmp[item[-2]].lstrip('[').rstrip(']').split(',')
                tmp[item[-2]]= list(map(str, converttmp))
        else:
             if isinstance(item[-1],float):
                 tmp[item[-2]] = float(env_value)
             if isinstance(item[-1],int):
                 tmp[item[-2]] = int(env_value)
             if isinstance(item[-1],bool):
                 tmp[item[-2]] = bool(env_value)
             if isinstance(item[-1],str):
                 tmp[item[-2]] = str(env_value)
 
'''
这里测试调用loadyaml函数，传入参数yaml文件名，输出json文件判断此时内存中数据是否已经修改
'''

#loadyaml("./LoadYaml.yaml")
#print(type(conf["shsjzx"]["database"]["name"]["address"]))
#print(conf)

