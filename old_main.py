from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load trained ML model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI(
    title="AgriPriceRisk Prediction API",
    version="1.1.0",
    description="Predict agricultural price risk using IoT sensor data and a trained ML model."
)

# Input schema for IoT sensor data
class SensorData(BaseModel):
    crop: str
    temperature: float
    humidity: float
    rainfall: float
    soil_moisture: float

@app.get("/")
def root():
    return {"message": "Welcome to the AgriPriceRisk IoT-enabled API!"}

@app.post("/predict")
def predict(data: SensorData):
    """
    Predict agricultural price risk using IoT sensor data.
    """

    # Prepare features in the correct format
    X = np.array([[data.temperature, data.humidity, data.rainfall, data.soil_moisture]])

    # Predict using trained model
    y_pred = model.predict(X)
    risk_score = float(y_pred[0])

    # Interpret the prediction
    if risk_score < 25:
        risk_level = "Low"
    elif risk_score < 50:
        risk_level = "Medium"
    else:
        risk_level = "High"

    return {
        "crop": data.crop,
        "temperature": data.temperature,
        "humidity": data.humidity,
        "rainfall": data.rainfall,
        "soil_moisture": data.soil_moisture,
        "predicted_risk_score": round(risk_score, 2),
        "risk_level": risk_level
    }
