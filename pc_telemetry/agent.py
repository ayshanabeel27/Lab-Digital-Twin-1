import json
import time
import urllib.request

from collector import collect_telemetry


INTERVAL_SECONDS = 5
BACKEND_URL = "http://127.0.0.1:8000/telemetry"


def send_telemetry(data):
    payload = json.dumps(data).encode("utf-8")

    request = urllib.request.Request(
        BACKEND_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(request) as response:
        return response.read().decode("utf-8")


def main():
    print("PC Telemetry Agent started.")
    print(f"Collecting telemetry every {INTERVAL_SECONDS} seconds...")
    print("Press Ctrl+C to stop.\n")

    while True:
        try:
            data = collect_telemetry()

            print(json.dumps(data, indent=2))

            response = send_telemetry(data)
            print("Backend response:", response)

            print("-" * 60)

            time.sleep(INTERVAL_SECONDS)

        except KeyboardInterrupt:
            print("\nPC Telemetry Agent stopped.")
            break

        except Exception as e:
            print(f"Telemetry error: {e}")
            time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    main()