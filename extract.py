import requests

def fetch_weather():

    latitude = -20.876
    longitude = 89.987

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}"
        f"&longitude={longitude}"
        f"&current="
        f"temperature_2m,"
        f"relative_humidity_2m,"
        f"precipitation,"
        f"cloud_cover,"
        f"wind_speed_10m,"
        f"wind_direction_10m"
    )

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Failed to fetch the weather data.")
    
    return response.json()