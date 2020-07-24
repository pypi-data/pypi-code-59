# -*- coding=utf-8 -*-

from captcha.image import ImageCaptcha
from random import randint
import gvcode
import base64
from io import BytesIO


CHAR_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', #'i', 
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', #'I', 
        'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

class CaptchaHelper(object):

    @staticmethod
    def generate(length=4):
        
        chars = ''.join([(CHAR_LIST[randint(0, len(CHAR_LIST))])for i in range(length)])
        
        image = ImageCaptcha().generate_image(chars)

        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())
        # print(chars ,type(image),img_str)
        return chars, img_str
        # image.show()

# CaptchaHelper.generate()

# s, v = gvcode.generate() #序列解包
# s.show() #显示生成的验证码图片
# print(v) #打印验证码字符串
 
# image.show()
 
        # self.write(simplejson.dumps({'code': 0, 'img': stream.getvalue().encode('base64')}))
    #这里是将stream的值进行了一次base64的编码