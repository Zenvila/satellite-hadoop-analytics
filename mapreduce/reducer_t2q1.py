#!/usr/bin/env python3
import sys

sensors = set()
for line in sys.stdin:
    key, _ = line.strip().split('\t')
    sensors.add(key)

print(f"Unique ISS Sensors\t{len(sensors)}")
