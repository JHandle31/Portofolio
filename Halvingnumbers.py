import sys
number = float(sys.argv[1])
total = number
times = int(sys.argv[2])
try:
    print sys.argv[3]
    x = 1
    while total != float(sys.argv[3]):
        
        total += number / (2**x)
        x += 1
    print x
except:
        
    print number,times

    for i in range(1,times+1):
        localNum = number / (2 ** i)
        total += localNum
        
        print localNum

    print total
