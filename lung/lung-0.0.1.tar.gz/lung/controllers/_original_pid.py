import numpy as np

from lung.controllers.core import Controller
from lung.controllers.core import Phase
from lung.controllers._pid import PID

# Adapted directly from _PID_update in
# https://github.com/mschottdorf/Ventilator-Dev/blob/fancy_control/vent/controller/control_module.py
class OriginalPID(Controller):
    def __init__(
        self,
        K=[2.0, 2.0, 0.0],
        offset=0.0,
        pip_gain=1.0,
        i_phase=1.0,
        peep_time=0.5,
        cycle_duration=3.0,
        RC=0.3,
        **kwargs
    ):
        self.K_P, self.K_I, self.K_D = K
        self.pip_gain = pip_gain
        self.i_phase = i_phase
        self.peep_time = peep_time
        self.cycle_duration = cycle_duration
        self.RC = RC
        self.filter = np.zeros(3)
        self.PID = PID(waveform=self.waveform, K=K, RC=RC)

    def feed(self, state, t):
        dt = self.dt(t)
        phase = self.phase(t)

        u_in = 0
        if phase == Phase.RAMP_UP or phase == Phase.PIP:
            # __get_PID_error
            pid_signal = self.PID.feed(state, t)

            # __calculate_control_signal_in
            self.filters[0] = pid_signal
            self.filters = np.roll(self.filters, -1)
            u_in = np.mean(self.filters)

        elif phase == Phase.RAMP_DOWN:
            u_in = 0

        else:
            u_in = 5 * (1 - np.exp(5 * (self.peep_time + self.i_phase) - t))


        return (u_in, self.u_out(t))
