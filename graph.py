import networkx as nx               
import matplotlib.pyplot as plt     

class Graph:
    def get_graph(df):
        # Grafo orientato
        graph = nx.DiGraph()

        counter = df[df.columns[1]].value_counts()
        multiple_IDs = counter[counter > 1].index
        df = df[df[df.columns[1]].isin(multiple_IDs)]

        # Per ogni POI creo un nodo
        poi = df.iloc[:, 4].unique()
        graph.add_nodes_from(list(map(int, poi)))

        # Per ogni cambio di POI, aggiungo un arco tra i POI (nodi) interessati, se esso non esiste, altrimenti incremento il peso dell'arco
        for id_value in multiple_IDs:

            # Itero solo su tuple aventi stesso ID
            same_ID = df[df.iloc[:, 1] == id_value]
            
            # Itero sulle righe adiacenti
            for i in range(len(same_ID) - 1):
                poi_prec = same_ID.iloc[i, 4]
                poi_succ = same_ID.iloc[i + 1, 4]
                
                # Se il POI è differente dal successivo aggiungo l'arco o incremento il peso
                if poi_prec != poi_succ:                            
                    if graph.has_edge(poi_prec, poi_succ):          
                        graph[poi_prec][poi_succ]['weight'] += 1                  # Incremento il peso
                    else:
                        graph.add_edge(int(poi_prec), int(poi_succ), weight=1)    # Creo l'arco
        return graph   
        
    def get_graph_image(graphs):
        for i, graph in enumerate(graphs):
            # Dimensione del grafo
            plt.figure(figsize=(12, 8)) 

            # Layout del grafo
            pos = nx.circular_layout(graph)

            # Etichette dei pesi
            edge_labels = nx.get_edge_attributes(graph, 'weight')

            # Disegno dei nodi
            nx.draw(graph, pos, with_labels=True, node_size=5000, node_color='skyblue', font_size=13, font_weight='bold', edge_color='black')

            # Disegno gli archi con curvatura solo se esistono due archi tra due nodi
            for (node1, node2, dati) in graph.edges(data=True):
                peso = dati['weight']
                
                if graphs[i].has_edge(node2, node1):  # Se esiste anche l'arco inverso (B -> A)
                    if node1 < node2:
                        # Disegna l'arco dritto A -> B
                        nx.draw_networkx_edges(graph, pos, edgelist=[(node1, node2)], edge_color='black', arrows=True, arrowstyle='-|>', arrowsize=20)
                        nx.draw_networkx_edge_labels(graph, pos, edge_labels={(node1, node2): peso}, font_size=12)
                    else:
                        # Disegna l'arco curvo B -> A
                        nx.draw_networkx_edges(graph, pos, edgelist=[(node2, node1)], connectionstyle="arc3,rad=0.15", edge_color='black', arrows=True, arrowstyle='-|>', arrowsize=20)
                        nx.draw_networkx_edge_labels(graph, pos, edge_labels={(node2, node1): peso}, font_size=12)
                else:
                    # Se c'è solo un arco tra due nodi, arco dritto
                    nx.draw_networkx_edges(graph, pos, edgelist=[(node1, node2)], edge_color='black', arrows=True, arrowstyle='-|>', arrowsize=20)
                    nx.draw_networkx_edge_labels(graph, pos, edge_labels={(node1, node2): peso}, font_size=12)
            plt.title(f"GRAPH {i+1}", fontweight='bold', fontsize='12')
        plt.subplots_adjust()
        plt.show()










""" Sezione relativa alla visualizzazione grafica del grafo
        # Dimensione del grafo
        #plt.figure(figsize=(12, 8)) 

        # Layout del grafo
        #pos = nx.circular_layout(graph)

        # Etichette dei pesi
        #edge_labels = nx.get_edge_attributes(graph, 'weight')

        # Disegno i nodi
        #nx.draw(graph, pos, with_labels=True, node_size=5000, node_color='skyblue', font_size=13, font_weight='bold', edge_color='black')

        # Disegno gli archi con curvatura solo se esistono due archi tra due nodi
        for (node1, node2, dati) in graph.edges(data=True):
            peso = dati['weight']
            
            if graph.has_edge(node2, node1):  # Se esiste anche l'arco inverso (B -> A)
                if node1 < node2:
                    # Disegna l'arco dritto A -> B
                    nx.draw_networkx_edges(graph, pos, edgelist=[(node1, node2)], edge_color='black', arrows=True, arrowstyle='-|>', arrowsize=20)
                    nx.draw_networkx_edge_labels(graph, pos, edge_labels={(node1, node2): peso}, font_size=12)
                else:
                    # Disegna l'arco curvo B -> A
                    nx.draw_networkx_edges(graph, pos, edgelist=[(node2, node1)], connectionstyle="arc3,rad=0.15", edge_color='black', arrows=True, arrowstyle='-|>', arrowsize=20)
                    nx.draw_networkx_edge_labels(graph, pos, edge_labels={(node2, node1): peso}, font_size=12)
            else:
                # Se c'è solo un arco tra due nodi, arco dritto
                nx.draw_networkx_edges(graph, pos, edgelist=[(node1, node2)], edge_color='black', arrows=True, arrowstyle='-|>', arrowsize=20)
                nx.draw_networkx_edge_labels(graph, pos, edge_labels={(node1, node2): peso}, font_size=12)

        #plt.title("Grafo relativo al cambio dei POI")
        #plt.show()
""" 
        