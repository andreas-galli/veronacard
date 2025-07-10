import pandas as pd
import sklearn.cluster as skl
import matplotlib.pyplot as plt

def KMeans_clustering():
    distance_matrix = pd.read_csv('csv_files/2_2018_WEIGHT_distance_matrix.csv', index_col=0)
    print(distance_matrix)
    # Un vettore per ogni data
    distance_values = distance_matrix.values

    # Questa porzione di codice viene eseguita solo per determinare quale numero di cluster è più opportuno
    
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
    
    # Imposto il numero di cluster, scegliendolo con il metodo del gomito
    n_clusters = 3  
    kmeans = skl.KMeans(n_clusters=n_clusters)
    clusters = kmeans.fit_predict(distance_values)

    # Preparo il df per salvarlo nel csv
    results = pd.DataFrame({
        'DATE': distance_matrix.index,
        'CLUSTER': clusters
    })

    # Decisione del csv su cui salvare i risultati del clustering
    results.to_csv('TIROCINIO_2018_WEIGHT_clustering.csv', index=False)