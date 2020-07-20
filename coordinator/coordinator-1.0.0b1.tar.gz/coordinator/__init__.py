from collections import defaultdict


class Coordinator:
    def fire_hook(self, hook="default", context={}):
        """
        Fires a hook, calling all of its functions.

        :param hook: The hook name to call, defaults to "default"
        :type hook: str, optional
        :param context: A dict to pass to each function
        :type context: dict, optional
        """

        for f in self._hooks_db[hook]:
            self._run_task(f, context)

    def register_task(self, hook="default"):
        """
        A decorator to register a task to a hook.

        :param hook: The hook name to register with, defaults to "default"
        :type hook: str, optional
        """
        def _register_task(f):
            self._hooks_db[hook].append(f)
            return f

        return _register_task

    def __init__(self, huey=None):
        """
        Initializes a hook coordinator instance.

        :param huey: The Huey instance to use. Defaults to None, which will create a MiniHuey instance.
        :type huey: Huey, MiniHuey
        :return: The coordinator object.
        :rtype: Coordinator
        """
        if huey:
            self._huey = huey
        else:
            from huey.contrib.mini import MiniHuey
            self._huey = MiniHuey()
        self._hooks_db = defaultdict(list)

        @self._huey.task()
        def _run_task(f, context):
            return f(context)

        self._run_task = _run_task
