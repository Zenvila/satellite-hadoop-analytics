#!/usr/bin/env python3
import sys

data = {}
for line in sys.stdin:
    line = line.strip()
    if line.startswith("Timestamp"):
        continue
    parts = line.split(",")
    if len(parts) >= 8:
        try:
            ts = parts[0].strip()
            sat = parts[2].strip()
            lat = float(parts[4].strip())
            sensor = parts[6].strip()
            value = float(parts[7].strip())
            key = (ts, sat)
            if key not in data:
                data[key] = {"lat": lat}
            data[key][sensor] = value
        except:
            pass

for key, vals in data.items():
    lat = vals.get("lat", 0)
    humidity = vals.get("Humidity", None)
    pressure = vals.get("Internal_Pressure", None)
    if lat > 0 and humidity is not None and pressure is not None:
        if humidity > 80 and pressure < 900:
            print(f"north_match\t1")
