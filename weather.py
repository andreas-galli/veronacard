import requests 

def get_weather_by_date(date):
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Verona/{date}/{date}?unitGroup=metric&key=RSG69VW7PDL5DU52KB9V8WSLB&contentType=json'

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