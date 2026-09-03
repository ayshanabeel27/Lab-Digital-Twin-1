import psutil
from datetime import datetime, timezone

from config import COMPUTER_ID, ROOM_ID, DISK_PATH


def collect_telemetry():
    """
    Collect current telemetry from the computer.
    Returns the telemetry as a Python dictionary.
    """

    # CPU
    cpu_pct = psutil.cpu_percent(
        interval=1,
        percpu=False
    )

    cpu_per_core = psutil.cpu_percent(
        interval=None,
        percpu=True
    )

    # RAM
    memory = psutil.virtual_memory()

    # Disk usage
    disk = psutil.disk_usage(DISK_PATH)

    # Disk I/O
    disk_io = psutil.disk_io_counters()

    # Network
    network = psutil.net_io_counters()

    # Process count
    process_count = len(psutil.pids())

    # Boot time
    boot_timestamp = datetime.fromtimestamp(
        psutil.boot_time(),
        timezone.utc
    ).isoformat()

    telemetry = {
        "computer_id": COMPUTER_ID,
        "room_id": ROOM_ID,

        "timestamp": datetime.now(
            timezone.utc
        ).isoformat(),

        "cpu_pct": round(cpu_pct, 2),

        "cpu_per_core": [
            round(value, 2)
            for value in cpu_per_core
        ],

        "ram_pct": round(
            memory.percent,
            2
        ),

        "ram_used_gb": round(
            memory.used / (1024 ** 3),
            2
        ),

        "ram_available_gb": round(
            memory.available / (1024 ** 3),
            2
        ),

        "disk_pct": round(
            disk.percent,
            2
        ),

        "disk_read_mb": round(
            disk_io.read_bytes / (1024 ** 2),
            2
        ),

        "disk_write_mb": round(
            disk_io.write_bytes / (1024 ** 2),
            2
        ),

        "net_sent_mb": round(
            network.bytes_sent / (1024 ** 2),
            2
        ),

        "net_recv_mb": round(
            network.bytes_recv / (1024 ** 2),
            2
        ),

        "process_count": process_count,

        "boot_time": boot_timestamp
    }

    return telemetry