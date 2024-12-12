import pandas as pd         
import networkx as nx   
from clustering import *
from graphs.graph_similarity import *
from graphs.graph import Graph
from matrices.matrix import Matrix

# Importo il CSV delle strisciate
df = pd.read_csv('log_veronaCard.csv')
POIs = sorted(df.iloc[:, 4].unique())

# Eseguo un test di visualizzazione sotto forma di grafo di qualche giornata

graphs = []
dates = []

d1 = '2018-01-01'
d2 = '2018-01-02'

# Genero inizialmente la matrice che rappresenta la giornata
m1 = Matrix.get_matrix(df[df.iloc[:, 0] == d1], POIs)
m2 = Matrix.get_matrix(df[df.iloc[:, 0] == d2], POIs)

# Stampa della matrice
print(f'{d1}: \n{m1}\n')
print(f'{d2}: \n{m2}')

# Creazione del grafo a partire dalla matrice
g1 = Graph.get_graph(m1, df[df.iloc[:, 0] == d1])
g2 = Graph.get_graph(m2, df[df.iloc[:, 0] == d1])

print('\nGED = ', get_ged(g1, g2))

graphs.extend([g1, g2])
dates.extend([d1, d2])

# Visualizzazione dei grafi
Graph.get_graph_image(graphs, dates)

