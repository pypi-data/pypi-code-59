import igraph as ig
import numpy as np


def join_vertex_information(sparse_distance_matrix, vertex_values):
    """ Join vertex-data with edges

    Creates two sparse matrices, one for the 'from' vertices and one 
    for the 'to' vertices, filled with the vertex values. Analogous to
    performing two (left) joins in a tabular format. This function is f.i.
    used to find edges of which the vertices lie in different lens bins.
    """
    from_values = sparse_distance_matrix.copy()
    to_values = sparse_distance_matrix.copy()
    for vertex_idx, value in enumerate(vertex_values):
        from_values.data[np.nonzero(from_values.row == vertex_idx)] = value
        to_values.data[np.nonzero(to_values.col == vertex_idx)] = value
    return from_values, to_values


def filter_from_coo_matrix(coo_matrix, boolean_mask):
    """ Filter from coo matrix

    Applies a boolean mask to the data in a sparse matrix.
    """
    coo_matrix.row = coo_matrix.row[boolean_mask]
    coo_matrix.col = coo_matrix.col[boolean_mask]
    coo_matrix.data = coo_matrix.data[boolean_mask]
    return coo_matrix


def sparse_matrix_to_igraph(sparse_network):
    """ Convert sparse adjacency matrix to igraph

    Converts a sparse matrix to an undirected igraph object, including
    edge-weights.
    """
    sparse_network = sparse_network.tocoo()
    g = ig.Graph()
    g.to_undirected()
    g.add_vertices(np.arange(0, sparse_network.shape[0], dtype = 'int'))
    g.add_edges(list(zip(sparse_network.row, sparse_network.col)))
    g.es['weight'] = sparse_network.data
    return g


def sparse_matrix_to_networkx(sparse_network):
    g = nx.Graph(stad_graph)
    return g


def sparse_is_in(sparse_distance_matrix, sparse_network):
    """ Is-in for sparse matrices.

    This function efficiently determines which edges in the distance matrix are
    also present in the sparse network. It assumes that all edges of the sparse
    network exist in the sparse distance matrix, and that they are ordered
    similarly. E.g. no edge occurs in the sparse distance matrix before it does
    in the sparse network.
    
    Returns a boolean array indicating whether the edge in the distance matrix
    also exists in the network.

    This function is useful when combining edge-information of the full
    distance matrix with edges of a sparser network.
    """
    n_distances = len(sparse_distance_matrix.row)
    output_mask = np.zeros(n_distances, dtype = bool)
    network_idx = 0
    for idx in range(n_distances):
        is_same_edge = (sparse_distance_matrix.row[idx] == sparse_network.row[
            network_idx]) and (sparse_distance_matrix.col[idx] ==
                               sparse_network.col[network_idx])

        if is_same_edge:
            output_mask[idx] = True
            network_idx += 1
            if network_idx == len(sparse_network.data):
                break
    return output_mask
