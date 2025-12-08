from typing import Dict
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# Model path relative to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.joblib")

# Load model bundle (pipeline + feature names)
bundle = joblib.load(MODEL_PATH)
model = bundle["model"]
FEATURE_NAMES = bundle["feature_names"]

app = FastAPI(title="APS Failure Prediction API")


class APSData(BaseModel):
    features: Dict[str, float]


@app.get("/")
def health_check():
    return {"status": "ok", "detail": "APS failure prediction API is running"}


@app.post("/predict")
def predict(payload: APSData):
    df = pd.DataFrame([payload.features])
    df = df.reindex(columns=FEATURE_NAMES)  
    y_pred = model.predict(df)[0]
    y_prob = model.predict_proba(df)[0][1]
    return {
        "failure_prediction": int(y_pred),
        "failure_probability": float(y_prob)
    }
