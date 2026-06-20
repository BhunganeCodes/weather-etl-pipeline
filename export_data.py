import pandas as pd
from extract import fetch_weather
from transform import transform_weather

def export_data(data):
    data.to_csv("weather_report.csv", index=False)
    print("Data exported!")

data = fetch_weather()
transformed = transform_weather(data)
export_data(transformed)
