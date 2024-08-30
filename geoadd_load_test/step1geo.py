#!/usr/bin/env python
import random
import time

def genRandomLatLong():
    i = 0
    id = i
    i += 1
    yield id, random.uniform(-180, 180), random.uniform(-90, 90)

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
print("Last lat, long", lat, long)
