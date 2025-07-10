import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Carica il dataset
df = pd.read_csv('results/2018/emb_2018.csv')

# Rimuoviamo la colonna 'date' e usiamo solo gli embedding
X = df.iloc[:, 1:].values  # Prendiamo solo i vettori di embedding


# Calcola l'inertia (somma delle distanze) per diversi valori di k
inertias = []
k_range = range(1, 11)  # Prova valori di k da 1 a 10 (puoi adattarlo in base alle tue necessità)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)

# Traccia il grafico del gomito
plt.figure(figsize=(8, 6))
plt.plot(k_range, inertias, marker='o')
plt.title('Metodo del Gomito per K-Means')
plt.xlabel('Numero di Cluster (k)')
plt.ylabel('Inertia')
plt.xticks(k_range)
plt.grid(True)
plt.show()