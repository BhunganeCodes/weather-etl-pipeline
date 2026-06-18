import pandas as pd
from datetime import datetime

def transform_weather(data):

    current = data["current"]

    transformed = {
        "timestamp": datetime.now(),
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "precipitation": current["precipitation"],
        "cloud_cover": current["cloud_cover"],
        "wind_speed": current["wind_speed_10m"],
        "wind_direction": current["wind_direction_10m"]
    }

    return pd.DataFrame([transformed])