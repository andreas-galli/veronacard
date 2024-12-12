import pandas as pd      
from clustering import *
from graphs.graph_similarity import *

df = pd.read_csv('log_veronaCard.csv')
POIs = sorted(df.iloc[:, 4].unique())

cluster = pd.read_csv("../results/2018/flussi/3_clusters/2018_WEIGHT_clustering.csv") # Da adattare al csv da analizzare
cluster = cluster[cluster.iloc[:, 1] == 0].iloc[:, 0] # Da adattare al cluster analizzato

df.iloc[:, 2] = pd.to_datetime(df.iloc[:, 2], format="%d/%m/%Y %H:%M", errors='coerce').dt.strftime("%Y-%m-%d %H:%M")
df = df[df.iloc[:, 2].astype(object).str.startswith('2018')] # Da adattare all'anno analizzato
df['date'] = pd.to_datetime(df.iloc[:, 2]).dt.date

result = {}
for date in sorted(df.iloc[:, 6].unique()):
    df_date = df[df.iloc[:, 6] == date]
    for vc in df_date.iloc[:, 1]:
        if (date, vc) not in result:
            df_vc = df[df.iloc[:, 1] == vc]
            if len(df_vc.index) >= 3:
                # Seleziona i primi n POI
                n = 3
                poi_sequence = df_vc.iloc[:, 4].head(n).tolist()
                print(date, vc, poi_sequence)
                # Salva nel dizionario con chiave (data, id_vc)
                result[(date, vc)] = poi_sequence

result_df = pd.DataFrame([
    {'data': key[0], 'id_vc': key[1], 'poi_sequence': value}
    for key, value in result.items()
])

# Salva nel csv specificato i risultati, cioé il df 'result_df'
result_df.to_csv('first_3_movements.csv', index=False)
