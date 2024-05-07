import requests


def get_schedule_from_api():
    # Zastąp 'adres_twojego_serwera' adresem Twojego serwera
    url = 'http://127.0.0.1:5000/scrape'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Błąd podczas pobierania danych:", response.status_code)
        return None


schedule = get_schedule_from_api()

if schedule:
    for day in schedule:
        print("Dzień:", day['day_of_the_week'])
        print("------------------------------")
        for event in day['events']:
            print("Czas:", event['time'])
            print("Nazwa:", event['name'])
            print("Instruktor:", event['instructor'])
            print("Poziom:", event['level'])
            print("--------------------------------")
else:
    print("Nie udało się pobrać harmonogramu.")
