import pandas as pd

# Importo il CSV delle strisciate
df = pd.read_csv('results/results.csv')

# Ordino i risultati per ordine decrescente di dissimilarità
"""
df = df.sort_values(by=['GED', 'ABS_WGED', 'REL_WGED'],
                    key=lambda x: df['GED'] + df['ABS_WGED'] + df['REL_WGED'],
                    ascending=False)
"""

# CSV in cui le coppie di grafi sono ordinati per distanza complessiva decrescente 
#df.to_csv('results.csv', index=False)

# DataFrame ordinato per GED decrescente
df_GED = df.sort_values(by=['GED', 'ABS_WGED', 'REL_WGED'], 
                        ascending=[False, False, False])
df_GED.to_csv('results/results_by_GED.csv', index=False)

# DataFrame ordinato per ABS_WGED decrescente
df_ABS_WGED = df.sort_values(by=['ABS_WGED', 'REL_WGED', 'GED'], 
                        ascending=[False, False, False])
df_ABS_WGED.to_csv('results/results_by_ABS_WGED.csv', index=False)

# DataFrame ordinato per REL_WGED decrescente
df_REL_WGED = df.sort_values(by=['REL_WGED', 'ABS_WGED', 'GED'], 
                        ascending=[False, False, False])
df_REL_WGED.to_csv('results/results_by_REL_WGED.csv', index=False)

# 