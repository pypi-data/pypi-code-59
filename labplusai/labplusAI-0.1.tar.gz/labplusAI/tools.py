# coding=UTF-8
"""
import matplotlib.pyplot as plt
from skimage import io as skio
from skimage import transform
import pandas as pd
import shutil
import keras
from keras import layers
import time
import warnings
warnings.filterwarnings("ignore")
"""
import os, zipfile
import re
import cv2
import json
import math
import random
import requests
import time, datetime
import subprocess
import hashlib
import numpy as np
import pandas as pd
from PIL import Image
from skimage import io as skio
from requests_toolbelt.multipart import encoder

class video2image():

    def __init__(self, name='', image_resize=(30,30)):
        """
        video2image构造函数，传入名称name和目标图片尺寸image_resize
        """
        if name == '':
            self.name = str(int(time.time()))
        else:
            self.name = name
        self._path = self.name + "_imgs"
        self.image_resize = image_resize
        self.video_index = -1
        self.has_converted = False
        
        if os.path.exists(self._path):
            
            if os.path.exists(self._path + "/config.json"):
                with open(self._path + "/config.json", 'r') as f:
                    try:
                        config = json.load(f)
                        if "image_resize" in config.keys() and config["image_resize"] == list(image_resize) and config["video_index"] >= 0:
                            self.video_index = config["video_index"]
                            self.has_converted = True
                            return
                    except:
                        pass
                   
            os.remove( self._path + "/config.json" )
            if os.path.exists(self._path + "/images"):
                for f in os.listdir( self._path + "/images" ):
                    fp = os.path.join( self._path, "images", f)
                    if os.path.isfile(fp):  os.remove( fp )
            else:
                os.mkdir( self._path + "/images" )
        else:
            os.mkdir( self._path )
            os.mkdir( self._path + "/images" )

        config = {}
        config["image_resize"] = self.image_resize

        with open(self._path + "/config.json", 'w') as f:
            json.dump(config, f)


    def set_video_label(self, source, label):
        """
        在当前目录下生成一个以 video2image.name 命名的文件夹,如./sig,文件夹结构如下：
        ./
            sig/
                config.json     # config文件中存储一些配置信息，如当前的image_resize值，label文本（按set_video_label执行顺序确定0、1、2....）
                images/
                    null_2020-5-12-10-10-10-0.png   # 考虑同一个标签多个视频文件，因此最终图片的命名规则为:  label_时间日期戳_序号.png
                    null_2020-5-12-10-10-10-1.png
                    .............................
        """
        if not os.path.exists(source):
            print("[video2image.set_video_label] file does not exist")
            return

        config = {}
        has_label = False
        if os.path.exists(self._path + "/config.json"):
            with open(self._path + "/config.json", 'r') as f:
               config = json.load(f)
            for index in range(self.video_index, -1, -1):
                key = "label_" + str(index)
                if key in config:
                    if label == config[key]:
                        has_label = True
                        break
        else:
            config["image_resize"] = self.image_resize
        
        if not has_label:
            self.video_index += 1
            config["label_" + str(self.video_index)] = label

        config["video_index"] = self.video_index

        with open(self._path + "/config.json", 'w') as f:
            json.dump(config, f)

        cap = cv2.VideoCapture( source )
        frame_count = int(cap.get(7))

        now = datetime.datetime.now()
        timestamp = now.strftime("_%Y-%m-%d-%H-%M-%S_")
        temp_path = self.path() + "/images/" + label + timestamp
        for c in range(frame_count):
            ret,frame = cap.read()
            save_path = temp_path + str(c) + ".jpg"
            cv2.imencode('.jpg', frame)[1].tofile(save_path)
            img = Image.open(save_path)

            ratio = (img.size[0] * self.image_resize[1]) / (img.size[1] * self.image_resize[0])
            if ratio > 1:
                # 裁切x轴
                crop_len = int( (img.size[0] - (self.image_resize[0] * img.size[1] / self.image_resize[1]) ) / 2 )
                img = img.crop((crop_len, 0, img.size[0] - crop_len, img.size[1]))
            elif ratio < 1:
                # 裁切y轴
                crop_len = int( (img.size[1] - (self.image_resize[1] * img.size[0] / self.image_resize[0]) ) / 2 )
                img = img.crop((0, crop_len, img.size[0], img.size[1] - crop_len))
           
            img = img.resize( self.image_resize, Image.ANTIALIAS)
            img.save(save_path)
            print( "\r"+"progress label:[{}] {}/{}".format(label, c+1, frame_count), end="" ,flush=True)
        print("")

        
    def labels(self):
        """
        通过config获取标签文本列表
        """
        if os.path.exists(self._path + "/config.json"):
            with open(self._path + "/config.json", 'r') as f:
                config = json.load(f)
                _labels = []
                for index in range(self.video_index + 1):
                    key = "label_" + str(index)
                    if key in config: _labels.append(config[key])
                return _labels
        else:
            return []
        
    def path(self):
        """
        获取之前生成的文件夹绝对路径
        """
        return os.path.abspath(self._path)
        
    def data(self, shuffle=True):
        """
        将images文件夹下的图片读取为ndarray格式，最终返回一个元组(x,y),x、y都是ndarray
        shuffle参数默认为True，即需要打乱顺序
        """
        config = None
        with open(self._path + "/config.json", 'r') as f:
            config = json.load(f)
        
        if config is None: return None, None

        _dict = {}
        for index in range(self.video_index + 1):
            key = "label_" + str(index)
            if key in config: _dict[config[key]] = index

        imglist = []
        labellist = []
        for imgpath in os.listdir(self._path + "/images"):
            img = skio.imread(os.path.join(self._path, "images", imgpath))
            imglist.append(img)
            _label = imgpath.split("_")[0]
            if _label in _dict: labellist.append(_dict[_label])

        x_data = np.array(imglist)
        y_data = np.array(pd.get_dummies(np.array(labellist)))
        x_data = x_data/255

        if shuffle:
            indices = np.arange(x_data.shape[0])
            np.random.shuffle(indices)
            x_data = x_data[indices]
            y_data = y_data[indices]

        return x_data, y_data


