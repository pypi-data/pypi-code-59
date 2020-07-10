from .base_atari_env import BaseAtariEnv, base_env_wrapper_fn


def raw_env(**kwargs):
    return BaseAtariEnv(game="double_dunk", num_players=2, mode_num=None, **kwargs)


env = base_env_wrapper_fn(raw_env)
