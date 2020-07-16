from stad import stad, StadExploration
from sklearn.metrics.pairwise import euclidean_distances
from scipy.sparse import isspmatrix, triu
from scipy.optimize import shgo
import numpy as np
import pandas as pd
import pytest

data = pd.read_csv('./examples/data/horse.csv')
idx = np.random.choice(data.shape[0], 200, replace=False)
data = data.iloc[idx, :]
dist = euclidean_distances(data)


def check_array(array, length, relaxed = False):
    assert isinstance(array, list)
    if relaxed:
        assert len(array) >= length
    else:
        assert len(array) == length


def check_no_lens_detail(detail, explore_steps, relaxed = False):
    assert isspmatrix(detail['normalised_distances'])
    assert isspmatrix(detail['mst'])
    assert isspmatrix(detail['non_mst_distances'])

    check_array(detail['distance_thresholds'], explore_steps, relaxed)
    check_array(detail['correlations'], explore_steps, relaxed)
    check_array(detail['penalised_correlations'], explore_steps, relaxed)
    check_array(detail['added_edges'], explore_steps, relaxed)

    assert detail['best_penalised_correlation'] == \
        np.max(detail['penalised_correlations'])
    idx = np.argmax(detail['penalised_correlations'])
    assert detail['best_correlation'] == \
        detail['correlations'][idx]
    assert detail['best_distance_threshold'] == \
        detail['distance_thresholds'][idx]
    assert detail['num_edges_added'] == \
        detail['added_edges'][idx]


def check_lens_detail(detail, relaxed = False):
    assert isspmatrix(detail['lens_initial_mst'])
    assert isspmatrix(detail['adjacent_edges'])
    assert isspmatrix(detail['non_adjacent_edges'])
    assert isspmatrix(detail['in_community_edges'])
    check_array(detail['community_membership'],
                detail['non_adjacent_edges'].shape[0],
                relaxed)


