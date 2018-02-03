from math import sqrt
import time


limit = 2000000
numlist = range(limit+1); numlist[1] = 0
now = time.time()
for x in xrange(2,int(sqrt(limit))+1):
    if numlist[x] > 0:
        for n in xrange(x*x, limit+1, x): numlist[n] = 0

print sum(numlist)
print time.time() - now
