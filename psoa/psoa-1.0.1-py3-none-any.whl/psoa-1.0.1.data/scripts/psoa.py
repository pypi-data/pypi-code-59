'''
An implementation of the Particle Swarm Optimization algorithm

Args:
--------------------
To be added

Returns:
--------------------
parameters -- list of float
              a list of estimated parameters that optimize the objective function
best_objective_result -- float,
                         best result measured with the objective function

Examples:
--------------------
>>> s = swarm()
>>> obj1 = lambda x: -((x[0] - 10) ** 2 + (x[1] - 25) ** 2)
>>> s.maximize(obj1)
([10.0, 25.0], -0.0)
>>> # Rastrigin function
>>> obj2 = lambda x: 10 * len(x) + np.sum([xi ** 2 - 10 * np.cos(2 * np.pi * xi) for xi in x])
>>> s.minimize(obj2, dim=5, max_iteration=1e5, boundaries=((-5.12, -5.12, -5.12, -5.12, -5.12),
>>>                                                        (5.12, 5.12, 5.12, 5.12, 5.12)))
([-2.0902191353445784e-09,
  -6.659027711151939e-10,
  -4.9074379144973505e-09,
  1.1250520464439336e-09,
  -3.42855219094123e-10],
 0.0)

References:
--------------------
[1] "James McCaffrey: Swarm Intelligence Optimization using Python",
    Video from PyData Seattle 2015,
    available at https://www.youtube.com/watch?v=bVDX_UwthZI&t=1038s,
    accessed on 2020-07-04
'''


import numpy as np


class swarm(object):

    default_population = 100
    default_friction_weight = 1 - 0.729  # friction force
    default_cognitive_weight = 1.49445  # attraction force towards particles' best positions
    default_social_weight = 1.49445  # attraction force towards swarm' best position
    default_dim = 2
    default_max_iteration = 1e4
    default_stop_criteria_coef = 5
    # stop if the best result doesn't change in (max_iteration over this number) of iterations

    def __init__(self, population=default_population,
                 friction_weight=default_friction_weight,
                 social_weight=default_social_weight,
                 cognitive_weight=default_cognitive_weight):
        self.population = population
        self.friction_weight = friction_weight
        self.cognitive_weight = cognitive_weight
        self.social_weight = social_weight

    def maximize(self, *args, **kwargs):  # when we want to maximize the objective function
        self.extreme, self.arg_extreme = np.max, np.argmax
        self.better = np.greater
        return self.optimize(*args, **kwargs)

    def minimize(self, *args, **kwargs):  # when we want to maximize the objective function
        self.extreme, self.arg_extreme = np.min, np.argmin
        self.better = np.less
        return self.optimize(*args, **kwargs)

    def optimize(self, objective_function, dim=default_dim,
                 initial_values=None, boundaries=None,
                 max_iteration=default_max_iteration,
                 stop_criteria_coef=default_stop_criteria_coef):
        self.dim = dim  # how many parameters in objective function
        self.obj = objective_function  # objective function
        self.max_iteration = int(max_iteration)
        self.stop_iter = self.max_iteration // stop_criteria_coef
        if boundaries is None:
            self.boundaries = None
            self.param_mins, self.param_maxs = None, None
        else:
            self.boundaries = np.array(boundaries)
            self.param_mins, self.param_maxs = self.boundaries
        self.boundaries = None if boundaries is None else np.array(boundaries)
        self.initialize_position_velocity(initial_values)
        self.losses = []
        for i in range(self.max_iteration):
            self.update()
            self.losses.append(self.swarm_best_obj)
            # stop if the best result doesn't change in "stop_iter" of iterations
            if len(self.losses) >= self.stop_iter and self.losses[-1] == self.losses[-self.stop_iter]:
                print('stopped early at %d interations' % i)
                break
        return self.swarm_best_pos.tolist(), self.swarm_best_obj

    def update(self):
        # In each step, a particle receives three forces
        # - a friction force that slows down the particle
        # - a random attraction force towards the particle's previous best position
        # - a random attraction force towards the swarm's previous best position
        # they are used to update the particle's velocity
        self.s_c_rnds = np.random.random(size=(2 * self.population, self.dim))
        self.velocities = ((1 - self.friction_weight) * self.velocities +  # friction
                           self.s_c_rnds[:self.population] * self.cognitive_weight *
                           (self.particle_best_pos - self.positions) +  # attraction
                           self.s_c_rnds[self.population:] * self.social_weight *
                           (self.swarm_best_pos - self.positions))  # another attraction
        # update the positions using the particle velocities
        self.positions = self.positions + self.velocities
        # reflecting boundaries
        if self.boundaries is not None:
            self.positions_clipped = self.positions.clip(self.param_mins, self.param_maxs)
            self.velocities *= 1 - (self.positions != self.positions_clipped) * 2
            self.positions = self.positions_clipped
        # record particles' best positions
        self.curr_objs = np.apply_along_axis(self.obj, 1, self.positions)
        self.particle_best_pos = (self.positions * self.better(self.curr_objs, self.best_objs
                                                               ).reshape(-1, 1) +
                                  self.particle_best_pos * (~self.better(self.curr_objs, self.best_objs)
                                                            ).reshape(-1, 1))
        self.best_objs = self.extreme([self.best_objs, self.curr_objs], axis=0)
        # record swarm's best positions
        self.swarm_best_pos = self.particle_best_pos[self.arg_extreme(self.best_objs)]
        self.swarm_best_obj = self.extreme(self.best_objs)

    def initialize_position_velocity(self, initial_values):
        if self.boundaries is not None:
            # if no boundary conditions are given
            # randomly assign positions within boundaries
            # randomly assign velocities with maximum velocity equals to half of the boundary width
            self.positions = np.random.uniform(self.param_mins, self.param_maxs,
                                               size=(self.population, self.dim))
            self.velocities = np.random.uniform(self.param_mins / 2, self.param_maxs / 2,
                                                size=(self.population, self.dim))
        else:
            # if no boundary condition is given
            # randomly assign velocities and positions between 0 and 1
            self.positions = np.random.random(size=(self.population, self.dim))
            self.velocities = np.random.random(size=(self.population, self.dim))
        if initial_values is not None:  # we could pass initial values for one and only one particle
            self.positions[0] = np.array(initial_values)
        self.particle_best_pos = self.positions
        self.best_objs = np.apply_along_axis(self.obj, 1, self.positions)
        self.swarm_best_pos = self.particle_best_pos[self.arg_extreme(self.best_objs)]
