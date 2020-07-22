#  Copyright (c) intmain 2020.

import uuid
from . import priority as Priority
from .redirect import Redirection


class Task:
    def __init__(self, func, callback=None, priority=Priority.MIDDLE, args=(), kwargs={}):
        """
        Args:
            func: 需要执行的函数
            callback:  执行完的回调函数
            priority: 优先级
            *args:
            **kwargs:
        """
        self._id = uuid.uuid4().hex
        self.function = func
        self.callback = callback
        self.priority = priority
        self.args = args
        self.kwargs = kwargs
        # 任务运行过程的输出，stdout的输出
        self._outputs: Redirection = None

    @property
    def id(self):
        return self._id

    @property
    def outputs(self) -> Redirection:
        return self._outputs

    @outputs.setter
    def outputs(self, value: Redirection):
        self._outputs = value

    def run(self):
        try:
            if self.callback:
                # 回调函数原型 callback(task_obj, result)
                result = self.callback(self, self.function(*self.args, **self.kwargs))
            else:
                result = self.function(*self.args, **self.kwargs)
            return result
        except Exception as e:
            if self.callback:
                result = self.callback(self, e)
            else:
                result = e
            return result
