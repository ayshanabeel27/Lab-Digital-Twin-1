import json
import time

from collector import collect_telemetry


INTERVAL_SECONDS = 5


def main():
    print("PC Telemetry Agent started.")
    print(f"Collecting telemetry every {INTERVAL_SECONDS} seconds...")
    print("Press Ctrl+C to stop.\n")

    while True:
        try:
            data = collect_telemetry()

            print(json.dumps(data, indent=2))
            print("-" * 60)

            time.sleep(INTERVAL_SECONDS)

        except KeyboardInterrupt:
            print("\nPC Telemetry Agent stopped.")
            break

        except Exception as e:
            print(f"Telemetry collection error: {e}")
            time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    main()