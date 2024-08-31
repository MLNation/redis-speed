#!/usr/bin/env python
import random
import time

def genRandomLatLong():
    result = []
    for i in range(0, 1000 * 1000):
        result.append((i, random.uniform(-180, 180), random.uniform(-90, 90)))
    return result

start = time.time()
lapse = 0

counter = 0
for id, lat, long in genRandomLatLong():
    counter += 1
    if counter % 100000 == 0:
        print("counter", counter)

end = time.time()
lapse = end - start

print("lapsed time", lapse)
print("Memory counter value", counter)
print("Memory counter speed {:,} QPS".format(counter / lapse))
