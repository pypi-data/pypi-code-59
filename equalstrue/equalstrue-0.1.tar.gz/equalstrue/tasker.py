#%%
import time
from datetime import datetime, timedelta
class Tasker:
    """[summary]
    """
    def __init__(self) -> None:
        """[summary]
        """
        self.tasks=[]
        self.start_time = datetime.now()
    
    def register(self,**kwargs1):
        """[summary]
        """
        def wrapper(*args,**kwargs):
            kwargs = {**kwargs,**kwargs1}
            self.add_task(*args,**kwargs)
        return wrapper

    def add_task(self,task,interval=timedelta(seconds=1)):
        """[summary]

        Args:
            task ([callable/string]): [description]
            interval ([type], optional): [description]. Defaults to timedelta(seconds=1).
        """
        if isinstance(task,str):
            self.tasks.append({'name':task,'interval':interval,'type':str, 'action':lambda:print(task),'last_run':self.start_time})
        if callable(task):
            self.tasks.append({'name':task.__name__,'interval':interval,'type':str ,'action':task,'last_run':self.start_time})
    
    def run(self):
        try:
            self.start_time = datetime.now()
            while len(self.tasks)>0:
                time.sleep(1)
                cur_time = datetime.now()
                due_tasks = [task for task in self.tasks if (task['last_run'] + task['interval'])<cur_time]
                print(f'\r {datetime.now():%H:%M:%S%p}', end='')
                for task in due_tasks:
                    print(f' Running {task["name"]}',end='')
                    task['last_run'] = cur_time
                    task['action']()
                    
        except KeyboardInterrupt as identifier:
            pass