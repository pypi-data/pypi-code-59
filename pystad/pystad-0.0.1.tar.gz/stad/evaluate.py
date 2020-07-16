import numpy as np
from scipy.sparse import triu
from scipy.sparse.csgraph import shortest_path

from .explore import StadExploration


def find_best_number_of_edges(detail, explore_params):
    # Evaluate the distance thresholds. Adds 'correlations' to detail
    evaluate_correlations(detail, explore_params)

    # Extract the best values
    best_idx = np.argmax(detail['penalised_correlations'])
    detail['best_correlation'] = detail['correlations'][best_idx]
    detail['best_penalised_correlation'] = detail['penalised_correlations'][
        best_idx]
    detail['best_distance_threshold'] = detail['distance_thresholds'][best_idx]

    # Re-compute best STAD network
    stad_graph, detail['num_edges_added'] = add_edges_to_stad(
        detail['mst'].copy().tolil(), detail['best_distance_threshold'],
        detail['non_mst_distances'])
    return stad_graph.tocoo()


def evaluate_correlations(detail, explore_params):
    # pre-allocate output values
    detail['correlations'] = []
    detail['penalised_correlations'] = []
    detail['added_edges'] = []
    stad_graph = detail['mst'].copy().tolil()

    if explore_params['strategy'] == StadExploration.OPTIMISER:
        detail['distance_thresholds'] = []
        run_optimiser(stad_graph, detail, explore_params)
    else:
        run_sweep(stad_graph, detail, explore_params)

    # nan values occur when a graph is fully connected
    mask = np.nonzero(np.isnan(detail['correlations']))[0]
    if len(mask) > 0:
        detail['correlations'][mask] = 0
        detail['penalised_correlations'][mask] = 0


def run_optimiser(stad_graph, detail, explore_params):
    """ Run optimiser

    Runs the given scipy.optimize function. Results are appended to detail
    """

    # The optimisation function
    explore_params['optimiser'](
        # The evaluation function
        evaluate_correlation_at,
        # Fixed parameters for evaluate_correlation_at
        args = (stad_graph, detail, explore_params),
        # Bounds provided by explore params
        bounds = [(explore_params['min_factor'], explore_params['max_factor'])],
        maxiter = explore_params['iterations'],
        # Additional arugments
        **explore_params['kwargs']
    )


def run_sweep(stad_graph, detail, explore_params):
    """ Run sweep

    Performs a linear or logarithmic sweep. Results are appended to detail
    """
    thresholds = detail['distance_thresholds']
    detail['distance_thresholds'] = []

    for distance_limit in thresholds:
        evaluate_correlation_at(
            distance_limit,
            stad_graph,
            detail,
            explore_params
        )


def evaluate_correlation_at(distance_limit, graph, detail, explore_params):
    """ Determines quality of network at given distance threshold

    Computes the (penalised) correlation at the given distance limit, for use
    with SciPy optimisers. Also updates bookkeeping in detail.
    """

    # Avoid influence from previous iterations
    graph, added_edges = add_edges_to_stad(
        graph.copy(),
        distance_limit,
        detail['non_mst_distances']
    )

    graph_distance = triu(
        shortest_path(graph, directed = False, unweighted = True),
        k = 1
    )

    correlation = np.corrcoef(
        graph_distance.data[~detail['non_adjacent_edges'].data],
        detail['normalised_distances'].data
    )[0, 1]
    penalised_correlation = (
        correlation - explore_params['penalty'] * (
            added_edges / len(detail['non_mst_distances'].data)
        )
    )

    # Keep track of the iteration
    detail['distance_thresholds'].append(distance_limit)
    detail['added_edges'].append(added_edges)
    detail['correlations'].append(correlation)
    detail['penalised_correlations'].append(penalised_correlation)

    # SciPy optimisers minimise, so return the negative correlation
    return -penalised_correlation


def add_edges_to_stad(graph, distance_limit, non_mst_distances):
    edge_mask = non_mst_distances.data <= distance_limit
    graph[non_mst_distances.row[edge_mask], non_mst_distances.col[
        edge_mask]] = True
    return graph, edge_mask.sum()
