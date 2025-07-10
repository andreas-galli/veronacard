import pandas as pd         
import networkx as nx 
from gnn import *
from graph import Graph
from matrix import Matrix
import torch
from torch_geometric.data import Data

# Importo il CSV delle strisciate
df = pd.read_csv('../csv_files/log_veronaCard.csv')
POIs = sorted(df.iloc[:, 4].unique())

# Eseguo un test di visualizzazione sotto forma di grafo di qualche giornata

graphs = []
dates = []

d1 = '2018-01-01'
d2 = '2018-07-16'

# Genero inizialmente la matrice che rappresenta la giornata
m1 = Matrix.get_matrix(df[df.iloc[:, 0] == d1], POIs)
m2 = Matrix.get_matrix(df[df.iloc[:, 0] == d2], POIs)

# Creazione del grafo a partire dalla matrice
g1 = Graph.get_graph(m1, df[df.iloc[:, 0] == d1])
g2 = Graph.get_graph(m2, df[df.iloc[:, 0] == d1])

graphs.extend([g1, g2])
dates.extend([d1, d2])

# Visualizzazione dei grafi
Graph.get_graph_image(graphs, dates)