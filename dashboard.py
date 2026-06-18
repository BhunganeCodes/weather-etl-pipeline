import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("data/weather.db")

df = pd.read_sql(
    "SELECT * FROM weather_data",
    conn
)

conn.close()

df["timestamp"] = pd.to_datetime(df["timestamp"])

plt.figure(figsize=(12,6))

plt.plot(
    df["timestamp"],
    df["temperature"],
    label="Temperature"
)

plt.plot(
    df["timestamp"],
    df["humidity"],
    label="Humidity"
)

plt.legend()

plt.title("Weather Trends")

plt.xlabel("Time")

plt.ylabel("Value")

plt.show()