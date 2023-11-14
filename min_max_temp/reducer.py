#!/usr/bin/env python
import sys
max_temp = 27
min_temp = -1
current_station = ""
for line in sys.stdin:
    data = line.split()
    name = data[0]
    if current_station == "":
        current_station=name
    if current_station != name:
        print '%s\t%s\t%s' % (current_station, max_temp,min_temp)
        current_station = name
        max_temp = 27
        min_temp = -1
    value1 = float(data[1])
    value2 = float(data[2])
    if value1 > max_temp:
        max_temp = value1
    if value2 < min_temp:
        min_temp = value2
print '%s\t%s\t%s' % (current_station, max_temp,min_temp)

