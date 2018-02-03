xy = map(int,raw_input('').split(' '))
arr1 = list(raw_input(''))
arr1 = arr1[::-1]
arr2 = list(raw_input(''))
d = int(raw_input(''))
e = len(arr1)

if(d == 0):
    arr2 = arr1 + arr2
else:
    for i in range(d,0,-1):
        arr2.insert(i,arr1[e-1])
        e -= 1
        if(e==0):
            break

    if(d < xy[0]):
        for i in range(xy[0]-d,0,-1):
            arr2.insert(0,arr1[i-1])
print ''.join(arr2)

