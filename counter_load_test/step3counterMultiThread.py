#!/usr/bin/env python

import redis
import time
import threading

keyname = "testkey"

def push_redis(threadId, records):
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

    print("thread ID {}, lapsed time {}, memory counter value {}, memory counter speed {}".format(
        threadId,
        lapse,
        counter,
        counter / lapse))

def push_multi():
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.delete(keyname)
    r.set(keyname, "0")

    threads = []
    total = 1000000
    threadCount = 5

    for i in range(0, threadCount):
        t = threading.Thread(target=push_redis, args=(i, total // threadCount))
        threads.append(t)
    start = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end = time.time()
    lapse = end - start

    redisCount = int(r.get(keyname).decode('utf-8'))
    print("Redis counter value", redisCount)
    print("lapse time", lapse)
    print("Redis speed {:,} QPS".format(redisCount / lapse))


push_multi()
