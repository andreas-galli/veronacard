import pandas as pd
from graphs.graph_similarity import *
from graphs.graph import Graph
from matrices.matrix import Matrix

df = pd.read_csv('log_veronaCard.csv')
POIs = sorted(df.iloc[:, 4].unique())

# Per concentrarsi su un singolo anno, mantengo le tuple di un anno specifico 
df_2 = df[(df.iloc[:, 0] >= '2016-01-01') & (df.iloc[:, 0] <= '2016-12-31')]

unique_dates = sorted(df_2.iloc[:, 0].unique())

graphs = {}

for date in unique_dates:
    df_date = df_2[df_2.iloc[:, 0] == date]
    # Generazione di ogni grafo a partire dalla sua matrice 
    graphs[date] = Graph.get_graph(Matrix.get_matrix(df_date, POIs), df_date)

results = []

# Confronto di ogni coppia di grafi presente nel dataset e salvataggio dei risultati in un csv
with open('results/2017/2017_results.csv', 'w') as file:
    for i in range(len(unique_dates)):
        for j in range(i + 1, len(unique_dates)):
            date1 = unique_dates[i]
            date2 = unique_dates[j]
            graph1 = graphs[date1]
            graph2 = graphs[date2]

            approx_ged = get_ged(graph1, graph2)
            abs_dist = get_absolute_distance(graph1, graph2)

            print(f'{date1}, {date2}: {approx_ged}')

            results.append({
                'DATE1': date1,
                'DATE2': date2, 
                'GED': approx_ged,
                'ABS_DIST': abs_dist
            })
results_df = pd.DataFrame(results).to_csv('results/2017/2017_results.csv', index=False)