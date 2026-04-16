#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if line.startswith("Timestamp"):
        continue
    parts = line.split(",")
    if len(parts) >= 7:
        sat_name = parts[2].strip()
        sensor = parts[6].strip()
        if "METEOR" in sat_name:
            print(f"{sensor}\t1")
