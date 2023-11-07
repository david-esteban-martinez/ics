#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()  # Remove leading and trailing whitespace
    parts = line.split()  # Split the line into parts based on spaces
    url = parts[3]  # Extract the URL
    print '%s\t%s' % (url, 1)

