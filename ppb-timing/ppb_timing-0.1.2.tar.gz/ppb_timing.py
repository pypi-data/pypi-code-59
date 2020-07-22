from dataclasses import dataclass
from types import FunctionType
from typing import Optional

import ppb
from ppb.events import *
from ppb.systemslib import System
from ppb.utils import get_time


@dataclass
class Timer:
    end_time: float
    callback: FunctionType
    repeating: float = 0
    clear: bool = False
    until: float = None

    def __hash__(self):
        return hash(id(self))
    
    def cancel(self):
        self.clear = True


class Timers(System):

    @classmethod
    def delay(cls, seconds, func):
        t = Timer(get_time() + seconds, func)
        cls.scene.timers.add(t)
        return t
    
    @classmethod
    def repeat(cls, seconds, func, until=None):
        n = get_time()
        until = until if until is None else n + until
        t = Timer(n + seconds, func, repeating=seconds, until=until)
        cls.scene.timers.add(t)
        return t
    
    @classmethod
    def on_scene_started(cls, ev: SceneStarted, signal):
        ev.scene.timers = set()
        cls.scene = ev.scene
    
    @classmethod
    def on_scene_continued(cls, ev: SceneContinued, signal):
        cls.scene = ev.scene

    @classmethod
    def on_update(cls, ev: Update, signal):
        clear = []
        for t in list(ev.scene.timers):
            if t.clear:
                clear.append(t)
            else:
                now = get_time()
                if now >= t.end_time:
                    if t.until is None or t.until > now:
                        t.callback()
                    if t.repeating > 0:
                        if t.until is None or t.until > now:
                            t.end_time += t.repeating
                            continue
                    clear.append(t)
        for t in clear:
            cls.scene.timers.remove(t)


delay = Timers.delay
repeat = Timers.repeat
