from fastapi import FastAPI
from pydantic import BaseModel

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
    return {
        "cpu": data.cpu,
        "ram": data.ram,
        "temperature": data.temp
    }