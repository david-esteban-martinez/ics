#!/usr/bin/env python

import os
import sys
# Directorio con los archivos de temperaturas
# Vamos linea a linea imprimiendo por stdout las temperaturas
for line in sys.stdin:
    # file_name = os.environ['map_input_file']
    try:
        file_name = os.environ['mapreduce_map_input_file']
    except KeyError:
        file_name = os.environ['map_input_file']
    data = line.split()
    temp1 = float(data[5])
    temp2 = float(data[6])
    if temp1 > 100 or temp1 < -100:
        data[5] = "0"
    if temp2 > 100 or temp2 < -100:
        data[6] = "0"
    # name=name[2].split('.')[0]
    # s1 = file_name.split('/')
    # file_name = s1[-1]

    print '%s\t%s\t%s' % (file_name, data[5], data[6])