#!/usr/bin/python

import os

path = "/etc"

paths=[]

i = 0
for (path, dirs, files) in os.walk(path):
    paths.append((path,dirs,files))
    print path
    print dirs
    print files
    print "----"
    i += 1
    if i >= 4:
        break

for (paths, dirs, files) in paths:
    print path
    print dirs
    print files
    print "----"
