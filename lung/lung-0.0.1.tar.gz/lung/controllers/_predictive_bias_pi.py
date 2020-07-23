import numpy as np
from lung.controllers.core import Controller
from lung.controllers.core import LinearForecaster
from lung.controllers._pid import PID
from lung.controllers._lookahead import Lookahead


class PredictiveBiasPI(Controller):
    def __init__(self, p, i, RC, lookahead_steps=15, bias_lr=0.01, **kwargs):
        # controller coeffs
        self.bias_lr = bias_lr
        self.bias = 0
        self.waveform = waveform
        self.storage = 3
        self.forecaster = LinearForecaster(self.storage)
        self.pid = PID(self.waveform, [p, i, 0.0], RC=RC)
        self.base_controller = Lookahead(self.forecaster, self.pid, lookahead_steps)

    def feed(self, state, t):
        err = self.waveform.at(t) - state
        self.bias = self.bias + np.sign(err) * self.bias_lr
        base_control = self.base_controller.feed(state, t)
        return (base_control + self.bias, self.u_out(t))
