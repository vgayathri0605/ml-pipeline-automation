import pandas as pd
import os

RAW_DATA_PATH = "../data/raw/customer_churn.csv"
PROCESSED_DATA_PATH = "../data/processed/clean_data.csv"


def load_data():
    print("Loading dataset...")

    df = pd.read_csv(RAW_DATA_PATH)

    print("Dataset loaded successfully")
    print(df.head())

    return df


def save_processed_data(df):
    print("Saving processed data...")

    os.makedirs("../data/processed", exist_ok=True)

    df.to_csv(PROCESSED_DATA_PATH, index=False)

    print("Data saved to processed folder")


if __name__ == "__main__":

    data = load_data()

    save_processed_data(data)