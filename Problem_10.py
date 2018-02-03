import math,time
number = 2000000
total = 0
allTrue = True
now = time.time()
for i in range(2,int(number)):
    
    for j in range(2,int(math.sqrt(i))):
        if i % j == 0:
            allTrue = False
            break

    if allTrue == True:
        total += i
    allTrue = True
print total
print time.time() - now
