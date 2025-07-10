import networkx as nx               
import matplotlib.pyplot as plt 
import pandas as pd    
import os
from pathlib import Path

# Classe contenente metodi volti alla generazione e alla visualizzazione di grafi

class Graph:
    # La generazione di un grafo avviene a partire da una matrice e il df contenente l'insieme dei POI del dataset log_veronaCard.csv
    def get_graph(matrix, df):
        path_distances_csv = Path(os.getcwd())
        path_distances_csv = Path(f'{path_distances_csv}/csv_files/poi_distances.csv')
        poi_distances = pd.read_csv(path_distances_csv)
        
        distances_dict = {
            (row['poi_id_1'], row['poi_id_2']): row['distance']
            for i, row in poi_distances.iterrows()
        }

        # Grafo orientato
        graph = nx.DiGraph()

        for poi in matrix.index:
            graph.add_node(poi)

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                weight = matrix.iat[i, j]
                if(weight > 0):
                    poi_i = matrix.index[i]
                    poi_j = matrix.columns[j]
                    distance = distances_dict.get((poi_i, poi_j), None)
                    graph.add_edge(matrix.index[i], matrix.columns[j], weight=weight, distance=distance)
        return graph  

    # Restituisce le immagini dei grafi inseriti nella lista di grafi 'graphs'
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
        plt.savefig(f'graph_images/{date}_graph.png', format='png', dpi=300)  # Salva il grafico come PNG con risoluzione 300 DPI
        plt.close()