import time

number = 1
i = 1
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in arr:
    number *= i
print number
now = time.time()
while True:
    allTrue = True
    for j in arr:       
        if i % j != 0:
            allTrue = False
            break
        else:
            allTrue = True
    if allTrue == True:
        print i
        print time.time() - now
        break
    i += 1
