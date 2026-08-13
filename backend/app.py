from fastapi import FastAPI
from pydantic import BaseModel

import sys
sys.path.append("../ai-engine/data")

from predictor import predict_health

app = FastAPI()

class PredictionInput(BaseModel):
    cpu: float
    ram: float
    temp: float


@app.get("/")
def home():
    return {"message": "Digital Twin Backend is Running"}


@app.post("/predict")
def predict(data: PredictionInput):

    health = predict_health(
        data.cpu,
        data.ram,
        data.temp
    )

    return {
        "health": health
    }