import numpy as np
import pandas as pd
from scipy.sparse.csgraph import minimum_spanning_tree

from .sparse import (filter_from_coo_matrix, join_vertex_information,
                     sparse_matrix_to_igraph)


def compute_mst_with_lens(detail, lens_params):
    # Discretise the lens values
    lens_binned, detail['lens_bins'] = pd.cut(pd.Series(lens_params['values']),
                                              bins = lens_params['bins'],
                                              labels = np.arange(0, lens_params[
                                                  'bins'], 1), retbins = True)
    # Remove empty bins s.t. adjacent edges can cross them
    lens_binned = lens_binned.cat.remove_unused_categories()
    lens_binned.cat.categories = np.arange(0, len(lens_binned.cat.categories))

    # Adds 'adjacent_edges', 'non_adjacent_edges', and removes non-adjacent
    # edges from 'adjacent_edges' and 'normalised_distances'
    classify_edges_lens(detail, lens_binned, lens_params)

    # Compute Stage 1 MST
    mst_distances = detail['normalised_distances'].copy()
    mst_distances.data[detail['adjacent_edges'].data] += 1
    # csr format 
    detail['lens_initial_mst'] = minimum_spanning_tree(mst_distances)

    # Adds 'in_community_edges' and 'community_membership'
    classify_edges_community(detail, lens_params)

    # Update distances s.t. between community and between bin edges have 
    # the same weight.
    mst_distances.data[~detail['in_community_edges'].data & ~detail[
        'adjacent_edges'].data] += 1

    # Final MST
    detail['mst'] = minimum_spanning_tree(mst_distances)  # csr format


def classify_edges_lens(detail, lens_binned, lens_params):
    # Classify edges as: within bin, to adjacent bin, to non-adjacent bin
    # No non-adjacent edges are allowed in the output network
    (from_lens_bin, to_lens_bin) = join_vertex_information(
        detail['normalised_distances'], lens_binned)
    within_edge = detail['normalised_distances'].copy()
    within_edge.data = from_lens_bin.data == to_lens_bin.data

    detail['adjacent_edges'] = within_edge.copy()
    detail['adjacent_edges'].data = ((
                                             from_lens_bin.data + 1) ==
                                     to_lens_bin.data) | (
                                            from_lens_bin.data == (
                                            to_lens_bin.data + 1))

    # Also account for the outer bins when the lens is circular
    if lens_params['circular']:
        min_bin = 0
        max_bin = max(lens_binned.cat.categories)
        detail['adjacent_edges'].data = \
            detail['adjacent_edges'].data | (
                (from_lens_bin.data == min_bin) &
                (to_lens_bin.data == max_bin) | (
                    from_lens_bin.data == max_bin
                ) & (
                    to_lens_bin.data == min_bin
                )
            )

    detail['non_adjacent_edges'] = within_edge.copy()
    detail['non_adjacent_edges'].data = ~(
            within_edge.data | detail['adjacent_edges'].data
    )

    # Remove non-adjacent edges
    edge_mask = ~detail['non_adjacent_edges'].data
    detail['normalised_distances'] = filter_from_coo_matrix(
        detail['normalised_distances'],
        edge_mask
    )
    detail['adjacent_edges'] = filter_from_coo_matrix(
        detail['adjacent_edges'],
        edge_mask
    )


def classify_edges_community(detail, lens_params):
    # Classify edge community
    detail['community_membership'] = find_communities(
        detail['lens_initial_mst'],
        lens_params
    )
    (from_membership, to_membership) = join_vertex_information(
        detail['normalised_distances'],
        detail['community_membership']
    )
    detail['in_community_edges'] = detail['normalised_distances'].copy()
    detail['in_community_edges'].data = \
        from_membership.data == to_membership.data


def find_communities(mst_network, lens_params):
    g = sparse_matrix_to_igraph(mst_network)
    if lens_params['use_weights']:
        communities = g.community_walktrap(weights = 1 / (1 + mst_network.data),
                                           steps = lens_params['walk_length'])
    else:
        communities = g.community_walktrap(steps = lens_params['walk_length'])

    return communities.as_clustering().membership
