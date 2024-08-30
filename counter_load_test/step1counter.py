#!/usr/bin/env python

import time

start = time.time()
lapse = 0

counter = 0
while counter < 50000:
    counter += 1

end = time.time()
lapse = end - start

print("lapsed time", lapse)
print("Memory counter value", counter)
print("Memory counter speed {:,} QPS".format(counter / lapse))
