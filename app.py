from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# python -m uvicorn app:app --reload
model = joblib.load("model.joblib")

class Busdata(BaseModel):
    temperature_mean_last_24h: float
    vibration_level : float
    mileage_km : float
    engine_load : float
    ambient_temp : float
    coolant_pressure : float
    battery_voltage : float

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "Hello Worlds"}


@app.post("/predict")
def predict(data: Busdata):
    data_dict = data.model_dump()
    df = pd.DataFrame([data_dict])
    prediction = model.predict(df)            
    probability = model.predict_proba(df)     

    pred_int = int(prediction[0])                                
    pred_prob = float(probability[0, pred_int])                   

    return {"failure_prediction": pred_int,
            "failure_probability": pred_prob}


