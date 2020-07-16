import numpy as np
from scipy.sparse import isspmatrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.optimize import dual_annealing

from .evaluate import find_best_number_of_edges
from .explore import StadExploration, compute_stad_evaluation_points
from .lens_1D import compute_mst_with_lens
from .sparse import filter_from_coo_matrix, sparse_is_in


def stad(distance_matrix,
         explore_strategy = StadExploration.EDGES_LOGARITHMIC,
         explore_optimiser = dual_annealing,
         explore_optimiser_kwargs = None,
         explore_steps = 10,
         explore_min_value = 0.01,
         explore_max_value = 0.5,
         explore_edge_penalty = 0,
         lens_values = None,
         lens_bins = None,
         lens_is_circular = False,
         lens_community_weights = False,
         lens_community_walk = 4):
    """ STAD (Simplified Topological Approximation of Data)

    This function computes a STAD network. A STAD network describes the global
    topology of a point-cloud. The algorithm computes a minimum spanning tree 
    and adds edges (ordered by distance) until the correlation between the 
    graph distance and original distance is at its maximum. To find the maximum
    correlation, several exploration strategies are available (see parameters).

    STAD is able to apply a lens or filter to explore different dimensions of
    the data. Using a lens, points that differ in that dimension are separated
    in the network.

    The algorithm is implemented using SciPy Sparse matrices.

    Parameters
    ----------
    distance_matrix : SciPy Sparse Matrix
        The distance matrix of the point-cloud. This matrix should only 
        contain the upper triangle of the complete matrix.
    explore_strategy : StadExploration
        An enum to select an exploration strategy. The algorithm searches for
        the number of edges that maximises the correlation of the graph 
        distance and the original distances. This search is a linear or 
        logarithmic sweep, either in terms of edges or in the (normalised) 
        distance of edges. In addition, one can use the OPTIMISER value. Then
        an SciPy.optimize function is used to find the optimal network.
    explore_optimiser : function
        A SciPy.optimize function, to use when the OPTIMISER strategy is chosen.
        The default value is: scipy.optimize.dual_annealing.
    explore_optimiser_kwargs : dictionary
        Additional keyword arguments for the optimisation function. Only used
        when the OPTIMISER strategy is chosen.
    explore_steps : int
        The number of networks to explore, when searching for the maximum 
        correlated network.
    explore_min_value : numeric
        The minimum exploration value as a factor of the maximum normalised 
        distance (1) or maximum number of edges that can be added to the mst.
    explore_max_value : numeric
        The maximum exploration value as a factor of the maximum normalised 
        distance (1) or maximum number of edges that can be added to the mst.
    explore_edge_penalty : numeric
        A 'weight decay'-like factor on the correlation. When maximising the
        correlation, it is applied as: 
            correlation - (explore_edge_penalty * (added edges / max edges))
    lens_values : Optional list, numpy.Array, pandas.Series
        The (numerical) values of the lens dimension for each vertex. When not 
        specified, STAD is evaluated without lens.
    lens_bins : int
        The number of bins used to discretise the lens dimension.
    lens_is_circular : bool
        Indicates whether the lens dimension is circular. For instance, 
        weekdays are circular.
    lens_community_weights : bool
        When a lens is applied, STAD uses the community_walktrap algorithm to 
        detect communities in the minimum spanning tree. This parameter 
        specifies whether weights are used (1 / (1 + distance)) in that 
        operation.
    lens_community_walk : int
        When a lens is applied, STAD uses the community_walktrap algorithm to 
        detect communities in the minimum spanning tree. This parameter 
        determines the length of the random walks used in that operation. When 
        not specified, the implementation's default is used (4).
    
    Returns
    -------
    stad_graph : SciPy sparse matrix
        The adjacency matrix of the STAD network in the form of a boolean SciPy
        sparse matrix.
    details : dict
        A dictionary containing internal representations, which can be used to 
        inspect the result in more detail. It includes:
            - The sparse normalised distance matrix.
            - The minimum spanning tree, used as basis for STAD.
            - A sparse matrix, indicating the non-adjacent edges.
            - The sparse normalised distance matrix, excluding mst edges.
            - The explored distance thresholds.
            - The correlation between the graph-distances and given distance-
              matrix at the distance thresholds.
            - The first-stage minimum spanning tree (only when a lens is used).
            - A sparse matrix indicating community membership (only when a lens 
              is used).
            - A sparse matrix indicating adjacent edges. (only when a lens
              is used).
            - A sparse matrix indicating within-community edges. (only when a
              lens is used).
            - The vertex community membership values. (only when a lens
              is used).
            - The positions of the lens intervals. (only when a lens
              is used).
            - The distance threshold with the highest correlation.
            - The highest correlation value.
            - The number of added edges of the output network.
    """
    # Some parameter checks
    validate_inputs(distance_matrix, explore_strategy, lens_values, lens_bins)
    (lens_params, explore_params) = group_parameters(
        lens_values,
        lens_bins,
        lens_is_circular,
        lens_community_weights,
        lens_community_walk,
        explore_strategy,
        explore_optimiser,
        explore_optimiser_kwargs,
        explore_steps,
        explore_min_value,
        explore_max_value,
        explore_edge_penalty
    )

    # Normalise the distance matrix, so that the correlation lies between 0 
    # and 1, and we can control the minimum spanning tree with a lens.
    distance_matrix = distance_matrix.copy().tocoo()
    distance_matrix.data = distance_matrix.data / distance_matrix.data.max()

    # We wil use a dictionary to keep track of internal representations.
    detail = {
        'normalised_distances': distance_matrix
    }

    # Adds 'mst' and 'non_adjacent_edges' and 'non_mst_distances' to detail.
    # When a lens is used, all non-adjacent edges are removed from 
    # 'normalised_distances'.
    compute_minimum_spanning_tree(detail, lens_params)

    # STAD maximises the correlation of the graph distance with the given
    # data-matrix, by adding all edges below a (normalised) distance threshold.
    # Here, we determine which distances are used as thresholds.
    # The optimiser strategy determines these points by itself!
    if explore_params['strategy'] != StadExploration.OPTIMISER:
        compute_stad_evaluation_points(detail, explore_params)

    # Maximise graph distance correlation
    stad_network = find_best_number_of_edges(detail, explore_params)
    return stad_network, detail


