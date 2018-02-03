from math import sqrt

x,total,arr = 600851475143,1,[]

for i in range(1,int(sqrt(x))):
    if x % i == 0:
        arr.append(i)

for i in range(len(arr)):
    if total < x:
        total *= arr[i]

print total

