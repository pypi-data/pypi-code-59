import time

from onecat_task_queue.queue import TaskQueue
from onecat_task_queue.task import Task

if __name__ == '__main__':
    task_queue = TaskQueue()


    def fun1():
        time.sleep(1)
        return 1


    def fun2():
        time.sleep(1)
        return 2


    task_queue.put(Task(
        func=fun1,
        callback=lambda task, result: print(f'task1 result: {result}'),
    ))
    task_queue.put(Task(
        func=fun2,
        callback=lambda task, result: print(f'task2 result: {result}'),
    ))

    task_queue.run()
