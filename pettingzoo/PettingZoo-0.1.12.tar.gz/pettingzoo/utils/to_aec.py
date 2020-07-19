from .env import AECEnv
from pettingzoo.utils import agent_selector

class MarkovToAECWrapper:
    def __init__(self, markov_env):
        self.env = markov_env
        self.agents = markov_env.agents
        assert len(self.agents) == len()


    def reset(self, observe=True):
        self._actions = []

        agent_indicies = list(range(len(self.agents)))
        self._agent_idx_selector = agent_selector(agent_indicies)
        self.dones = {agent:done for agent,done in zip(self.agents,self.env.dones)}
        self.infos = {agent:info for agent,info in zip(self.agents,self.env.infos)}
        self.rewards = {agent:reward for agent,reward in zip(self.agents,self.env.rewards)}

        self._observations = self.env.reset()

        agent_idx = self._agent_idx_selector.reset()

        return self._observations[agent_idx]

    def step(self, action):
