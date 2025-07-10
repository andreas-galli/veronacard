import pandas as pd         
import networkx as nx   
from clustering import *
from gnn import *
from graph import Graph
from matrix import Matrix
import torch
import pickle
from torch_geometric.data import Data, Batch

# Caricamento dei dati
df = pd.read_csv('log_veronaCard.csv')
POIs = sorted(df.iloc[:, 4].unique())

df_year = df[(df.iloc[:, 0] >= '2018-01-01') & (df.iloc[:, 0] <= '2018-12-31')]

unique_dates = sorted(df_year.iloc[:, 0].unique())

with open("saved_graphs.pkl", "rb") as g:
    graphs = pickle.load(g)
print("Grafi caricati.")

# Inizializza gli embeddings
embeddings = []

# Set delle dimensioni dell'embedding e del peso delle caratteristiche strutturali
out_dim = 64  # Imposta il numero di dimensioni dell'embedding
hidden_dim=128
structure_weight=0.5

# Creazione del batch
pyg_data_batch = Batch.from_data_list([graph_to_pyg_data(graph, structure_weight=structure_weight) for graph in graphs.values()])

# Esegui il modello sui dati in batch
model = GraphEmbeddingModel(in_dim=1, hidden_dim=hidden_dim, out_dim=out_dim)
model.eval()  # Modalità di valutazione

# Calcola gli embeddings per tutti i grafi nel batch
graph_embeddings = model(pyg_data_batch).detach().numpy()

# Associa ogni embedding con la sua data
for i, date in enumerate(unique_dates):
    embeddings_data = {'date': date}  # La data associata al grafo
    for j in range(out_dim):
        embeddings_data[f'v{j}'] = graph_embeddings[i][j]  # Aggiungi i valori dell'embedding per ogni dimensione
    embeddings.append(embeddings_data)  # Aggiungi i dati dell'embedding alla lista
    print(f"Embedding per la data {date} calcolato.")

# Salva gli embeddings in un CSV
embeddings_df = pd.DataFrame(embeddings)
embeddings_df.to_csv('embeddings/2018/emb_2018.csv', index=False)

print("Embeddings calcolati e salvati.")