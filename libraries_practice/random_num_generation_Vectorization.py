import numpy as np
import time as t
#random number generator
random = np.random.default_rng(15)
r = random.integers(2,4,size=10)
print(r)
#vectorization
start_time = t.time()
list = range(10000)
for i in list:
    square = (i**2)
endtime = t.time()
total_time = endtime-start_time
print(f"loop time:", total_time)
start = t.time()
arr = np.arange(10000)
square = arr**2
end= t.time()
print("Vectorized time:",end -start)
