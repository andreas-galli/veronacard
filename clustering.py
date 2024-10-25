import pandas as pd
import numpy as np
import sklearn.cluster as skl
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

def KMeans_clustering():
    distance_matrix = pd.read_csv('results_v3/flussi+struttura/2018_GED_WEIGHT_distance_matrix.csv', index_col=0)
    
    # Un vettore per ogni data
    distance_values = distance_matrix.values

    """
    # DEFINIZIONE N CLUSTER IN BASE AL METODO DEL GOMITO
    inertia_values = []
    n_cluster = range(1, 21)

    for n in n_cluster:
        kMeans = skl.KMeans(n_clusters=n, random_state=0)
        kMeans.fit(distance_values)
        inertia_values.append(kMeans.inertia_)

    plt.figure(figsize=(8, 6))
    plt.plot(n_cluster, inertia_values)
    plt.title('Elbow method')
    plt.xlabel('Cluster number')
    plt.xticks(range(1, 21))
    plt.ylabel('Inertia')
    plt.grid(True)
    plt.show()
    """
    n_clusters = 4
    kmeans = skl.KMeans(n_clusters=n_clusters)
    clusters = kmeans.fit_predict(distance_values)

    # Preparo il df per salvarlo nel csv
    results = pd.DataFrame({
        'DATE': distance_matrix.index,
        'CLUSTER': clusters
    })

    results.to_csv('results_v3/struttura/2018_GED_clustering.csv', index=False)
    


# Non produce risultati soddisfacenti
def spectral_clustering():
    distance_matrix = pd.read_csv('results_v3/struttura/2018_GED_distance_matrix.csv', index_col=0)
        
    # Trasformazione della matrice di distanze in una matrice di similarità
    gamma = 1

    # Spectral Clustering necessita della matrice di similarità (la genero a partire da quella delle distanze)
    similarity_matrix = np.exp(-gamma * distance_matrix)
    
    n_clusters_range = range(2, 11)
    silhouette_values = []

    for n in n_clusters_range:
        spectral = skl.SpectralClustering(
            n_clusters=n,
            affinity='precomputed'
        )
        clusters = spectral.fit_predict(similarity_matrix)
        
        # Calcola il Silhouette Score usando la distance matrix
        score = silhouette_score(distance_matrix, clusters, metric='precomputed')
        silhouette_values.append(score)
    
    for n, score in zip(n_clusters_range, silhouette_values):
        print(f'n_clusters={n}, Silhouette Score={round(score, 2)}')
