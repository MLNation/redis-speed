step1geo.py: generate a list of random geo coordinates in memory using a function that yields result one at a time (without Redis)

step1geoB.py: generate a list of random geo coordinates in memory using a function that returns an array of random coordinates (without Redis)

step2geoRedis.py: insert a list of random geo coordinates to Redis with a single thread

step3geoMultiThread.py: insert a list of random geo coordinates to Redis with multiple threads

step4geoMultiProcess.py: insert a list of random geo coordinates to Redis with multiple processes
