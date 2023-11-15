#!/usr/bin/env python
import os
import sys

for line in sys.stdin:
    line = line.strip()
    parts = line.split()
    user_id = os.environ['mapreduce_map_input_file']
    user_id =user_id.split('.')[1].split('/')[-1]
    url = parts[3]
    if url.endswith('.ps"'):
        print 'user:%s\t%s' % (user_id, 1)
    print 'url:%s\t%s' % (url, 1)