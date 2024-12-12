import numpy as np
import pandas as pd
import difflib as dl

# Generazione 'stats_first_3_movements', in cui si raggruppano i tripli spostamenti della giornata assegnando ad ognuno il numero di volte che si verifica
movements = pd.read_csv('first3mov/first_3_movements.csv')

_3movements_counter = {}

for day in movements.iloc[:, 0].unique():
    df_day = movements[movements.iloc[:, 0] == day] # Considero solo le tuple di giorno 'day'
    for _, record in df_day.iterrows():
        if (day, record[2]) not in _3movements_counter:
            _3movements_counter[(day, record[2])] = 1
        else:
             _3movements_counter[(day, record[2])] += 1

result_df = pd.DataFrame([
    {'date': key[0], '3_movements': key[1], 'counter': value}
    for key, value in _3movements_counter.items()
])

result_df = result_df.sort_values(by=[result_df.columns[0], result_df.columns[2]], ascending=[True, False])

result_df.to_csv('first3mov/stats_first_3_movements.csv', index=False)


# -------------------------------------------------------------------------------------------------------------------- #


# Analisi file: stats_first_3_movements.csv
df = pd.read_csv('../results/2018/flussi/3_clusters/2018_WEIGHT_clustering.csv')
df_stats = pd.read_csv('first3mov/stats_first_3_movements.csv')

_3movements_counter_cluster = {}

# Per le giornate appartenenti allo stesso cluster, calcolo il numero di volte che compare ogni triplo spostamento

for cluster in range(0, 3): # Situazione in cui i cluster sono 3 ed etichettati con un numero in [0, 2]
    df_cluster = df[df.iloc[:, 1] == cluster].iloc[:, 0]
    for date in df_stats.iloc[:, 0].unique():
        if (df_cluster == date).any():
            print(date)
            df_stats_date = df_stats[df_stats.iloc[:, 0] == date]
            for _, record in df_stats_date.iterrows():
                if (cluster, record[1]) not in _3movements_counter_cluster:
                    _3movements_counter_cluster[(cluster, record[1])] = record[2]
                else:
                    _3movements_counter_cluster[(cluster, record[1])] += record[2]

result_df_cluster = pd.DataFrame([
    {'cluster': key[0], '3_movements': key[1], 'counter': value}
    for key, value in _3movements_counter_cluster.items()
])

result_df_cl0 = result_df_cluster[result_df_cluster.iloc[:, 0] == 0]
result_df_cl0 = result_df_cl0.sort_values(by=[result_df_cl0.columns[0], result_df_cl0.columns[2]], ascending=[True, False])
result_df_cl0.iloc[:, 2] = result_df_cl0.iloc[:, 2] / (sum(result_df_cl0.iloc[:, 2]))

result_df_cl1 = result_df_cluster[result_df_cluster.iloc[:, 0] == 1]
result_df_cl1 = result_df_cl1.sort_values(by=[result_df_cl1.columns[0], result_df_cl1.columns[2]], ascending=[True, False])
result_df_cl1.iloc[:, 2] = result_df_cl1.iloc[:, 2] / (sum(result_df_cl1.iloc[:, 2]))

result_df_cl2 = result_df_cluster[result_df_cluster.iloc[:, 0] == 2]
result_df_cl2 = result_df_cl2.sort_values(by=[result_df_cl2.columns[0], result_df_cl2.columns[2]], ascending=[True, False])
result_df_cl2.iloc[:, 2] = result_df_cl2.iloc[:, 2] / (sum(result_df_cl2.iloc[:, 2]))

# Separazione i risultati relativi alle occorrenze dei tripli spostamenti: un file per ogni cluster
result_df_cl0.to_csv('first3mov/CL0_first_3_movements.csv', index=False)
result_df_cl1.to_csv('first3mov/CL1_first_3_movements.csv', index=False)
result_df_cl2.to_csv('first3mov/CL2_first_3_movements.csv', index=False)

