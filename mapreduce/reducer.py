#!/usr/bin/env python3
import sys

total = 0
for line in sys.stdin:
    line = line.strip()
    if '\t' in line:
        key, value = line.split('\t')
        total += int(value)

print(f"total\t{total}")
