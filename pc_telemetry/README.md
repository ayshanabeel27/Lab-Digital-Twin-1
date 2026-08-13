# PC Telemetry Agent

This module collects live telemetry from laboratory computers.

## Current telemetry

The agent collects:

- Computer ID
- Room ID
- Timestamp
- CPU utilization
- Per-core CPU utilization
- RAM utilization
- RAM used
- RAM available
- Disk utilization
- Disk read
- Disk write
- Network sent
- Network received
- Process count
- Boot time

## Architecture

PC
→ Python Telemetry Agent
→ JSON Telemetry
→ MQTT (next integration stage)
→ Backend
→ Database

## Installation

Create a virtual environment:

```bash
python -m venv venv