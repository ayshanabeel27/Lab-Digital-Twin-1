import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

df = pd.read_csv("sample_data.csv")

X = df[
[
    "cpu_pct",
    "cpu_core_avg",
    "ram_pct",
    "disk_pct",
    "net_sent",
    "net_received",
    "process_count"
]
]

y = df["health_score"]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

pickle.dump(
    model,
    open("model.pkl", "wb")
)

print("Model trained and saved")