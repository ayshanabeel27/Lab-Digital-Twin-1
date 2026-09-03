def calculate_health(data):

    score = 100

    score -= data["cpu_pct"] * 0.20
    score -= data["ram_pct"] * 0.15
    score -= data["disk_pct"] * 0.10

    score -= min(data["process_count"], 200) * 0.05

    return round(max(score, 0), 2)