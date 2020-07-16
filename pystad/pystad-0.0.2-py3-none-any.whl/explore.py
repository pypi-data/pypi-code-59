from enum import Enum

import numpy as np


class StadExploration(Enum):
    EDGES_LINEAR = 0
    EDGES_LOGARITHMIC = 1
    DISTANCES_LINEAR = 2
    DISTANCES_LOGARITHMIC = 3
    OPTIMISER = 4


def compute_stad_evaluation_points(detail, explore_params):
    switch_dict = {
        StadExploration.EDGES_LINEAR: edges_exploration_linear,
        StadExploration.EDGES_LOGARITHMIC: edges_exploration_logarithmic,
        StadExploration.DISTANCES_LINEAR: distance_exploration_linear,
        StadExploration.DISTANCES_LOGARITHMIC: distance_exploration_logarithmic
    }
    switch_dict[explore_params['strategy']](detail, explore_params)


def edges_exploration_linear(detail, explore_params):
    num_edges = len(detail['non_mst_distances'].data)
    edge_thresholds = np.linspace(explore_params['min_factor'] * num_edges,
                                  explore_params['max_factor'] * num_edges,
                                  explore_params['iterations'])
    edge_thresholds = np.unique(edge_thresholds.round()).astype('int')
    sorted_distances = np.sort(detail['non_mst_distances'].data)
    detail['distance_thresholds'] = sorted_distances[edge_thresholds]


def edges_exploration_logarithmic(detail, explore_params):
    num_edges = len(detail['non_mst_distances'].data)
    exponents = np.linspace(np.log10(explore_params['min_factor'] * num_edges),
                            np.log10(explore_params['max_factor'] * num_edges),
                            explore_params['iterations'])
    edge_thresholds = np.unique(np.power(10, exponents).round()).astype('int')
    sorted_distances = np.sort(detail['non_mst_distances'].data)
    detail['distance_thresholds'] = sorted_distances[edge_thresholds]


def distance_exploration_linear(detail, explore_params):
    distance_thresholds = np.linspace(explore_params['min_factor'],
                                      explore_params['max_factor'],
                                      explore_params['iterations'])
    detail['distance_thresholds'] = distance_thresholds


def distance_exploration_logarithmic(detail, explore_params):
    exponents = np.linspace(np.log10(explore_params['min_factor']),
                            np.log10(explore_params['max_factor']),
                            explore_params['iterations'])
    detail['distance_thresholds'] = np.power(10, exponents)
