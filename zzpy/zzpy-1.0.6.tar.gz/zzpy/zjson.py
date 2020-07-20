import json
import datetime


class DateEncoder(json.JSONEncoder):
    """
    Json 无法解析 datatime 类型的数据，构建 DateEncoder 类解决 datatime 解析问题
    https://blog.csdn.net/yilovexing/article/details/93633436
    """

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return super.default(obj)
            # return json.JSONEncoder.default(self, obj)


def jsondumps(obj):
    return json.dumps(obj, cls=DateEncoder)


def main():
    print(jsondumps({"k": 1, "d": datetime.datetime.now()}))


if __name__ == "__main__":
    main()
