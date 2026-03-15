from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

MODEL_PATH = "models/churn_model.pkl"

model = joblib.load(MODEL_PATH)


@app.get("/")
def home():
    return {"message": "Churn Prediction API Running"}


@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    if prediction[0] == 1:
        result = "Customer will churn"
    else:
        result = "Customer will stay"

    return {"prediction": result}