import numpy as np
import pandas as pd

from .sparse import sparse_is_in

def draw_correlations_matplotlib(detail, histogram_bins = 20,
                                 ax = None):
    """ Draw the correlation and penalised correlation using matplotlib

    Plots a histogram of normalised edge distances and the correlation curve.

    Parameters
    ----------
    detail: dictionary
        The detail dictionary returnd by STAD.
    histogram_bins: int
        The number of bins to use for the histogram
    ax: matplotlib Axes object
        The matplotlib axes to draw to. If None, a new one is created

    Returns
    -------
    fig: the matplotlib Figure object that was drawn to
    """
    import matplotlib.pyplot as plt

    if ax is None:
        fig = plt.figure()
        ax = plt.gca()
    else:
        plt.sca(ax)
        fig = plt.gcf()

    ax.hist(detail['non_mst_distances'].data, bins = histogram_bins)
    ax.set_xlabel('Normalised edge distance')
    ax.set_ylabel('Count')

    ax2 = plt.gca().twinx()
    ax2.plot(detail['distance_thresholds'], detail['penalised_correlations'],
             '.', color = 'C2', label = 'penalty correlation')
    ax2.plot(detail['distance_thresholds'], detail['correlations'],
             '.', color = 'C1', label = 'correlation')
    plt.legend()
    ax2.set_ylabel('Correlation')
    ax2.set_ylim([0, 1])
    plt.xlim([0, 1])
    return fig


def draw_optimiser_matplotlib(detail):
    """ Visualises the iterations of the optimiser

    Useful to determine whether the optimiser converged.

    Parameters
    ----------
    detail: dictionary
        The detail dictionary returned by STAD.

    Returns
    -------
    fig: a matplotlib Figure object that was drawn to
    """
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(4, 1)
    draw_optimiser_correlation_matplotlib(detail, axes[0])
    draw_optimiser_penalised_correlation_matplotlib(detail, axes[1])
    draw_optimiser_thresholds_matplotlib(detail, axes[2])
    draw_optimiser_edges_matplotlib(detail, axes[3])
    return fig


def draw_optimiser_correlation_matplotlib(detail, ax = None):
    """ Draws the correlation of the optimiser iterations

    Shows whether the optimiser converged.

    Parameters
    ----------
    detail: dictionary
        The detail dictionary returned by STAD.
    ax: matplotlib Axes object
        The matplotlib axes to draw to. If None, a new one is created

    Returns
    -------
    fig: the matplotlib Figure object that was drawn to
    """
    import matplotlib.pyplot as plt

    if ax is None:
        fig = plt.figure()
        ax = plt.gca()
    else:
        plt.sca(ax)
        fig = plt.gcf()

    ax.plot(detail['correlations'], '.', color = 'C1')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Correlation')

    return fig


def draw_optimiser_penalised_correlation_matplotlib(detail, ax = None):
    """ Draws the correlation of the optimiser iterations

    Shows whether the optimiser converged.

    Parameters
    ----------
    detail: dictionary
        The detail dictionary returned by STAD.
    ax: matplotlib Axes object
        The matplotlib axes to draw to. If None, a new one is created

    Returns
    -------
    fig: the matplotlib Figure object that was drawn to
    """
    import matplotlib.pyplot as plt

    if ax is None:
        fig = plt.figure()
        ax = plt.gca()
    else:
        plt.sca(ax)
        fig = plt.gcf()

    ax.plot(detail['penalised_correlations'], '.', color = 'C2')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Penalty correlation')

    return fig


def draw_optimiser_thresholds_matplotlib(detail, ax = None):
    """ Draws the normalised distance thresholds of the optimiser iterations

    Shows whether the optimiser converged.

    Parameters
    ----------
    detail: dictionary
        The detail dictionary returned by STAD.
    ax: matplotlib Axes object
        The matplotlib axes to draw to. If None, a new one is created

    Returns
    -------
    fig: the matplotlib Figure object that was drawn to
    """
    import matplotlib.pyplot as plt

    if ax is None:
        fig = plt.figure()
        ax = plt.gca()
    else:
        plt.sca(ax)
        fig = plt.gcf()

    ax.plot(detail['distance_thresholds'], '.', color = 'C0')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('edge distance')

    return fig


def draw_optimiser_edges_matplotlib(detail, ax = None):
    """ Draws the number of added edges of the optimiser iterations

    Shows whether the optimiser converged.

    Parameters
    ----------
    detail: dictionary
        The detail dictionary returned by STAD.
    ax: matplotlib Axes object
        The matplotlib axes to draw to. If None, a new one is created

    Returns
    -------
    fig: the matplotlib Figure object that was drawn to
    """
    import matplotlib.pyplot as plt

    if ax is None:
        fig = plt.figure()
        ax = plt.gca()
    else:
        plt.sca(ax)
        fig = plt.gcf()

    ax.plot(detail['added_edges'], '.', color = 'C3')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Added edges')

    return fig


