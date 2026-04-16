#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if line and not line.startswith("Timestamp"):
        print("total\t1")
