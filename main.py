import pandas as pd         
import networkx as nx   

from percentage_matrix_methods import *
from ged import *
from graph import Graph
from matrix import Matrix
from distanceBetwPOIs import Haversine

# Crea un dizionario con numero del POI come chiave e (latitudine, longitudine) come valori
poi_coords = {}

# Leggo il CSV dei POI e le coordinate
df_poi = pd.read_csv('poi_info.csv')

for i, row in df_poi.iterrows():
    poi_id = row['poi_id']
    lat = row['latitude']
    long = row['longitude']
    poi_coords[poi_id] = (lat, long)

# Test calcolo della distanza tra due punti avendo le coordinate
#print("*Test Haversine* Distanza Arena - Casa di Giulietta = ", Haversine.haversine(poi_coords, 49, 61) , "km\n")

# Importo il CSV delle strisciate
df = pd.read_csv('log_veronaCard.csv')

POIs = sorted(df.iloc[:, 4].unique())

# Mantengo tutte le tuple escludendo l'anno 2020
df_2 = df[(df.iloc[:, 0] >= '2014-01-01') & (df.iloc[:, 0] <= '2019-12-31')]

unique_dates = sorted(df_2.iloc[:, 0].unique())

graphs = {}

for date in unique_dates:
    df_date = df_2[df_2.iloc[:, 0] == date]
    graphs[date] = Graph.get_graph(df_date)

results = []

# Confronto ogni coppia di grafi presente nel dataset e salvo i risultati in un csv
with open('results.csv', 'w') as file:
    for i in range(len(unique_dates)):
        for j in range(i + 1, len(unique_dates)):
            date1 = unique_dates[i]
            date2 = unique_dates[j]
            graph1 = graphs[date1]
            graph2 = graphs[date2]

            approx_ged = get_ged(graph1, graph2)
            abs_wGed = get_absolute_weighted_ged(graph1, graph2)
            rel_wGed = round(get_relative_weighted_ged(graph1, graph2))

            print(f'{date1}, {date2}: {rel_wGed}')

            results.append({
                'date1': date1,
                'date2': date2, 
                'GED': approx_ged,
                'ABS_WGED': abs_wGed,
                'REL_WGED': rel_wGed
            })
#results_df = pd.DataFrame(results).to_csv('results.csv', index=False)
print("Risultati salvati nel file 'results.csv'")