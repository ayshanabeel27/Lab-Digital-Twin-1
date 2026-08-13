import pickle
import os

from health_score import calculate_health

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(
    open(os.path.join(BASE_DIR, "model.pkl"), "rb")
)


def predict_health(cpu, ram, temp):

    score = calculate_health(cpu, ram, temp)

    prediction = model.predict(
        [[cpu, ram, temp]]
    )

    if score > 80:
        status = "Healthy"

    elif score > 50:
        status = "Warning"

    else:
        status = "Critical"

    return {
        "health_score": score,
        "status": status
    }