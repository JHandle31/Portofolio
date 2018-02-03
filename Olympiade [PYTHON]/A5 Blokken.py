length = raw_input('')
arr1 = map(int,raw_input('').split(' '))
arr2 = map(int,raw_input('').split(' '))
matotal = 0
for i in arr1:
    for j in arr2:
        if i >= j:
            matotal += j
        elif (i>0 and j>i):
            matotal += i      
mitotal = 0
for i in arr1:
    mitotal += i
    if(i in arr2):
        arr2.remove(i)
if(len(arr2)>0):
    mitotal += sum(arr2)  
print mitotal, matotal-mitotal
