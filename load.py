import sqlite3

def load_to_database(df):

    connection = sqlite3.connect("data/weather.db")

    df.to_sql(
        "weather_data",
        connection,
        if_exists="append",
        index=False
    )

    connection.close()