#!/usr/bin/env python

import sys
number_of_wines=1
current_key = None
current_sum = 0
key = None
wine_type = "red"
current_count=0

for line in sys.stdin:

    line = line.strip()

    key, value = line.split('\t', 1)

    try:
        value = float(value)
    except ValueError:

        continue

    if current_key == key:
        current_sum += value
        current_count+=1
    else:
        if current_key:
            current_sum = current_sum / current_count
            print '%s\t%s' % (current_key, current_sum)
        current_sum = value
        current_key = key

if current_key == key:
    current_sum = current_sum / current_count
    print '%s\t%s' % (current_key, current_sum)