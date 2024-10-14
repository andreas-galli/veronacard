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

# Mantengo solo le tuple di data 01/01/2019
date1 = '2018-04-07'
df1 = df[df.iloc[:, 0] == date1]

matrix1 = Matrix.get_matrix(df1, POIs)
graph1 = Graph.get_graph(df1)

date2 = '2019-09-07'
df2 = df[df.iloc[:, 0] == date2]

matrix2 = Matrix.get_matrix(df2, POIs)

graph2 = Graph.get_graph(df2)

print(f"{date1}: {matrix1.sum().sum()} people\n{date2}: {matrix2.sum().sum()} people")

print("\nGED (networkx): ", nx.graph_edit_distance(graph1, graph2, timeout=30))

print("Approx. GED: ", get_ged(graph1, graph2))

print("Absolute Weighted GED: ", get_absolute_weighted_ged(graph1, graph2))

print("Relative Weighted GED: ", round(get_relative_weighted_ged(graph1, graph2), 2))

Graph.get_graph_image([graph1, graph2], date1, date2)

