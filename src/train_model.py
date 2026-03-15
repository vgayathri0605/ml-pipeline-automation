import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

DATA_PATH = "../data/processed/ml_ready_data.csv"
MODEL_PATH = "../models/churn_model.pkl"


def train_model():

    print("Loading dataset...")

    df = pd.read_csv(DATA_PATH)

    # Define features and target
    X = df.drop(["churn", "customer_id"], axis=1)
    y = df["churn"]

    print("Splitting dataset...")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Training model...")

    model = RandomForestClassifier()

    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    print("Model Accuracy:", accuracy)

    joblib.dump(model, MODEL_PATH)

    print("Model saved successfully")


if __name__ == "__main__":
    train_model()