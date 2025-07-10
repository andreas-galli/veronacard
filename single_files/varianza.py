import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Carica gli embedding
df = pd.read_csv("embeddings/2018/emb_2018.csv")

# Rimuovi la colonna 'date' e prendi solo gli embedding
X = df.iloc[:, 1:].values  

# Normalizziamo gli embedding (opzionale, ma utile)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Applica PCA
pca = PCA(n_components=10)  # Prendiamo le prime 10 componenti
X_pca = pca.fit_transform(X_scaled)

# Grafico varianza spiegata
plt.figure(figsize=(8,5))
plt.plot(range(1, 11), np.cumsum(pca.explained_variance_ratio_), marker='o', linestyle='--')
plt.xlabel('Numero di Componenti')
plt.ylabel('Varianza Spiegata Cumulativa')
plt.title('Analisi Varianza Spiegata con PCA')
plt.grid()
plt.show()
