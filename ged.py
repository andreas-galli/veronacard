# Implementazione Algoritmo di Similarità tra Grafi GRAPH EDIT DISTANCE (approssimativo), e di due sue varianti

import copy

def edit_weight_cost(edge1, edge2):
    return abs(edge1['weight'] - edge2['weight'])

def abs_to_rev_graph_weights(graph):
    graph_copy = copy.deepcopy(graph)
    weights_sum = sum(data['weight'] for u, v, data in graph_copy.edges(data=True))
    if weights_sum == 0:
        return graph_copy
    for u, v, data in graph_copy.edges(data=True):
        data['weight'] = round(data['weight'] / weights_sum * 100, 2)
    return graph_copy

def get_ged(g1, g2):
    # EDIT DISTANCE GRAPH
    total_cost = 0

    if len(g1.nodes()) == 0 or len(g2.nodes()) == 0:
        return -1

    edges_g1 = {(u, v) for u, v, data in g1.edges(data=True)}
    edges_g2 = {(u, v) for u, v, data in g2.edges(data=True)}
    nodes_g1 = set(g1.nodes())
    nodes_g2 = set(g2.nodes())
    total_cost += len(edges_g1 - edges_g2) + len(edges_g2 - edges_g1) + len(nodes_g1 - nodes_g2) + len(nodes_g2 - nodes_g1)
    return total_cost

def get_absolute_weighted_ged(g1, g2):
    # Non considero le differenze strutturali, ma solo differenze sui pesi di archi comuni
    total_cost = 0

    if len(g1.nodes()) == 0 or len(g2.nodes()) == 0:
        return -1

    edges_g1 = {(u, v) for u, v, data in g1.edges(data=True)}
    edges_g2 = {(u, v) for u, v, data in g2.edges(data=True)}
    common_edges = edges_g1 & edges_g2
    for edge in common_edges:
        edge1 = g1.get_edge_data(edge[0], edge[1])
        edge2 = g2.get_edge_data(edge[0], edge[1])
        total_cost += edit_weight_cost(edge1, edge2)
    return total_cost

def get_relative_weighted_ged(g1, g2):
    # Non considero le differenze strutturali, ma solo differenze sui pesi di archi comuni
    total_cost = 0

    if len(g1.nodes()) == 0 or len(g2.nodes()) == 0:
        return -1

    g1_rel = abs_to_rev_graph_weights(g1)
    g2_rel = abs_to_rev_graph_weights(g2)

    edges_g1 = {(u, v) for u, v, data in g1_rel.edges(data=True)}
    edges_g2 = {(u, v) for u, v, data in g2_rel.edges(data=True)}
    common_edges = edges_g1 & edges_g2
    for edge in common_edges:
        edge1 = g1_rel.get_edge_data(edge[0], edge[1])
        edge2 = g2_rel.get_edge_data(edge[0], edge[1])
        total_cost += edit_weight_cost(edge1, edge2)
    return total_cost