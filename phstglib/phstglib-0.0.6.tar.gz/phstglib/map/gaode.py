from urllib.request import urlopen
from urllib.parse import *
import json


def lnglat2car(lng1, lat1, lng2, lat2, key="49a90a6e71c311843d5eb9ae406be79b"):
    """汽车导航

    Parameters
    ----------

    Return
    ------
    distance : float
        导航距离（米）
    duration : int
        导航时间（秒）
    """
    url="https://restapi.amap.com/v3/direction/driving?origin={},{}&destination={},{}&strategy=12&extensions=base&key={}".format(
        lng1, lat1, lng2, lat2, key)
    try:
        req = urlopen(url)
        content = req.read().decode('utf-8')
        distance = json.loads(content, encoding='gbk')['route']['paths'][0]['distance']
        duration = json.loads(content, encoding='gbk')['route']['paths'][0]['duration']
        return float(distance), float(duration)
    except Exception:
        print("{},{};{},{}获取汽车导航出现异常".format(lng1, lat1, lng2, lat2))
        return 0


def address2lnglat(address, ak='49a90a6e71c311843d5eb9ae406be79b'):
    """通过地址获取经纬度

    Parameters
    ----------
    address ： string
        详细地址
    ak ：string
        百度开发者key
    Return
    ------
    distance : float
        导航距离（米）
    duration : int
        导航时间（秒）
    """
    url= 'https://restapi.amap.com/v3/geocode/geo?address={}&output=JSON&key={}'.format(address, ak)
    url = quote(url, safe=string.printable)
    try:
        req = urlopen(url)
        content = req.read().decode('utf-8')
        print(content)
        location = json.loads(content, encoding='gbk')['geocodes'][0]['location']
        return location.split(',')[0], location.split(',')[1]
    except Exception:
        print("获取{}经纬度出现异常".format(address))
        return 0, 0