import copy

from lung.controllers.core import Controller


class Lookahead(Controller):
    def __init__(self, forecast_model, base_controller, lookahead_steps, **kwargs):
        self.forecast_model = forecast_model
        self.base_controller = base_controller
        self.lookahead_steps = lookahead_steps

    def feed(self, state, t):
        dt = self.dt(t)

        controller_copy = copy.deepcopy(self.base_controller)
        self.forecast_model.update(state)
        u_in = 0
        for i in range(self.lookahead_steps):
            lookahead_state = self.forecast_model.predict(i)
            u_in = controller_copy.feed(lookahead_state, t + i * dt)

        self.base_controller.feed(state, t)
        return (u_in, self.u_out(t))
