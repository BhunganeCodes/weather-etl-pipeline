import pandas as pd
from datetime import datetime
from extract import fetch_weather

def transform_weather(data):

    current = data["current_weather"]

    transformed = {
        "timestamp": datetime.now(),
        "temperature": current["temperature"],
        "windspeed": current["windspeed"],
        "weathercode": current["weathercode"]
    }

    return pd.DataFrame([transformed])

data = fetch_weather()
print(transform_weather(data))