def validate_inputs(distance_matrix, explore_strategy, lens_values, lens_bins):
    assert isspmatrix(distance_matrix)
    assert isinstance(explore_strategy, StadExploration)
    # Require a lens_value for every vertex when not None
    assert (lens_values is None) or (
            len(lens_values) == distance_matrix.shape[0]
    )
    # Require a value for lens_bins when lens_values is given
    assert (lens_values is None) or not (lens_bins is None)


def group_parameters(lens_values, lens_bins, lens_is_circular,
                     lens_community_weights, lens_community_walk,
                     explore_strategy, explore_optimiser,
                     explore_optimiser_kwargs, explore_steps, explore_min_value,
                     explore_max_value, explore_edge_penalty):
    lens_params = {
        'values': lens_values,
        'bins': lens_bins,
        'circular': lens_is_circular,
        'use_weights': lens_community_weights,
        'walk_length': lens_community_walk
    }
    explore_params = {
        'strategy': explore_strategy,
        'optimiser': explore_optimiser,
        'kwargs': explore_optimiser_kwargs,
        'iterations': explore_steps,
        'min_factor': explore_min_value,
        'max_factor': explore_max_value,
        'penalty': explore_edge_penalty
    }
    if explore_optimiser_kwargs is None:
        explore_params['kwargs'] = dict()
    return lens_params, explore_params


def compute_minimum_spanning_tree(detail, lens_params):
    # Compute the minimum spanning tree
    if lens_params['values'] is None:
        # mst is in csr format
        detail['mst'] = minimum_spanning_tree(detail['normalised_distances'])
        detail['non_adjacent_edges'] = detail['normalised_distances'].copy()
        detail['non_adjacent_edges'].data = np.zeros(
            len(detail['non_adjacent_edges'].data),
            dtype = bool
        )
    else:
        # Writes to detail...
        compute_mst_with_lens(detail, lens_params)

    # Filter the edge distances that were not used by the mst
    detail['mst'] = detail['mst'].tocoo()
    mst_indices = sparse_is_in(detail['normalised_distances'], detail['mst'])
    detail['non_mst_distances'] = filter_from_coo_matrix(
        detail['normalised_distances'].copy(),
        ~mst_indices
    )
