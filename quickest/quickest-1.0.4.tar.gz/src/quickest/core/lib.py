import os, json, logging


import numpy as np
from scipy.stats import rv_discrete, norm
from scipy.special import expit, logit


CONTINUE = 0
STOP = 1


class Module:
    def __iter__(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    @classmethod
    def opts(cls):
        return [subclass.__name__ for subclass in cls.__subclasses__()]


#  Universal factory for modules that may or may not exhibit polymorphism
class ModuleFactory:
    def _get_module(self, base_cls, type=None, **kwargs):

        if len(base_cls.__subclasses__()) == 0:
            return base_cls(**kwargs)

        else:
            if type == None:
                type = base_cls.__subclasses__()[0].__name__

            for subclass in base_cls.__subclasses__():
                if type == subclass.__name__:
                    return subclass(**kwargs)

        raise AttributeError("Class {} has no subclass {}".format(base_cls, type))


class ChangeProcess(Module):
    def __init__(
        self,
        delay_cost=0.001,
        false_alarm_cost=1,
        max_duration=10000,
        observation_pdfs=[[0, 1], [0.1, 1], [0.2, 1], [0.5, 1]],
        initial_distribution=[0.5, 0.5, 0, 0],
        num_states=4,
        num_pre_change_states=2,
    ):

        self._delay_cost = 0.001
        self._false_alarm_cost = 1
        self._max_duration = 10000
        self._state_space = list(range(num_states))
        self._simulation_time = 0
        self._num_pre_change_states = num_pre_change_states
        self._history = np.zeros(self._max_duration, dtype=np.uint8)
        self._change_time = np.nan
        self._initial_distribution = rv_discrete(
            name="initial_distribution",
            values=(self._state_space, initial_distribution),
        )
        self._observation_pdfs = []

        for pdf in observation_pdfs:
            self._observation_pdfs.append(norm(pdf[0], pdf[1]))

        self._hidden_state = 0

    def __call__(self, action, dynamics):
        """[summary]

        Args:
            action ([type]): [description]
            dynamics (quickest.core.lib.Dynamics): The dynamics to use for the hidden state update

        Returns:
            [type]: [description]
        """

        cost = self._detection_penalty(action)

        new_state = dynamics(self._hidden_state)

        if (np.isnan(self._change_time)) and not (
            new_state in list(range(self._num_pre_change_states))
        ):

            self._change_time = self._simulation_time

        self._hidden_state = new_state
        self._history[self._simulation_time] = self._hidden_state
        self._simulation_time = self._simulation_time + 1

        return cost

    def __iter__(self):
        yield ("delay_cost", self._delay_cost)
        yield ("false_alarm_cost", self._false_alarm_cost)
        yield ("max_duration", self._max_duration)
        yield ("num_states", len(self._state_space))
        yield ("num_pre_change_states", self._num_pre_change_states)
        yield ("initial_distribution", self._initial_distribution.pk.tolist())

        observation_pdfs = []
        for pdf in self._observation_pdfs:
            observation_pdfs.append(list(pdf.args))
        yield ("observation_pdfs", observation_pdfs)

    @property
    def max_duration(self):
        return self._max_duration

    @property
    def num_states(self):
        return len(self._state_space)

    @property
    def num_pre_change_states(self):
        return self._num_pre_change_states

    @property
    def observation_pdfs(self):
        return self._observation_pdfs

    @property
    def state_history(self):
        return self._history

    @property
    def change_point(self):
        if not np.isnan(self._change_time):
            return self._change_time
        else:
            return None

    @property
    def initial_belief(self):
        return self._initial_distribution.pk.tolist()

    def observe(self):
        # TODO - sample from observation pdfs
        return self._observation_pdfs[self._hidden_state].rvs()

    def reset(self):
        self._hidden_state = self.sample_initial_state()
        self._history.fill(0)
        self._simulation_time = 0

    def sample_initial_state(self):
        return self._initial_distribution.rvs()

    # TODO How to handle different types of costs? Will action always be stop/go?

    def _detection_penalty(self, action):
        """Returns the cost of taking an action when only considering detection (not isolation)

        Args:
            action (int): 0 (continue) or 1 (stop)
        """

        # Check if simulation has finished
        penalty = 0

        if action == STOP:

            if not np.isnan(self._change_time):
                time_since_change = np.float64(
                    self._simulation_time - self._change_time
                )
                penalty = self._delay_cost * time_since_change
            else:
                penalty = self._false_alarm_cost

        elif action == CONTINUE:

            if self._simulation_time == self._max_duration:

                if not np.isnan(self._change_time):
                    time_since_change = self._simulation_time - self._change_time
                    penalty = self._delay_cost * time_since_change

        else:
            raise ValueError("action must be in 0 (continue) or 1 (stop)")

        return np.float64(penalty)


class FilterMixin:
    def _filter(self, measurement, prior_belief, transition_matrix, observation_pdfs):
        """[summary]

        Args:
            measurement (float): 
            prior_belief (array-like): 
            transition_matrix ([type]): 
            observation_pdfs ([list of scipy.stats.rv_discrete]):
        """

        likelihoods = np.zeros_like(observation_pdfs)

        for i in range(len(observation_pdfs)):
            likelihood = observation_pdfs[i].pdf(measurement)
            likelihoods[i] = likelihood

        N = len(likelihoods)
        likelihood_matrix = np.zeros((N, N), dtype=np.float64)

        for i in range(N):
            likelihood_matrix[i, i] = likelihoods[i]

        unnormalised_estimate = np.matmul(
            np.matmul(likelihood_matrix, np.transpose(transition_matrix)), prior_belief
        )

        belief = unnormalised_estimate / np.sum(unnormalised_estimate)

        return belief


class Policy(Module):
    def __call__(self):
        raise NotImplementedError

    @property
    def params(self):
        raise NotImplementedError

    @staticmethod
    def _reparameterise(decision_parameters):
        # decision_parameter(s) to free params
        raise NotImplementedError

    @staticmethod
    def _deparameterise(free_parameters):
        # free params to decision_parameters
        raise NotImplementedError


class ChangeDetector(Policy):
    def __init__(self, threshold=None):
        """A detector that marginalises pre- and post-belief states to the belief 
        that the change has or has not occurred, then compares that belief
        to a scalar threshold in [0,1].

        Args:
            threshold (float): The decision threshold. Defaults to 0.5.
        """
        if threshold == None:
            threshold_ = 0.5
        else:
            threshold_ = threshold
        self._free_params = self._reparameterise(threshold_)

    def __repr__(self):
        return "ChangeDetector"

    def __iter__(self):
        yield ("type", self.__repr__())
        yield ("threshold", self._deparameterise(self._free_params))

    def __call__(self, belief, num_pre_change_states):
        """The core policy method

        Args:
            belief (Array-like): A N-dimensional array in belief space 
            num_pre_change_states (int): the first N elements in the belief
            array are pre-change states.
        Returns:
            [int]: 0 for continue, 1 for stop
        """

        probability_no_change = np.sum(belief[:num_pre_change_states])
        probability_of_change = 1 - probability_no_change

        if probability_of_change < self.threshold:
            action = 0
        else:
            action = 1
        return action

    @property
    def threshold(self):
        return self._deparameterise(self._free_params)

    @property
    def params(self):
        """
        Returns:
            [numpy array of float64]: The free optimisation parameters used by solvers 
        """
        return self._free_params

    @params.setter
    def params(self, var):
        if isinstance(var, int) or isinstance(var, float):
            params = np.array([var], dtype=np.float64)
        else:
            params = np.array(var, dtype=np.float64)
        self._free_params = params

    @staticmethod
    def _reparameterise(decision_parameters):
        free_params = logit(decision_parameters)
        return np.array([free_params], dtype=np.float64)

    @staticmethod
    def _deparameterise(free_params):
        """Converts the free parameters to a decision parameter

        Args:
            free_params (array of numpy.float64): A free optimisation parameter

        Returns:
            [float]: Decision threshold
        """

        decision_threshold = expit(free_params)[0]
        return decision_threshold


class ChangeIsolator(Policy):
    def __init__(self, mock=[2, 7, 3]):
        self.data = mock

    def __repr__(self):
        return "ChangeIsolator"

    def __iter__(self):
        yield ("type", self.__repr__())
        yield ("mock", self.data)

    def __call__(self):
        # TODO
        return 0


class Dynamics(Module):
    # TODO COMMON METHODS

    @property
    def transition_matrix(self):
        raise NotImplementedError


class MarkovChain(Dynamics):
    def __init__(self, mockdata=[3, 5, 6]):
        self.data = mockdata

    def __repr__(self):
        return "MarkovChain"

    def __iter__(self):
        yield ("type", self.__repr__())
        yield ("mock", self.data)

    @property
    def transition_matrix(self):
        pass


class AugmentedHMM(Dynamics):
    def __init__(
        self,
        change_matrix=None,
        geometric_prior_matrix=None,
        pre_change_matrix=None,
        post_change_matrix=None,
    ):

        self._change_matrix = (
            np.array(change_matrix)
            if change_matrix is not None
            else np.array([[0.99, 0.01], [0.01, 0.99]], dtype=np.float64)
        )
        self._geometric_prior_matrix = (
            np.array(geometric_prior_matrix)
            if geometric_prior_matrix is not None
            else np.array([[0.99, 0.01], [0.01, 0.99]], dtype=np.float64)
        )
        self._pre_change_matrix = (
            np.array(pre_change_matrix)
            if pre_change_matrix is not None
            else np.array([[0.99, 0.01], [0.01, 0.99]], dtype=np.float64)
        )
        self._post_change_matrix = (
            np.array(post_change_matrix)
            if post_change_matrix is not None
            else np.array([[0.99, 0.01], [0.01, 0.99]], dtype=np.float64)
        )
        self._transition_matrix = self._get_transition_matrix(
            self._change_matrix,
            self._geometric_prior_matrix,
            self._pre_change_matrix,
            self._post_change_matrix,
        )

        self._transition_distributions = []

        state_space = tuple(range(self._transition_matrix.shape[0]))

        for row in self._transition_matrix:
            row_norm = row / np.sum(row)
            self._transition_distributions.append(
                rv_discrete(
                    name="initial_distribution", values=(state_space, tuple(row_norm)),
                )
            )

    def __repr__(self):
        return "AugmentedHMM"

    def __iter__(self):
        yield ("type", self.__repr__())
        yield ("change_matrix", self._change_matrix.tolist())
        yield ("geometric_prior_matrix", self._geometric_prior_matrix.tolist())
        yield ("pre_change_matrix", self._pre_change_matrix.tolist())
        yield ("post_change_matrix", self._post_change_matrix.tolist())

    def __call__(self, old_state):
        return self._transition_distributions[old_state].rvs()

    @property
    def transition_matrix(self):
        return self._transition_matrix

    @staticmethod
    def _get_transition_matrix(
        change_matrix, geometric_prior_matrix, pre_change_matrix, post_change_matrix,
    ):

        dim = pre_change_matrix.shape[0] + post_change_matrix.shape[0]
        matrix = np.zeros((dim, dim), dtype=np.float64)

        matrix[: pre_change_matrix.shape[0], : pre_change_matrix.shape[1]] = (
            geometric_prior_matrix[0, 0] * pre_change_matrix
        )

        matrix[: change_matrix.shape[0], pre_change_matrix.shape[1] :] = (
            geometric_prior_matrix[0, 1] * change_matrix
        )

        matrix[pre_change_matrix.shape[0] :, pre_change_matrix.shape[1] :] = (
            geometric_prior_matrix[1, 1] * post_change_matrix
        )

        # TODO ADD CASE WHERE CHANGE CAN SWITCH OFF

        return matrix


class _StoppingProblem(ModuleFactory, FilterMixin):
    modules = {"change_process": ChangeProcess, "dynamics": Dynamics, "policy": Policy}

    def __init__(self, dynamics={}, policy={}, change_process={}):

        self._changeProcess = self._get_module(ChangeProcess, **change_process)
        self._dynamics = self._get_module(Dynamics, **dynamics)
        self._policy = self._get_module(Policy, **policy)

    def __iter__(self):
        yield ("change_process", dict(self._changeProcess))
        yield ("dynamics", dict(self._dynamics))
        yield ("policy", dict(self._policy))

    def run(self):

        filt_hist = np.zeros(
            (self._changeProcess.max_duration, self._changeProcess.num_states),
            dtype=np.float64,
        )
        obs_hist = np.zeros(self._changeProcess.max_duration, dtype=np.float64)

        # TODO INIT MEASUREMENT HISTORY
        self._changeProcess.reset()

        cost = 0
        k = 0

        # Get an initial belief
        belief = self._changeProcess.initial_belief

        while cost == 0 and k < self._changeProcess.max_duration:

            observation = self._changeProcess.observe()
            obs_hist[k] = observation

            belief = self._filter(
                observation,
                belief,
                self._dynamics.transition_matrix,
                self._changeProcess.observation_pdfs,
            )

            filt_hist[k, :] = belief

            action = self._policy(belief, self._changeProcess._num_pre_change_states)
            cost = self._changeProcess(action, self._dynamics)
            k = k + 1

        state_history = self._changeProcess.state_history


        filt_hist = filt_hist[:k, :]
        obs_hist = obs_hist[:k]
        state_history = state_history[:k]

        state_space = list(range(self._changeProcess.num_states))

        result = {
            "cost": cost,
            "filter_history": filt_hist,
            "observation_history": obs_hist,
            "state_history": state_history,
            "pre_change_states": state_space[:self._changeProcess.num_pre_change_states],
            "post_change_states": state_space[self._changeProcess.num_pre_change_states:]
        }

        if self._changeProcess.change_point:
            result["change_point"] = self._changeProcess.change_point

        return result

    def optimise(self):
        pass
