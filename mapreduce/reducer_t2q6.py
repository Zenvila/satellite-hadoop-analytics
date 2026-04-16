#!/usr/bin/env python3
import sys
from collections import defaultdict

bins = defaultdict(int)
for line in sys.stdin:
    key, val = line.strip().split('\t')
    bins[int(key)] += int(val)

for b in sorted(bins.keys()):
    print(f"{b} to {b+10}\t{bins[b]}")

