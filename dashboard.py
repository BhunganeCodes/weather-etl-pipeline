import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

connection = sqlite3.connect("data/weather.db")

df = pd.read_sql(
    "SELECT * FROM weather_data",
    connection
)

connection.close()

df["timestamp"] = pd.to_datetime(df["timestamp"])

plt.figure(figsize=(10, 5))

plt.plot(
    df["timestamp"],
    df["temperature"]
)

plt.title("Temperature Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Temperature")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()