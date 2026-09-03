from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import datetime

import sys
sys.path.append("../ai-engine/data")

from predictor import predict_health

from database import SessionLocal, engine, Base
from models import Telemetry


app = FastAPI()

Base.metadata.create_all(bind=engine)


# Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- PREDICTION ----------------

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


# ---------------- TELEMETRY ----------------

class TelemetryInput(BaseModel):
    computer_id: str
    room_id: str
    timestamp: datetime

    cpu_pct: float
    ram_pct: float
    ram_used_gb: float
    ram_available_gb: float

    disk_pct: float

    net_sent_mb: float
    net_recv_mb: float

    process_count: int


@app.post("/telemetry")
def receive_telemetry(data: TelemetryInput, db: Session = Depends(get_db)):

    telemetry = Telemetry(
        computer_id=data.computer_id,
        room_id=data.room_id,
        timestamp=data.timestamp,

        cpu_pct=data.cpu_pct,
        ram_pct=data.ram_pct,
        ram_used_gb=data.ram_used_gb,
        ram_available_gb=data.ram_available_gb,

        disk_pct=data.disk_pct,

        net_sent_mb=data.net_sent_mb,
        net_recv_mb=data.net_recv_mb,

        process_count=data.process_count
    )

    db.add(telemetry)
    db.commit()
    db.refresh(telemetry)

    return {
        "message": "Telemetry received successfully",
        "id": telemetry.id
    }