import copy
import multiprocessing as mp
from gym.vector.utils import shared_memory
from pettingzoo.utils.agent_selector import agent_selector
import numpy as np
import ctypes
import gym

def spaces_are_homogenous(spaces):
    first_space = spaces[0]
    return [str(first_space) == str(space) for space in spaces]

class VectorMarovWrapper:
    def __init__(self, markov_env_constructor, num_envs, seed=None):
        assert num_envs >= 1
        assert callable(markov_env_constructor), "env_constructor must be a callable object (i.e function) that create an environment"

        self.envs = [(markov_env_constructor(seed=seed+i) if seed is not None else env_constructor()) for i in range(num_envs)]
        self.num_envs = num_envs
        self.env = self.envs[0]

        assert spaces_are_homogenous(list(self.env.observation_spaces.values())), "VectorMarovWrapper only accepts homogenous markov games, put the environment through the pad_observations wrapper to homogenize this environment"
        assert spaces_are_homogenous(list(self.env.action_spaces.values())), "VectorMarovWrapper only accepts homogenous markov games, put the environment through the pad_observations wrapper to homogenize this environment"

        self.num_agents = self.env.num_agents
        self.obs_size = self.num_envs*len(self.env.agents)
        self.agents = self.env.agents
        self.observation_space = self.env.observation_spaces[0]
        self.action_space = copy.copy(self.env.action_spaces)
        self._agent_selector = agent_selector(self.agents)

    def _find_active_agent(self):
        cur_selection = self.agent_selection
        while not any(cur_selection == env.agent_selection for env in self.envs):
            cur_selection = self._agent_selector.next()
        return cur_selection

    def reset(self, observe=True):
        '''
        returns: list of observations
        '''
        observations = []
        for env in self.envs:
            observations.append(env.reset(observe))

        self.rewards = {agent: [env.rewards[agent] for env in self.envs] for agent in self.agents}
        self.dones = {agent: [env.dones[agent] for env in self.envs] for agent in self.agents}
        self.env_dones = [all(env.dones.values()) for env in self.envs]
        self.infos = {agent: [env.infos[agent] for env in self.envs] for agent in self.agents}
        self.agent_selection = self._agent_selector.reset()
        self.agent_selection = self._find_active_agent()

        passes = [env.agent_selection != self.agent_selection for env in self.envs]

        return (observations if observe else None),passes

    def observe(self, agent):
        observations = []
        for env in self.envs:
            observations.append(env.observe(agent))
        return observations

    def last(self):
        last_agent = self.agent_selection
        return self.rewards[last_agent], self.dones[last_agent], self.infos[last_agent]

    def step(self, actions, observe=True):
        assert len(actions) == len(self.envs)
        old_agent = self.agent_selection

        observations = []
        for act,env in zip(actions,self.envs):
            observations.append(env.step(act,observe) if env.agent_selection == old_agent else env.observe(env.agent_selection))

        self.agent_selection = self._agent_selector.next()
        self.agent_selection = self._find_active_agent()
        new_agent = self.agent_selection


        self.rewards = {agent: [env.rewards[agent] for env in self.envs] for agent in self.agents}
        self.dones = {agent: [env.dones[agent] for env in self.envs] for agent in self.agents}
        self.infos = {agent: [env.infos[agent] for env in self.envs] for agent in self.agents}
        # self._agent_selections = [env.agent_selection for env in self.envs]
        # self.agent_selection = self._agent_selections[0]
        env_dones = [all(env.dones.values()) for env in self.envs]
        for i,(env,done) in enumerate(zip(self.envs,env_dones)):
            if done:
                observations[i] = env.reset(observe)

        passes = [env.agent_selection != self.agent_selection for env in self.envs]

        return (observations if observe else None),passes,env_dones
