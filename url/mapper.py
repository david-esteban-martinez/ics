#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()  # Remove leading and trailing whitespace
    parts = line.split()  # Split the line into parts based on spaces
    user_id = parts[2]  # Extract the user id
    url = parts[3]  # Extract the URL
    print '%s,%s\t%s' % (url,user_id, 1)

