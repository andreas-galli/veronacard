import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Carica il dataset
df = pd.read_csv('embeddings/2018/emb_2018.csv')

# Rimuoviamo la colonna 'date' e usiamo solo gli embedding
X = df.iloc[:, 1:].values  # Prendiamo solo i vettori di embedding

# Applichiamo K-Means con un numero di cluster (es. 4)
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=1)
df['cluster'] = kmeans.fit_predict(X)

df = df.drop(df.columns[1:33], axis=1)

# Salva il risultato con i cluster
df.to_csv('embeddings/2018/clusters_2018.csv', index=False)

print("Clustering completato! I risultati sono salvati in 'clusters_2018.csv'")