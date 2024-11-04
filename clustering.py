import pandas as pd
import numpy as np
import sklearn.cluster as skl
import matplotlib.pyplot as plt
import holidays
from sklearn.metrics import silhouette_score
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import kneed

def KMeans_clustering():
    distance_matrix = pd.read_csv('results_v3/2017/struttura/GED_distance_matrix.csv', index_col=0)
    
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

    n_clusters = 3  
    kmeans = skl.KMeans(n_clusters=n_clusters)
    clusters = kmeans.fit_predict(distance_values)

    # Preparo il df per salvarlo nel csv
    results = pd.DataFrame({
        'DATE': distance_matrix.index,
        'CLUSTER': clusters
    })

    results.to_csv('results_v3/2017/struttura/2017_GED_clustering.csv', index=False)

    #AGGIUNTA DELLA COLONNA CHE INDICA IL GIORNO FESTIVO
    df_clustering = pd.read_csv('results_v3/2017/struttura/2017_GED_clustering.csv')
    it_holidays = holidays.IT(years=2017)
    df_clustering['HOLIDAY'] = df_clustering['DATE'].apply(lambda x: 'YES' if pd.to_datetime(x) in it_holidays or pd.to_datetime(x).weekday() == 6 else 'NO')
    df_clustering.to_csv('results_v3/2017/struttura/2017_GED_clustering.csv', index=False)


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

def DBSCAN_clustering():
    distance_matrix = pd.read_csv('results_v3/2018/flussi/2018_WEIGHT_distance_matrix.csv', index_col=0)

    min_samples = 1
    eps_values = [6, 5.5, 5, 4.5, 4, 3.5, 3, 2.5, 2]
    cluster_results = {}

    for eps in eps_values:
        dbscan = DBSCAN(eps=eps, min_samples=min_samples, metric='precomputed')
        clusters = dbscan.fit_predict(distance_matrix)
        
        n_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
        n_noise = list(clusters).count(-1)
        cluster_results[eps] = (n_clusters, n_noise)

        print(f"eps={eps}: {n_clusters} clusters, {n_noise} noise points")