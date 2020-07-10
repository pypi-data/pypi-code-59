from pettingzoo import AECEnv
from pettingzoo.utils.agent_selector import agent_selector
from gym import spaces
import random
import rlcard
from rlcard.utils.utils import print_card
from rlcard.games.gin_rummy.player import GinRummyPlayer
from rlcard.games.gin_rummy.utils import utils
from rlcard.games.gin_rummy.utils.action_event import KnockAction, GinAction
import rlcard.games.gin_rummy.utils.melding as melding
import numpy as np
from pettingzoo.utils import wrappers
from .rlcard_base import RLCardBase


def env(**kwargs):
    env = raw_env(**kwargs)
    env = wrappers.TerminateIllegalWrapper(env, illegal_reward=-1)
    env = wrappers.AssertOutOfBoundsWrapper(env)
    env = wrappers.NaNRandomWrapper(env)
    env = wrappers.OrderEnforcingWrapper(env)
    return env


class raw_env(RLCardBase):

    metadata = {'render.modes': ['human']}

    def __init__(self, seed=None, knock_reward: float = 0.5, gin_reward: float = 1.0):
        super().__init__("gin-rummy", 2, (5, 52), seed)
        self._knock_reward = knock_reward
        self._gin_reward = gin_reward

        self.env.game.judge.scorer.get_payoff = self._get_payoff

    def _get_payoff(self, player: GinRummyPlayer, game) -> float:
        going_out_action = game.round.going_out_action
        going_out_player_id = game.round.going_out_player_id
        if going_out_player_id == player.player_id and type(going_out_action) is KnockAction:
            payoff = self._knock_reward
        elif going_out_player_id == player.player_id and type(going_out_action) is GinAction:
            payoff = self._gin_reward
        else:
            hand = player.hand
            best_meld_clusters = melding.get_best_meld_clusters(hand=hand)
            best_meld_cluster = [] if not best_meld_clusters else best_meld_clusters[0]
            deadwood_count = utils.get_deadwood_count(hand, best_meld_cluster)
            payoff = -deadwood_count / 100
        return payoff

    def render(self, mode='human'):
        for player in self.agents:
            state = self.env.game.round.players[self._name_to_int(player)].hand
            print("\n===== {}'s Hand =====".format(player))
            print_card([c.__str__()[::-1] for c in state])
        state = self.env.game.get_state(0)
        print("\n==== Top Discarded Card ====")
        print_card([c.__str__() for c in state['top_discard']] if state else None)
        print('\n')
