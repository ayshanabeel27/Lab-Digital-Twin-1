import pickle
import os

from feature_extractor import extract_features
from health_score import calculate_health

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(
    open(os.path.join(BASE_DIR, "model.pkl"), "rb")
)

def predict_health(data):

    features = extract_features(data)

    predicted_score = model.predict(
        [features]
    )[0]

    health_score = calculate_health(data)

    if health_score > 80:
        status = "Healthy"

    elif health_score > 50:
        status = "Warning"

    else:
        status = "Critical"

    return {
        "computer_id": data["computer_id"],
        "health_score": round(health_score, 2),
        "predicted_score": round(predicted_score, 2),
        "status": status
    }