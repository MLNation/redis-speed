#!/usr/bin/env python
import redis
import random
import time

def genRandomLongLat(suffix, total):
    result = []
    for i in range(0, total):
        result.append((f"{suffix}{i}", random.uniform(-180, 180), random.uniform(-60, 60)))
    return result

keyname = "testkeyGeo2"

r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.delete(keyname)

start = time.time()
randomLatLong = genRandomLongLat("x", 1000000)
i = 0
for id, long, lat in randomLatLong:
    #print(f"id {id}, long {long}, lat {lat}")
    r.geoadd(keyname, (long, lat, id))
    i += 1
    if i % 100000 == 0:
        print("counter", i)
end = time.time()
lapse = end - start

counter = len(randomLatLong)
redisCount = r.zcard(keyname)
print("lapsed time", lapse)
print("Memory counter value", counter)
print("Redis counter value", redisCount)
print("Memory counter speed {} QPS".format(counter / lapse))
