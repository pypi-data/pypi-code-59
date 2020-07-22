from robot_core.executor.executor import Executor


class AudioPlayerExecutor(Executor):

    def execute(self, **kwargs):
        from playsound import playsound
        playsound(kwargs["command"])

