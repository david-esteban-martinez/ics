#!/usr/bin/env python
import sys
# Directorio con los archivos de temperaturas
# Vamos linea a linea imprimiendo por stdout las temperaturas
for line in sys.stdin:
        data = line.split()
        temp1 = float(data[5])
        temp2 = float(data[6])
        if temp1 > 100 or temp1 < -100:
            data[5] = "0"
        if temp2 > 100 or temp2 < -100:
            data[6] = "0"
        # name=name[2].split('.')[0]
        print '%s\t%s\t%s' % (data[0], data[5], data[6])