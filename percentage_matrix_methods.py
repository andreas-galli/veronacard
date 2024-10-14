# Implementazione calcolo della differenza percentuale tra gli spostamenti tra i vari POI in due giornate differenti
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt   
import seaborn as sns     
import requests 

def abs_to_rev(m):
    sum = m.sum().sum()
    if sum != 0:
        return m / sum
    else:
        return m

def get_percentage_diff_matrix(m1, m2):
    m1 = abs_to_rev(m1)
    m2 = abs_to_rev(m2)
    return (m1 - m2) * 100

def total_percentage_diff(m1, m2):
    m_abs = np.abs(get_percentage_diff_matrix(m1, m2))
    return (m_abs.sum().sum())

def get_matrices_percentage_diff_table(m1, m2):
    data = []
    m1 = abs_to_rev(m1)
    m2 = abs_to_rev(m2)
    for row in m1.index:
        for col in m1.columns:
            if row != col:
                weight1 = m1.at[row, col] / m1.sum().sum()
                weight2 = m2.at[row, col] / m2.sum().sum()
                variation = (abs(weight2 - weight1))
                data.append([row, col, round(weight1 * 100, 2), round(weight2 * 100, 2), round(variation * 100, 2)])
    df = pd.DataFrame(data, columns=['POI Partenza', 'POI Destinazione', 'Peso G1 (%)', 'Peso G2 (%)', '% variazione'])
    pd.set_option('display.max_rows', None)
    print(df)

def get_matrices_percentage_diff_table_fig(m1, m2, date1, date2):
    m = get_percentage_diff_matrix(m1, m2)

    # Aggiungo alla mask le celle aventi 0 come valore in una delle due matrici o entrambe (comprese i == j)
    mask = (m1 == 0) | (m2 == 0)

    plt.figure(figsize=(16, 10))
    plt.subplots_adjust(left=0.2)

    heatmap = sns.heatmap(round(m, 2), annot=True, cmap='coolwarm', center=0,
                          cbar_kws={"label": "Differenza Percentuale"}, mask=mask)

    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if i == j or (m1.iloc[i, j] == 0 and m2.iloc[i, j] == 0): 
                heatmap.add_patch(plt.Rectangle((j, i), 1, 1, color='white', alpha=0))
            elif m1.iloc[i, j] == 0 or m2.iloc[i, j] == 0:
                heatmap.add_patch(plt.Rectangle((j, i), 1, 1, color='black', alpha=1))
                heatmap.text(j + 0.5, i + 0.5, round(m.iloc[i, j], 2), ha='center', va='center', color='white')

    plt.title(f"Variazione % degli spostamenti riscontrata il giorno {date1} "
              f"({m1.sum().sum()} spostamenti) rispetto al giorno {date2} "
              f"({m2.sum().sum()} spostamenti)\n\n{get_weather_by_date(date1)}\n{get_weather_by_date(date2)}\n", fontweight='bold', fontsize='12')
    plt.xlabel("POI Destinazione", fontweight='bold', fontsize='12')
    plt.ylabel("POI Partenza", fontweight='bold', fontsize='12')
    plt.show()

def get_weather_by_date(date):
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Verona/{date}/{date}?unitGroup=metric&key=RSG69VW7PDL5DU52KB9V8WSLB&contentType=json'

    """
    # API Request
    response = requests.get(url)

    weather = ''

    if response.status_code == 200:
        data = response.json()

        # Estraggo il valore di 'description' e 'precip' per avere un'idea generale sulla giornata
        if 'days' in data and len(data['days']) > 0:
            day = data['days'][0]
            
            description = day.get('description', 'Descrizione non disponibile')
            mm = day.get('precip', 'Dati sulle precipitazioni non disponibili')

            weather = f"{date}: {description}, precipitazioni (mm): {mm}"
            print(weather)
        else:
            print("Dati sul meteo non disponibili.")
    else:
        print("Error ", response.status_code)
    return weather
    """
    
