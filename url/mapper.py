#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    parts = line.split()
    user_id = parts[2]
    url = parts[3]
    if url.endswith('.ps'):
        print 'user:%s\t%s' % (user_id, 1)
    print 'url:%s\t%s' % (url, 1)