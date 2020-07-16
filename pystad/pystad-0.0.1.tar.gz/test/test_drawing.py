import stad
from scipy.sparse import triu
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np
import pandas as pd
import pytest


data = pd.read_csv('./examples/data/horse.csv')
idx = np.random.choice(data.shape[0], 200, replace=False)
data = data.iloc[idx, :]
dist = euclidean_distances(data)

(stad_graph, detail) = stad.stad(
    triu(dist, k = 1),
    explore_strategy = stad.StadExploration.OPTIMISER,
    explore_optimiser_kwargs = {
        'initial_temp': 100,
        'no_local_search': True
    },
    explore_edge_penalty = 0.1,
    explore_steps = 100
)


class TestMPLDrawing:
    def test_correlation(self):
        fig = stad.draw_correlations_matplotlib(detail)

    def test_optimiser(self):
        fig = stad.draw_optimiser_matplotlib(detail)

    def test_network(self):
        fig, nodes, edges, graph, layout = \
            stad.draw_network_matplotlib(stad_graph, detail)

    def test_vega_network(self):
        spec = stad.build_vega_spec(stad_graph, detail, data)