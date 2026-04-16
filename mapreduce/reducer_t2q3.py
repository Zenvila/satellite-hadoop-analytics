#!/usr/bin/env python3
import sys

total = 0.0
count = 0
for line in sys.stdin:
    _, value = line.strip().split('\t')
    total += float(value)
    count += 1

if count > 0:
    print(f"Avg Sea Surface Temp\t{total/count:.4f}")
