import requests

def fetch_weather():

    latitude = -20.876
    longitude = 89.987

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}"
        f"&longitude={longitude}"
        f"&current_weather=true"
    )

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Failed to fetch the weather data.")
    
    return response.json()