def draw_network_matplotlib(stad_graph, detail, layout = 'spring', ax = None,
                            positions = None,
                            edge_color = 'lightgrey',
                            adjacent_edge_color = 'skyblue',
                            edge_alpha = 1,
                            **kwargs):
    """ Draws the network using NetworkX

    Parameters
    ----------
    stad_graph: SciPy sparse matrix
    The output of STAD (or another graph from detail).
    detail: dictionary
        The detail dictionary returned by STAD.
    layout:
        The layout to use for drawing:
        ::
            >>> "kk": nx.kamada_kawai_layout,
            >>> "spring": nx.spring_layout,
            >>> "circ": nx.circular_layout,
            >>> "spect": nx.spectral_layout
    positions: np.array
        Positions to use for drawing, overrides layout. Should be either a
        networkx layout dictionary or a 2d numpy array.
    edge_color: string
        Color to dray edges in.
    adjacent_edge_color: string
        Color to dray adjacent edges in.
    edge_alpha: float
        Transparancy of edges
    ax: matplotlib Axes object
        The matplotlib axes to draw to. If None, a new one is created
    kwargs:
        Keyword arguments for networkx.draw_networkx_nodes()

    Returns
    -------
    fig: the matplotlib Figure object that was drawn to
    nodes: the networkx nodes object
    """

    import networkx as nx
    import matplotlib.pyplot as plt

    if ax is None:
        fig = plt.figure()
        ax = plt.gca()
    else:
        plt.sca(ax)
        fig = plt.gcf()

    layouts = {
        "kk": nx.kamada_kawai_layout,
        "spring": nx.spring_layout,
        "circ": nx.circular_layout,
        "spect": nx.spectral_layout
    }

    # Determine node size, from:
    # https://github.com/scikit-tda/kepler-mapper/blob/master/kmapper/drawing.py
    bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    width, height = bbox.width, bbox.height
    area = width * height * fig.dpi
    n_nodes = stad_graph.shape[0]

    # size of node should be related to area and number of nodes -- heuristic
    node_size = np.pi * area / n_nodes
    node_r = np.sqrt(node_size / np.pi)
    node_edge = node_r / 3

    # should just work
    g = nx.Graph(stad_graph)
    if not (positions is None):
        if isinstance(positions, dict):
            pos = positions
        else:
            pos = dict()
            for idx in range(positions.shape[0]):
                pos[idx] = np.array([positions[idx, 0], positions[idx, 1]])
    else:
        pos = layouts[layout](g)
    nodes = nx.draw_networkx_nodes(g, node_size = node_size, pos = pos,
                                   ax = ax, **kwargs)

    edges = nx.draw_networkx_edges(g, pos = pos, ax = ax,
                                   edge_color = edge_color,
                                   alpha = edge_alpha)

    if 'adjacent_edges' in detail:
        graph_mask = sparse_is_in(detail['adjacent_edges'], stad_graph)
        adjacent_mask = detail['adjacent_edges'].data[graph_mask]
        edge_list = np.array(g.edges())[adjacent_mask]
        edge_list = [(e[0], e[1]) for e in edge_list]
        edges = nx.draw_networkx_edges(
            g, pos = pos, ax = ax, alpha = edge_alpha,
            edge_color = adjacent_edge_color,
            edgelist = edge_list
        )

    edges.set_linewidth(node_edge)

    nodes.set_edgecolor("w")
    nodes.set_linewidth(node_edge)

    ax.axis("off")

    return fig, nodes, edges, g, pos


