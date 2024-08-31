#!/usr/bin/env python

import redis
import time
from multiprocessing import Process
import random

keyname = "testkeyGeo4"

def genRandomLongLat(suffix, total):
    result = []
    for i in range(0, total):
        result.append((f"{suffix}{i}", random.uniform(-180, 180), random.uniform(-60, 60)))
    return result


def push_redis(processId, randomLatLong):
    counter = 0
    r = redis.Redis(host='localhost', port=6379, db=0)

    start = time.time()

    for id, long, lat in randomLatLong:
        r.geoadd(keyname, (long, lat, id))
        counter += 1

    end = time.time()
    lapse = end - start

    print("Process ID {}, lapsed time {}, memory counter value {}, memory counter speed {}".format(
        processId,
        lapse,
        counter,
        counter / lapse))

def push_multi():
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.delete(keyname)

    processes = []
    total = 1000000
    processCount = 5
    for i in range(0, processCount):
        randomLatLong = genRandomLongLat(f"{i}", total // processCount)
        t = Process(target=push_redis, args=(i, randomLatLong))
        processes.append(t)
    start = time.time()
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    end = time.time()
    lapse = end - start

    redisCount = r.zcard(keyname)
    print("Redis counter value", redisCount)
    print("lapse time", lapse)
    print("Redis speed {:,} QPS".format(redisCount / lapse))


if __name__ == '__main__':
    push_multi()
