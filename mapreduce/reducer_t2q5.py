#!/usr/bin/env python3
import sys

count = 0
for line in sys.stdin:
    _, val = line.strip().split('\t')
    count += int(val)

print(f"Southern Hemisphere Matches\t{count}")

