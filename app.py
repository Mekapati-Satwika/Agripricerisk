from fastapi import FastAPI
from sensors import read_sensor_data
from agroformer import AgroFormer
from agroscope import AgroScope
import torch

app = FastAPI()
model = AgroFormer()
reasoner = AgroScope()

@app.get("/")
def root():
    return {"message": "Agri Price Risk Early Warning API Running"}

@app.get("/predict")
def predict():
    data = read_sensor_data()
    inputs = torch.tensor([[data["temperature"], data["humidity"], data["soil_moisture"]]], dtype=torch.float32)
    risk_score = float(model(inputs).item())
    explanation = reasoner.explain(data)
    return {"sensor_data": data, "risk_score": round(risk_score, 3), "explanation": explanation}
