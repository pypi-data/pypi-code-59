from logic.settings import N_ROUND_METRICS

def trunc(x):
    return float('%.{}f'.format(N_ROUND_METRICS)%(x))