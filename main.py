import pandas as pd         
import networkx as nx   
from clustering import *
from ged import *
from graph import Graph
from matrix import Matrix
from distanceBetwPOIs import Haversine
from weather import get_weather_by_date

"""Molte righe sono commentate poiché utili alla sola generazione di csv"""

# Importo il CSV delle strisciate
df = pd.read_csv('log_veronaCard.csv')
POIs = sorted(df.iloc[:, 4].unique())

graphs = []
dates = []

d1 = '2018-01-10'
d2 = '2018-01-13'

m1 = Matrix.get_matrix(df[df.iloc[:, 0] == d1], POIs)
m2 = Matrix.get_matrix(df[df.iloc[:, 0] == d2], POIs)
print(f'{d1}: \n{m1}\n')
print(f'{d2}: \n{m2}')

g1 = Graph.get_graph(m1, df[df.iloc[:, 0] == d1])
g2 = Graph.get_graph(m2, df[df.iloc[:, 0] == d1])

print('\nGED = ', get_ged(g1, g2))

graphs.extend([g1, g2])
dates.extend([d1, d2])
Graph.get_graph_image(graphs, dates)


#KMeans_clustering()

#spectral_clustering() # Non produce buoni risultati di silhouette score

#DBSCAN_clustering()

#GENERAZIONE results_v3.csv

# Mantengo tutte le tuple escludendo l'anno 2020
df_2 = df[(df.iloc[:, 0] >= '2016-01-01') & (df.iloc[:, 0] <= '2016-12-31')]

unique_dates = sorted(df_2.iloc[:, 0].unique())

graphs = {}

for date in unique_dates:
    df_date = df_2[df_2.iloc[:, 0] == date]
    #genero ogni grafo a partire dalla sua matrice 
    graphs[date] = Graph.get_graph(Matrix.get_matrix(df_date, POIs), df_date)

results = []

"""
# Confronto ogni coppia di grafi presente nel dataset e salvo i risultati in un csv
with open('results_v3/2016/2016_results_v3.csv', 'w') as file:
    for i in range(len(unique_dates)):
        for j in range(i + 1, len(unique_dates)):
            date1 = unique_dates[i]
            date2 = unique_dates[j]
            graph1 = graphs[date1]
            graph2 = graphs[date2]

            approx_ged = get_ged(graph1, graph2)
            abs_wged = get_absolute_weighted_ged(graph1, graph2)

            print(f'{date1}, {date2}: {approx_ged}')

            results.append({
                'DATE1': date1,
                'DATE2': date2, 
                'GED': approx_ged,
                'ABS_WGED': abs_wged 
            })
results_df = pd.DataFrame(results).to_csv('results_v3/2016/2016_results_v3.csv', index=False)
print("Done")
"""

"""
# MATRICE DELLE DISTANZE USANDO COME METRICA LE STRUTTURE DEI GRAFI
#GENERAZIONE DEL FILE distanceMatrix.csv e verifica del funzionamento
distance_matrix = Matrix.get_GED_matrix_from_csv('results_v3/2016/2016_results_v3.csv')
distance_matrix.to_csv('results_v3/2016/struttura/GED_distance_matrix.csv', header=True)

# Leggi il CSV nella matrice delle distanze
distance_matrix = pd.read_csv('results_v3/2016/struttura/GED_distance_matrix.csv', index_col=0)
# Mostra la matrice per verificare che sia correttamente caricata
print(distance_matrix)




#MATRICE DELLE DISTANZE USANDO COME METRICA I PESI NORMALIZZATI
#GENERAZIONE DEL FILE distanceMatrix.csv e verifica del funzionamento
distance_matrix = Matrix.get_WEIGHT_matrix_from_csv('results_v3/2016/2016_results_v3.csv')
distance_matrix.to_csv('results_v3/2016/flussi/WEIGHT_distance_matrix.csv', header=True)

# Leggi il CSV nella matrice delle distanze
distance_matrix = pd.read_csv('results_v3/2016/flussi/WEIGHT_distance_matrix.csv', index_col=0)

# Mostra la matrice per verificare che sia correttamente caricata
print(distance_matrix) 

#MATRICE DELLE DISTANZE USANDO COME METRICA FLUSSI + STRUTTURA
#GENERAZIONE DEL FILE distanceMatrix.csv e verifica del funzionamento
distance_matrix = Matrix.get_GED_WEIGHT_matrix_from_csv('results_v3/2016/2016_results_v3.csv')
distance_matrix.to_csv('results_v3/2016/flussi&struttura/GED_WEIGHT_distance_matrix.csv', header=True)

# Leggi il CSV nella matrice delle distanze
distance_matrix = pd.read_csv('results_v3/2016/flussi&struttura/GED_WEIGHT_distance_matrix.csv', index_col=0)
# Mostra la matrice per verificare che sia correttamente caricata
print(distance_matrix)
"""