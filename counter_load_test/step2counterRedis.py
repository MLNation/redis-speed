#!/usr/bin/env python
import redis
import time
counter = 0
r = redis.Redis(host='localhost', port=6379, db=0)
keyname = "testkey"
r.set(keyname, "0")

start = time.time()
while counter < 50000:
    r.incr(keyname)
    counter += 1
end = time.time()
lapse = end - start

redisCount = r.get(keyname)
print("lapsed time", lapse)
print("Memory counter value", counter)
print("Redis counter value", redisCount.decode('utf-8'))
print("Memory counter speed {} QPS".format(counter / lapse))
