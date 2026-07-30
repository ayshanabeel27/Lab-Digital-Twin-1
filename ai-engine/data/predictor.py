import pickle

from health_score import calculate_health

model = pickle.load(
    open("model.pkl", "rb")
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