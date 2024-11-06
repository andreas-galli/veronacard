import networkx as nx               
import matplotlib.pyplot as plt     

class Graph:
    def get_graph(matrix, df):
        # Grafo orientato
        graph = nx.DiGraph()
        for poi in matrix.index:
            if poi in df:
                graph.add_node(poi)

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                weight = matrix.iat[i, j]
                if weight > 0:
                    graph.add_edge(matrix.index[i], matrix.columns[j], weight=weight)

        return graph  
        
    def get_graph_image(graphs, dates):
        graphs = graphs if graphs is not None else []
        dates = dates if dates is not None else []
        # Per mantenere i nodi comuni nella stessa posizione nei grafi generati
        union_graph = nx.DiGraph()
        for graph in graphs:
            union_graph.add_nodes_from(graph.nodes())
        pos = nx.circular_layout(union_graph)

        for i, (graph, date) in enumerate(zip(graphs, dates)):
            # Dimensione del grafo
            n_movements = 0
            for (node1, node2, dati) in graph.edges(data=True):
                peso = dati['weight']
                n_movements += peso
            
            plt.figure(figsize=(12, 8)).canvas.manager.set_window_title(f'{date} GRAPH, {n_movements} total movements')
            
            # Etichette dei pesi
            edge_labels = nx.get_edge_attributes(graph, 'weight')

            # Disegno dei nodi
            nx.draw(graph, pos, with_labels=True, node_size=5000, node_color='skyblue', font_size=13, font_weight='bold', edge_color='black')

            for (node1, node2, dati) in graph.edges(data=True):
                peso = dati['weight']

                nx.draw_networkx_edges(graph, pos, edgelist=[(node1, node2)], edge_color='black', arrows=True, arrowstyle='-|>', arrowsize=20)

                if (node2, node1) not in edge_labels or node1 < node2:
                    nx.draw_networkx_edge_labels(graph, pos, edge_labels={(node1, node2): peso}, font_size=12)
        plt.subplots_adjust()
        plt.show()