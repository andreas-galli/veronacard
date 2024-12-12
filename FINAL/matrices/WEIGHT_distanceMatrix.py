import pandas as pd
from graphs.graph_similarity import *
from matrices.matrix import Matrix

""" Generazione della matrice delle distanze usando come misura di similarità le differenze di flussi 
    (absolute_distance), usando il metodo get_GED_matrix_from_csv(...).
    La matrice delle distanze è generata a partire da un csv di risultati in cui vi è ogni coppia di date (diverse),
    tra cui è calcolata la distanza di flusso. """

# Generazione della matrice
distance_matrix = Matrix.get_WEIGHT_matrix_from_csv('results/2017/2017_results.csv')
distance_matrix.to_csv('results/2017/flussi/2018_WEIGHT_distance_matrix.csv', header=True)

# Verifico che il csv sia stato riempito correttamente
distance_matrix = pd.read_csv('results/2017/flussi/2018_WEIGHT_distance_matrix.csv', index_col=0)
print(distance_matrix)
