#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if line.startswith("Timestamp"):
        continue
    parts = line.split(",")
    if len(parts) >= 8:
        sensor = parts[6].strip()
        value = parts[7].strip()
        if sensor == "Sea_Surface_Temp":
            try:
                print(f"SST\t{float(value)}")
            except:
                pass
