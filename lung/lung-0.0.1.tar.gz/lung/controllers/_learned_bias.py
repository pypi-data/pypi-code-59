import numpy as np
from lung.controllers.core import Controller


class LearnedBias(Controller):
    def __init__(self, base_controller, bias_lr=0.01, **kwargs):
        self.base_controller = base_controller
        self.bias_lr = bias_lr
        self.bias = 0

    def feed(self, state, t):
        err = self.waveform.at(t) - state
        self.bias = self.bias + np.sign(err) * self.bias_lr
        base_control = self.base_controller.feed(state, t)
        return (base_control + self.bias, self.u_out(t))
