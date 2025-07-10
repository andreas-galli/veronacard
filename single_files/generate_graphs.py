import pandas as pd         
import networkx as nx   
from clustering import *
from graph_similarity import *
from gnn import *
from graph import Graph
from matrix import Matrix
import torch
from torch_geometric.data import Data, Batch
import pickle

# Caricamento dei dati
df = pd.read_csv('log_veronaCard.csv')
POIs = sorted(df.iloc[:, 4].unique())

df_year = df[(df.iloc[:, 0] >= '2018-01-01') & (df.iloc[:, 0] <= '2018-12-31')]

unique_dates = sorted(df_year.iloc[:, 0].unique())

graphs = {}

# Creazione dei grafi per ogni data
for date in unique_dates:
    df_date = df_year[df_year.iloc[:, 0] == date]
    graphs[date] = Graph.get_graph(Matrix.get_matrix(df_date, POIs), df_date)
    print(date)

with open("saved_graphs.pkl", "wb") as f:
    pickle.dump(graphs, f)

print("Grafi salvati con successo!")