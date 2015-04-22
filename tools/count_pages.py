#!/usr/bin/env python2

fc = open("in.txt", "r").read()

tot = 0.0
for i in fc.split("\n"):
    if i.strip() == "":
        continue

    a = i.split(" ")
    tot += float(a[0])

print tot
