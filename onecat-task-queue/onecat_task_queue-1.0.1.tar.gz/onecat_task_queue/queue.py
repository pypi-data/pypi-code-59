#  Copyright (c) intmain 2020.

import threading
import sys
import heapq
from .task import Task
from .redirect import Redirection


class PriorityQueue:
    """
    自己实现的优先级队列
    参考：https://zhuanlan.zhihu.com/p/37637660
    """

    def __init__(self):
        self._index = 0
        self.queue = []

    def push(self, priority, val):
        heapq.heappush(self.queue, (priority, self._index, val))
        self._index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]

    @property
    def empty(self):
        return len(self.queue) == 0


class TaskQueue:
    """
    基于线程的异步任务队列
    todo 下次做一个基于进程的队列，充分利用多核CPU性能
    """

    def __init__(self, output_redirect=False):
        self.queue = PriorityQueue()
        self.output_redirect = output_redirect
        self._redirect_objs = {}
        self._results = {}

    def put(self, task: Task):
        """
        将task加入任务列表
        Args:
            task:
        Returns: 返回task id
        """
        self.queue.push(task.priority, task)
        return task.id

    def get(self):
        """
        从任务队列中出列一个任务
        """
        return self.queue.pop()

    def run(self):
        """
        按照优先级从当前任务队列中取出任务执行
        """
        while not self.queue.empty:
            task = self.get()
            # 开启新线程
            t = threading.Thread(target=self._task_wrapper, name=task.id, args=[task])
            self._log(f'Start thread {task.id}')
            t.start()

    def get_output(self, task_id: str) -> Redirection:
        return self._redirect_objs.get(task_id, None)

    def get_result(self, task_id: str):
        return self._results.get(task_id, None)

    @staticmethod
    def _log(msg: str):
        """
        日志输出接口，可以替换为日志组件
        Args:
            msg: 日志内容
        """
        print(f'[TaskQueue] {msg}')

    def _task_wrapper(self, task: Task):
        if self.output_redirect:
            if task.id in self._redirect_objs:
                redirect_obj = self._redirect_objs[task.id]
            else:
                redirect_obj = Redirection(2048)
                self._redirect_objs[task.id] = redirect_obj
            # 重定向输出
            sys.stdout = redirect_obj
            task.outputs = redirect_obj
            result = task.run()
            # 恢复默认输出
            redirect_obj.reset()
            self._log(f'Task finished. {task.id}')
        else:
            result = task.run()

        # 保存结果
        self._results[task.id] = result
