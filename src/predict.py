import joblib
import pandas as pd

MODEL_PATH = "../models/churn_model.pkl"

def predict_churn():

    print("Loading trained model...")

    model = joblib.load(MODEL_PATH)

    # Example new customer data
    data = {
        "age": [30],
        "monthly_bill": [75],
        "contract_type": [0],
        "support_calls": [3]
    }

    df = pd.DataFrame(data)

    prediction = model.predict(df)

    if prediction[0] == 1:
        print("Prediction: Customer will churn")
    else:
        print("Prediction: Customer will stay")


if __name__ == "__main__":
    predict_churn()