import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# Carica gli embedding
df = pd.read_csv('embeddings/2018/emb_2018.csv')

# Prendi solo i valori degli embedding
X = df.iloc[:, 1:].values  

# Riduzione dimensionale con PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Riduzione dimensionale con t-SNE
tsne = TSNE(n_components=2, perplexity=100, n_iter=1000, random_state=42)
X_tsne = tsne.fit_transform(X)

# Plot PCA
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.7)
plt.title("PCA sugli embedding")
plt.xlabel("PC1")
plt.ylabel("PC2")

# Plot t-SNE
plt.subplot(1, 2, 2)
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], alpha=0.7)
plt.title("t-SNE sugli embedding")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")

plt.show()