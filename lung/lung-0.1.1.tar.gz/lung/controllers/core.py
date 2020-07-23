import abc
from enum import Enum
import numpy as np

from lung.utils import BreathWaveform


ControllerRegistry = []


class Phase(Enum):
    RAMP_UP = 1
    PIP = 2
    RAMP_DOWN = 3
    PEEP = 4


class Controller(abc.ABC):
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj.__setattr__("name", cls.__name__)
        obj.__setattr__("time", float("inf"))
        obj.__setattr__("waveform", BreathWaveform())

        for kw, arg in kwargs.items():
            obj.__setattr__(kw, arg)

        return obj

    @classmethod
    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)
        if cls.__name__ not in [ctrl.__name__ for ctrl in ControllerRegistry]:
            ControllerRegistry.append(cls)

    @abc.abstractmethod
    def feed(self, state, t):
        pass

    def u_out(self, t):
        phase = self.phase(t)
        u_out = np.zeros_like(phase)
        u_out[np.equal(phase, Phase.RAMP_DOWN.value)] = 1
        u_out[np.equal(phase, Phase.PEEP.value)] = 1

        return u_out if np.isscalar(t) else u_out[0]

    def dt(self, t):
        dt = max(0, t - self.time)
        self.time = t
        return dt

    def cycle_phase(self, t):
        return t % self.waveform.period

    def phase(self, t):
        return self.waveform.phase(t)


class LinearForecaster:
    def __init__(self, history_length):
        self.history = np.zeros(history_length)
        self._update_lin_fit()

    def update(self, value):
        self.history[0] = value
        self.history = np.roll(self.history, -1)
        self._update_lin_fit()

    def predict(self, steps_ahead):
        return self.lin_fit(len(self.history) + steps_ahead)

    def _update_lin_fit(self):
        self.lin_fit = np.poly1d(np.polyfit(range(len(self.history)), self.history, 1))
