# feature_extractor.py

def extract_features(data):

    return [
        data["cpu_pct"],
        data["cpu_core_avg"],
        data["ram_pct"],
        data["disk_pct"],
        data["net_sent"],
        data["net_received"],
        data["process_count"]
    ]