#!/usr/bin/env python
import sys
import os

first = True
header = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides","free sulfur dioxide",
          "total sulfur dioxide", "density", "pH", "sulphates", "alcohol", "quality"]

for line in sys.stdin:
    file_name = os.environ['mapreduce_map_input_file']
    file_name=file_name.split('-')[1].split('_')[0].split('.')[0]
    line = line.strip()
    parts = line.split(";")
    if parts.__len__()!=header.__len__():
        continue

    # wine_type = "NotYet"
    for i in  range(header.__len__()):
        print '%s:%s\t%s' % (file_name, header[i],parts[i])