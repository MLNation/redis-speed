#!/usr/bin/env python

import redis
import time
from multiprocessing import Process

keyname = "testkey"

def push_redis(processId, records):
    counter = 0
    r = redis.Redis(host='localhost', port=6379, db=0)

    start = time.time()
    lapse = 0

    #while lapse < 10:
    while counter < records:
        r.incr(keyname)
        counter += 1

        end = time.time()
        lapse = end - start

    print("process ID {}, lapsed time {}, memory counter value {}, memory counter speed {}".format(
        processId,
        lapse,
        counter,
        counter / lapse))

def push_multi():
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.delete(keyname)
    r.set(keyname, "0")

    processes = []
    total = 1000000
    processCount = 5
    for i in range(0, 5):
        t = Process(target=push_redis, args=(i, total // processCount))
        processes.append(t)
    start = time.time()
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    end = time.time()
    lapse = end - start

    redisCount = int(r.get(keyname).decode('utf-8'))
    print("Redis counter value", redisCount)
    print("lapse time", lapse)
    print("Redis speed {:,} QPS".format(redisCount / lapse))


if __name__ == '__main__':
    push_multi()