class TestStad:
    def test_no_lens_output(self):
        explore_steps = 10
        (stad_graph, detail) = stad(
            triu(dist, k = 1), 
            explore_steps = explore_steps
        )
        assert isspmatrix(stad_graph)
        check_no_lens_detail(detail, explore_steps)

    def test_lens_output(self):
        explore_steps = 10
        n_bins = 3
        (stad_graph, detail) = stad(
            triu(dist, k = 1), 
            explore_steps = explore_steps,
            lens_values = data['x'],
            lens_bins = n_bins
        )
        assert isspmatrix(stad_graph)
        check_no_lens_detail(detail, explore_steps)
        check_lens_detail(detail)

    def test_reject_dense_input(self):
        with pytest.raises(Exception) as e_info:
            stad(dist)

    def test_reject_lens_without_bins(self):
        with pytest.raises(Exception) as e_info:
            stad(
                triu(dist, k = 1),
                lens_values = data['x']
            )

    def test_accept_bins_without_lens(self):
        stad(triu(dist, k = 1), lens_bins = 3)

    def test_reject_wrong_lens_size(self):
        with pytest.raises(Exception) as e_info:
            stad(
                triu(dist, k = 1),
                lens_values = data['x'][0:10],
                lens_bins = 3
            )

    def test_wrong_strategy_input(self):
        with pytest.raises(Exception) as e_info:
            stad(
                triu(dist, k = 1),
                explore_strategy = "some thing weird"
            )
    
    def test_linear_edge_exploration(self):
        explore_steps = 10
        (stad_graph, detail) = stad(
            triu(dist, k = 1), 
            explore_strategy = StadExploration.EDGES_LINEAR,
            explore_steps = explore_steps
        )
        assert isspmatrix(stad_graph)
        check_no_lens_detail(detail, explore_steps)

    def test_logarithmic_edge_exploration(self):
        explore_steps = 10
        (stad_graph, detail) = stad(
            triu(dist, k = 1), 
            explore_strategy = StadExploration.EDGES_LOGARITHMIC,
            explore_steps = explore_steps
        )
        assert isspmatrix(stad_graph)
        check_no_lens_detail(detail, explore_steps)

    def test_linear_distance_exploration(self):
        explore_steps = 10
        (stad_graph, detail) = stad(
            triu(dist, k = 1), 
            explore_strategy = StadExploration.DISTANCES_LINEAR,
            explore_steps = explore_steps
        )
        assert isspmatrix(stad_graph)
        check_no_lens_detail(detail, explore_steps)

    def test_logarithmic_distance_exploration(self):
        explore_steps = 10
        (stad_graph, detail) = stad(
            triu(dist, k = 1), 
            explore_strategy = StadExploration.DISTANCES_LOGARITHMIC,
            explore_steps = explore_steps
        )
        assert isspmatrix(stad_graph)
        check_no_lens_detail(detail, explore_steps)

    def test_linear_edge_exploration_lens(self):
        explore_steps = 10
        (stad_graph, detail) = stad(
            triu(dist, k = 1), 
            lens_values = data.x,
            lens_bins = 3,
            explore_strategy = StadExploration.EDGES_LINEAR,
            explore_steps = explore_steps
        )
        assert isspmatrix(stad_graph)
        check_no_lens_detail(detail, explore_steps)
        check_lens_detail(detail)

    def test_logarithmic_edge_exploration_lens(self):
        explore_steps = 10
        (stad_graph, detail) = stad(
            triu(dist, k = 1),
            lens_values = data.x,
            lens_bins = 3,
            explore_strategy = StadExploration.EDGES_LOGARITHMIC,
            explore_steps = explore_steps
        )
        assert isspmatrix(stad_graph)
        check_no_lens_detail(detail, explore_steps)
        check_lens_detail(detail)

    def test_linear_distance_exploration_lens(self):
        explore_steps = 10
        (stad_graph, detail) = stad(
            triu(dist, k = 1), 
            lens_values = data.x,
            lens_bins = 3,
            explore_strategy = StadExploration.DISTANCES_LINEAR,
            explore_steps = explore_steps
        )
        assert isspmatrix(stad_graph)
        check_no_lens_detail(detail, explore_steps)
        check_lens_detail(detail)

    def test_logarithmic_distance_exploration_lens(self):
        explore_steps = 10
        (stad_graph, detail) = stad(
            triu(dist, k = 1), 
            lens_values = data.x,
            lens_bins = 3,
            explore_strategy = StadExploration.DISTANCES_LOGARITHMIC,
            explore_steps = explore_steps
        )
        assert isspmatrix(stad_graph)
        check_no_lens_detail(detail, explore_steps)
        check_lens_detail(detail)

    def test_optimiser(self):
        explore_steps = 100
        (stad_graph, detail) = stad(
            triu(dist, k = 1),
            explore_strategy = StadExploration.OPTIMISER,
            explore_optimiser_kwargs = {
                'initial_temp': 100,
                'no_local_search': True
            },
            explore_edge_penalty = 0.1,
            explore_steps = explore_steps
        )

        assert isspmatrix(stad_graph)
        check_no_lens_detail(detail, explore_steps, relaxed = True)
    
    def test_optimiser_lens(self):
        explore_steps = 100
        (stad_graph, detail) = stad(
            triu(dist, k = 1), 
            lens_values = data.x,
            lens_bins = 3,
            explore_strategy = StadExploration.OPTIMISER,
            explore_optimiser_kwargs = {
                'initial_temp': 100,
                'no_local_search': True
            },
            explore_steps = explore_steps
        )
        assert isspmatrix(stad_graph)
        check_no_lens_detail(detail, explore_steps, relaxed = True)
        check_lens_detail(detail, relaxed = True)

    def test_custom_optimiser(self):
        def custom_optimiser(fun, args, bounds, maxiter, **kwargs):
            shgo(fun, bounds, args=args, options={
                    'maxiter': maxiter,
                    **kwargs
                }
            )
        
        explore_steps = 10
        (stad_graph, detail) = stad(
            triu(dist, k = 1), 
            explore_strategy = StadExploration.OPTIMISER,
            explore_steps = explore_steps,
            explore_optimiser = custom_optimiser,
            explore_optimiser_kwargs = {
                'n': 4
            }
        )
        assert isspmatrix(stad_graph)
        check_no_lens_detail(detail, explore_steps, relaxed = True)