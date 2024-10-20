import pandas as pd
import sklearn.cluster as skl
import matplotlib.pyplot as plt

def clusterize():
    distance_matrix = pd.read_csv('results_v2/distanceMatrix.csv', index_col=0)
    
    # Un vettore per ogni data
    distance_values = distance_matrix.values

    """ 
    DEFINIZIONE N CLUSTER IN BASE AL METODO DEL GOMITO --> dal grafico 4 cluster, ma gruppi troppo eterogenei --> 5

    inertia_values = []
    n_cluster = range(1, 11)

    for n in n_cluster:
        kMeans = skl.KMeans(n_clusters=n, random_state=42)
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
    n_clusters = 5

    kmeans = skl.KMeans(n_clusters=n_clusters)
    clusters = kmeans.fit_predict(distance_values)

    # Preparo il df per salvarlo nel csv
    results = pd.DataFrame({
        'DATE': distance_matrix.index,
        'CLUSTER': clusters
    })

    results.to_csv('results_v2/clustering_results_using_distance_matrix.csv', index=False)