import pandas as pd

INPUT_PATH = "../data/processed/clean_data.csv"
OUTPUT_PATH = "../data/processed/ml_ready_data.csv"


def preprocess_data():

    print("Loading processed dataset...")

    df = pd.read_csv(INPUT_PATH)

    print("Dataset shape:", df.shape)

    # Handle missing values
    df = df.dropna()

    # Convert categorical column to numeric
    df["contract_type"] = df["contract_type"].map({
        "monthly": 0,
        "yearly": 1
    })

    print("Data preprocessing completed")

    df.to_csv(OUTPUT_PATH, index=False)

    print("ML ready dataset saved")


if __name__ == "__main__":
    preprocess_data()