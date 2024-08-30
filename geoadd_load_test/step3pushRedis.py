#!/usr/bin/env python

import redis
import time
import threading
import random

keyname = "testGeo2"

def genRandomLongLat(suffix, total):
    result = []
    for i in range(0, total):
        result.append((f"{suffix}{i}", random.uniform(-180, 180), random.uniform(-60, 60)))
    return result


def push_redis(threadId, randomLatLong):
    counter = 0
    r = redis.Redis(host='localhost', port=6379, db=0)

    start = time.time()

    for id, long, lat in randomLatLong:
        r.geoadd(keyname, (long, lat, id))
        counter += 1

    end = time.time()
    lapse = end - start

    print("thread ID {}, lapsed time {}, memory counter value {}, memory counter speed {}".format(
        threadId,
        lapse,
        counter,
        counter / lapse))

def push_multi():
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.delete(keyname)

    threads = []
    threadCount = 5
    total = 1000000
    for i in range(0, threadCount):
        randomLatLong = genRandomLongLat(f"{i}", total//threadCount)
        t = threading.Thread(target=push_redis, args=(i,randomLatLong))
        threads.append(t)
    start = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end = time.time()
    lapse = end - start

    redisCount = r.zcard(keyname)

    print("Redis counter value", redisCount)
    print("lapse time", lapse)
    print("Redis speed {:,} QPS".format(redisCount / lapse))
    assert redisCount == total, f"Redis count {redisCount} not equal to total {total}"


push_multi()
