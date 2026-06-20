from extract import fetch_weather
from transform import transform_weather
from load import load_to_database
from export_data import export_data

def run_pipeline():

    print("Extracting data...")
    data = fetch_weather()

    print("Transforming data...")
    df = transform_weather(data)

    print("Loading data to database...")
    load_to_database(df)

    print("Saving data to csv...")
    export_data(df)

    print("Pipeline Completed!")
    

if __name__ == "__main__":
    run_pipeline()