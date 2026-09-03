import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from collector import collect_telemetry


def test_collect_telemetry():

    data = collect_telemetry()

    assert "computer_id" in data
    assert "room_id" in data
    assert "timestamp" in data

    assert "cpu_pct" in data
    assert "cpu_per_core" in data

    assert "ram_pct" in data
    assert "ram_used_gb" in data
    assert "ram_available_gb" in data

    assert "disk_pct" in data

    assert "net_sent_mb" in data
    assert "net_recv_mb" in data

    assert "process_count" in data


if __name__ == "__main__":
    test_collect_telemetry()
    print("Telemetry collector test passed.")