#!/usr/bin/env python

import sys

first = True
header = list()
#how do i get the wine type????
for line in sys.stdin:
    if first:
        header = line.strip().split()
        continue
    line = line.strip()  # Remove leading and trailing whitespace
    parts = line.split()  # Split the line into parts based on spaces
    for header_item, item in header, parts:
        print '%s:%s\t%s' % (wine_type,header_item, item)