def build_vega_spec(stad_graph, detail, vertex_data, color_type = "continuous",
                    color_field = None, output_size = (600, 600), strength = -3,
                    distance = 15, radius = 5, theta = 0.9, distance_max = 100):
    """ Creates a vega-spec for an interactive graph visualisation

    Parameters
    ----------
    stad_graph: SciPy sparse matrix
        The output network from STAD
    detail: dictionary
        The detail dictionary from STAD
    vertex_data: pandas.DataFrame
        A dataframe containing vertex data
    color_type: string
        Should the colour be mapped 'continuous' or 'categorical'?
    color_field: string
        The column name of `vertex_data` to map to the colourscale
    output_size: tuple (width, height)
        The output size in pixels
    strength: int
        Vega nbody force simulation parameter
    distance: int
        Vega nbody force simulation parameter
    radius: int
        Vega nbody force simulation parameter
    theta: float
        Vega nbody force simulation parameter
    distance_max: int
        Vega nbody force simulation parameter

    Returns
    -------
        Vega spec dictionary
    """
    # Convert to record-type dict
    vertex_data['name'] = np.arange(0, stad_graph.shape[0])
    if 'community_membership' in detail:
        vertex_data['community'] = detail['community_membership']
    node_data = vertex_data.to_dict('record')
    edge_data = pd.DataFrame({
        'source': stad_graph.row,
        'target': stad_graph.col,
        'weight': stad_graph.data
    }).to_dict('record')

    colour_type_switch = {
        "continuous": "linear",
        "categorical": "ordinal",
    }

    tooltip_signal = {}
    feature_labels = node_data[0].keys()
    for f in feature_labels:
        tooltip_signal[f] = "datum['" + f + "']"

    vega_src = dict()
    vega_src["$schema"] = "https://vega.github.io/schema/vega/v5.json"
    vega_src["width"] = output_size[0]
    vega_src["height"] = output_size[1]
    vega_src["padding"] = 0
    vega_src["autosize"] = "none"
    vega_src["signals"] = [{
        "name": "cx",
        "update": "width / 2"
        }, {
        "name": "cy",
        "update": "height / 2"
        }, {
        "description": "State variable for active node dragged status.",
        "name": "dragged",
        "value": 0,
        "on": [{
            "events": "symbol:mouseout[!event.buttons], window:mouseup",
            "update": "0"
        }, {
            "events": "symbol:mouseover",
            "update": "dragged || 1"
        }, {
            "events": "[symbol:mousedown, window:mouseup] > window:mousemove!",
            "update": "2",
            "force": True
        }]
        }, {
        "description": "Graph node most recently interacted with.",
        "name": "dragged_node",
        "value": None,
        "on": [{
            "events": "symbol:mouseover",
            "update": "dragged === 1 ? item() : dragged_node"
        }]
    }, {
        "description": "Flag to restart Force simulation upon data changes.",
        "name": "restart",
        "value": False,
        "on": [{
            "events": {
                "signal": "dragged"
                },
            "update": "dragged > 1"
            }]
    }]
    vega_src["scales"] = [{
        "name": "colourScale",
        "type": colour_type_switch[color_type],
        "domain": {
            "data": "node-data",
            "field": color_field
        }
    }]
    if color_type == "continuous":
        vega_src["scales"][0]["range"] = {"scheme": "viridis"}
    else:
        vega_src["scales"][0]["range"] = {"scheme": "rainbow"}

    vega_src["legends"] = [{
        "fill": "colourScale"
        }]
    vega_src["data"] = [{
        "name": "node-data",
        "values": node_data
        }, {
        "name": "link-data",
        "values": edge_data
        }]
    vega_src["marks"] = []
    vega_src["marks"].append({
        "name": "nodes",
        "type": "symbol",
        "zindex": 1,
        "from": {
            "data": "node-data"
            },
        "on": [{
            "trigger": "dragged",
            "modify": "dragged_node",
            "values": "dragged === 1 ? {fx:dragged_node.x, fy:dragged_node.y} "
                      ": {fx:x(), fy:y()}"
        }, {
            "trigger": "!dragged",
            "modify": "dragged_node",
            "values": "{fx: null, fy: null}"
        }],
        "encode": {
            "enter": {
                "fill": {
                    "scale": "colourScale",
                    "field": color_field
                    },
                "tooltip": {
                    "signal": str(tooltip_signal).replace('"', '')
                }
            },
            "update": {
                "size": {
                    "value": 50
                    },
                "cursor": {
                    "value": "pointer"
                    }
            }
        },
        "transform": [{
            "type": "force",
            "iterations": 300,
            "velocityDecay": 0.5,
            "restart": {
                "signal": "restart"
                },
            "static": False,
            "forces": [{
                "force": "center",
                "x": {
                    "signal": "cx"
                    },
                "y": {
                    "signal": "cy"
                    }
                }, {
                "force": "collide",
                "radius": radius
                }, {
                "force": "nbody",
                "strength": strength,
                "theta": theta,
                "distanceMax": distance_max
                }, {
                "force": "link",
                "links": "link-data",
                "distance": distance
                }]
        }]
    })
    if (color_field is None) or (color_field == 'none'):
        vega_src["marks"][0]['encode']['enter']['fill'] = {"value": "skyblue"}

    vega_src["marks"].append({
        "type": "path",
        "from": {
            "data": "link-data"
            },
        "interactive": False,
        "encode": {
            "update": {
                "stroke": {
                    "value": "lightgrey"
                    }
            }
        },
        "transform": [{
            "type": "linkpath",
            "shape": "line",
            "sourceX": "datum.source.x",
            "sourceY": "datum.source.y",
            "targetX": "datum.target.x",
            "targetY": "datum.target.y"
        }]
    })

    return vega_src
