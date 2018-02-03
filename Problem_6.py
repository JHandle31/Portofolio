
def squarenumbers(nums):
    x = 0
    for i in range(nums+1):
        x += i * i
    return x
def sumnumbers(nums):
    x = 0
    for i in range(nums + 1):
        x += i
    total = x * x
    return total

print sumnumbers(100) - squarenumbers(100)
print squarenumbers(100), sumnumbers(100)

num = 10

print 1+2+3+4+5+6+7+8+9+10
print (num * (num+1) * 0.5) * (num * (num+1) * 0.5)
