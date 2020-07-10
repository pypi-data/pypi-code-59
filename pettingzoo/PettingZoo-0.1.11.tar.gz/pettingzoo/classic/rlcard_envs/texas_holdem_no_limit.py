from pettingzoo import AECEnv
from pettingzoo.utils.agent_selector import agent_selector
from gym import spaces
import rlcard
import random
from rlcard.utils.utils import print_card
import numpy as np
from pettingzoo.utils import wrappers
from .rlcard_base import RLCardBase


def env(**kwargs):
    env = raw_env(**kwargs)
    env = wrappers.TerminateIllegalWrapper(env, illegal_reward=-1)
    env = wrappers.AssertOutOfBoundsWrapper(env)
    pass_action = 2
    env = wrappers.NanNoOpWrapper(env, pass_action, "'checked' with action {}".format(pass_action))
    env = wrappers.OrderEnforcingWrapper(env)
    return env


class raw_env(RLCardBase):

    metadata = {'render.modes': ['human']}

    def __init__(self, seed=None):
        super().__init__("no-limit-holdem", 2, (54,), seed)
        self.observation_spaces = self._convert_to_dict([spaces.Box(low=np.zeros(54,), high=np.append(np.ones(52,), [100, 100]), dtype=np.float32) for _ in range(self.num_agents)])

    def render(self, mode='human'):
        for player in self.agents:
            state = self.env.game.get_state(self._name_to_int(player))
            print("\n=============== {}'s Hand ===============".format(player))
            print_card(state['hand'])
            print("\n{}'s Chips: {}".format(player, state['my_chips']))
        print('\n================= Public Cards =================')
        print_card(state['public_cards']) if state['public_cards'] else print('No public cards.')
        print('\n')
