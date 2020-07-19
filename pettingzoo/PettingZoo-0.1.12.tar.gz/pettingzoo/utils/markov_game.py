from pettingzoo.utils import MarkovEnv
import numpy as np


class MarkovEnv(object):
    def __init__(self):
        pass

    def step(self, action):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    def render(self, mode='human'):
        raise NotImplementedError

    def close(self):
        pass

class markov_game(MarkovEnv):
    def __init__(self, AECEnv):
        super(markov_game, self).__init__()
        self.AECenv = AECEnv
        self.agents = AECEnv.agents[:]
        self.observation_spaces = [AECEnv.observation_spaces[agent] for agent in self.agents]
        self.action_spaces = [AECEnv.action_spaces[agent] for agent in self.agents]

    def agent_index(self, agent):
        return self.agents.index(agent)

    def reset(self):
        self.AECenv.reset(observe=False)
        observations = [self.AECenv.observe(agent) for agent in self.agents]
        return observations

    def render(self, mode='human'):
        self.AECenv.render(mode=mode)

    def close(self):
        self.AECenv.close()

    def step(self, actions):
        for agent_inorder in self.agents:
            env_agent = self.AECenv.agent_selection
            assert agent_inorder == env_agent, "Markov Game is wrapping an environment which has an unusual agent order, this is not allowed"
            self.AECenv.step(actions[agent], observe=False)

        observations = [self.AECEnv.observe(agent) for agent in self.agents]

        dones = [self.AECenv.dones[agent] for agent in self.agents]
        rewards = [self.AECenv.rewards[agent] for agent in self.agents]
        infos = [self.AECenv.infos[agent] for agent in self.agents]
        return self.observations, self.AECEnv.rewards, dones, self.AECEnv.infos
