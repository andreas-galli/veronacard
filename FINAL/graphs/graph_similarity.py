import copy

def edit_weight_cost(edge1, edge2):
    return abs(edge1['weight'] - edge2['weight'])

def abs_to_rev_graph_weights(graph):
    # Funzione che relativizza i pesi degli archi rispetto al numero di spostamenti totali avvenuti nella giornata
    graph_copy = copy.deepcopy(graph)
    weights_sum = sum(data['weight'] for u, v, data in graph_copy.edges(data=True))
    if weights_sum == 0:
        return graph_copy
    for u, v, data in graph_copy.edges(data=True):
        data['weight'] = round(data['weight'] / weights_sum * 100, 2)
    return graph_copy

def get_ged(g1, g2):
    # Graph Edit Distance semplificata (per avere un tempo di esecuzione ridotto)
    total_cost = 0

    if len(g1.nodes()) == 0 or len(g2.nodes()) == 0:
        return -1

    edges_g1 = {(u, v) for u, v, data in g1.edges(data=True)}
    edges_g2 = {(u, v) for u, v, data in g2.edges(data=True)}
    nodes_g1 = set(g1.nodes())
    nodes_g2 = set(g2.nodes())
    total_cost += len(edges_g1 - edges_g2) + len(edges_g2 - edges_g1) + len(nodes_g1 - nodes_g2) + len(nodes_g2 - nodes_g1)
    return total_cost

def get_absolute_distance(g1, g2):
    # Non si considerano le differenze strutturali, ma solo le differenze tra flussi su percorsi comuni (il nome della funzione non è esattissimo)
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

    # Sommo al total_cost i pesi degli archi che sono in un grafo, ma non nell'altro
    for edge in (edges_g1 - edges_g2):
        total_cost += g1.get_edge_data(edge[0], edge[1])['weight']

    for edge in (edges_g2 - edges_g1):
        total_cost += g2.get_edge_data(edge[0], edge[1])['weight']

    return total_cost