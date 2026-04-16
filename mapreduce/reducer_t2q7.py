#!/usr/bin/env python3
import sys
import math

ozone = []
sst = []

for line in sys.stdin:
    key, val = line.strip().split('\t')
    if key == "Ozone_Level":
        ozone.append(float(val))
    elif key == "Sea_Surface_Temp":
        sst.append(float(val))

n = min(len(ozone), len(sst))
if n < 2:
    print("Correlation\tNot enough data")
else:
    ox = ozone[:n]
    sx = sst[:n]
    mean_o = sum(ox)/n
    mean_s = sum(sx)/n
    num = sum((ox[i]-mean_o)*(sx[i]-mean_s) for i in range(n))
    den = math.sqrt(sum((ox[i]-mean_o)**2 for i in range(n)) * sum((sx[i]-mean_s)**2 for i in range(n)))
    corr = num/den if den != 0 else 0
    print(f"Ozone vs SST Correlation\t{corr:.4f}")
