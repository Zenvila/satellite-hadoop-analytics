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
        if sensor in ("Temperature", "Atmos_Temp", "Radio_Temp"):
            try:
                temp = float(value)
                bin_low = int(temp // 10) * 10
                print(f"{bin_low}\t1")
            except:
                pass

