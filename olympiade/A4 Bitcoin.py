arr = []
N1 = raw_input('')
for i in range(int(N1)):
    arr.append(int(raw_input('')))
arr.append(0)
worth = 0
bitc = 0
s = -1
b = -1
i = 0
while i < (len(arr)-1):
    x = arr[i]
    for j in xrange(i , len(arr)-1):
        if(arr[j] > arr[j+1] and bitc == 1):
            s = j
            break
        elif(arr[j] < arr[j+1] and bitc == 0):
            b = j
            break
    i = j
    if(i==s):
        worth += arr[i]
        bitc = 0

    if(i==b):
        worth -= arr[i]
        bitc = 1
    i += 1
print worth

