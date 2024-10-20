import pandas as pd

# Importo il CSV delle strisciate
df = pd.read_csv('results_v2/results_v2.csv')

# Ordino i risultati in result_v2.csv per ordine decrescente di dissimilarità totale
df = df.sort_values(by=['GED', 'ABS_WGED'],
                    key=lambda x: df['GED'] + df['ABS_WGED'],
                    ascending=False)
df.to_csv('results_v2/results_v2.csv', index=False)

# DataFrame ordinato per GED decrescente
df_GED = df.sort_values(by=['GED', 'ABS_WGED'], 
                        ascending=[False, False])
df_GED.to_csv('results_v2/results_by_GED.csv', index=False)

# DataFrame ordinato per ABS_WGED decrescente
df_ABS_WGED = df.sort_values(by=['ABS_WGED', 'GED'], 
                        ascending=[False, False])
df_ABS_WGED.to_csv('results_v2/results_by_ABS_WGED.csv', index=False)