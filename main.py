import pandas as pd         
import networkx as nx   

from clustering import clusterize
from ged import *
from graph import Graph
from matrix import Matrix
from distanceBetwPOIs import Haversine
from weather import get_weather_by_date

"""Molte righe sono commentate poiché utili alla sola generazione di csv"""

# Importo il CSV delle strisciate
df = pd.read_csv('log_veronaCard.csv')

graphs = []
dates = []

d1 = '2015-06-22'
d2 = '2015-06-08'
d3 = '2015-06-11'

g1 = Graph.get_graph(df[df.iloc[:, 0] == d1])
g2 = Graph.get_graph(df[df.iloc[:, 0] == d2])
g3 = Graph.get_graph(df[df.iloc[:, 0] == d3])

graphs.extend([g1, g2, g3])
dates.extend([d1, d2, d3])
Graph.get_graph_image(graphs, dates) 


get_weather_by_date(d1)
get_weather_by_date(d2)
get_weather_by_date(d3)

#clusterize()


#GENERAZIONE DEL FILE distanceMatrix.csv e verifica del funzionamento
"""
distance_matrix = Matrix.get_matrix_from_csv('results_v2/results_v2.csv')
distance_matrix.to_csv('results_v2/distanceMatrix.csv', header=True)

# Leggi il CSV nella matrice delle distanze
distance_matrix = pd.read_csv('results_v2/distanceMatrix.csv', index_col=0)

# Mostra la matrice per verificare che sia correttamente caricata
print(distance_matrix)
"""


#GENERAZIONE results_v2.csv
"""
# Mantengo tutte le tuple escludendo l'anno 2020
df_2 = df[(df.iloc[:, 0] >= '2014-01-01') & (df.iloc[:, 0] <= '2019-12-31')]

unique_dates = sorted(df_2.iloc[:, 0].unique())

graphs = {}

for date in unique_dates:
    df_date = df_2[df_2.iloc[:, 0] == date]
    graphs[date] = Graph.get_graph(df_date)

results = []

# Confronto ogni coppia di grafi presente nel dataset e salvo i risultati in un csv
with open('results_v2.csv', 'w') as file:
    for i in range(len(unique_dates)):
        for j in range(i + 1, len(unique_dates)):
            date1 = unique_dates[i]
            date2 = unique_dates[j]
            graph1 = graphs[date1]
            graph2 = graphs[date2]

            approx_ged = get_ged(graph1, graph2)
            abs_wGed = get_absolute_weighted_ged(graph1, graph2)

            print(f'{date1}, {date2}: {abs_wGed}')

            results.append({
                'DATE1': date1,
                'DATE2': date2, 
                'GED': approx_ged,
                'ABS_WGED': abs_wGed
            })
results_df = pd.DataFrame(results).to_csv('results_v2.csv', index=False)
print("Risultati salvati nel file 'results_v2.csv'")
"""