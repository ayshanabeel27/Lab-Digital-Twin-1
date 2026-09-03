from predictor import predict_health

sample = {
    "computer_id": "PC002",
    "cpu_pct": 95,
    "cpu_core_avg": 90,
    "ram_pct": 92,
    "disk_pct": 88,
    "net_sent": 300,
    "net_received": 250,
    "process_count": 280
}

result = predict_health(sample)

print(result)