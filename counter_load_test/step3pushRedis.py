#!/usr/bin/env python

import redis
import time
import threading

keyname = "testkey"

def push_redis(threadId):
    counter = 0
    r = redis.Redis(host='localhost', port=6379, db=0)

    start = time.time()
    lapse = 0

    while lapse < 10:
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
    r.set(keyname, "0")

    threads = []
    for i in range(0, 20):
        t = threading.Thread(target=push_redis, args=(i,))
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
