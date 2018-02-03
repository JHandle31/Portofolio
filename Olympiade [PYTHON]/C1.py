#Recursion training

dics = {}
h = {}
x = raw_input()
for i in range(int(x)-1):
    z = raw_input('')
    if(len(str(z)) <= 0):
        break
    x = z.split(' ')
    if dics.has_key(x[0]):
        dics[x[0]] += [x[1]]
    else:
        dics[x[0]] = [x[1]]

    if dics.has_key(x[1]):
        dics[x[1]] += [x[0]]
    else:
        dics[x[1]] = [x[0]]

smallest = 5000
branch = 0

def weight(start,path=[]):
    global tot
    path = path + [start]
    for i in dics[start]:
        if i not in path:
            tot += 1
            x = weight(i,path)
        else:
            paths.append(path)
    return paths
for xa in dics:
    paths = []
    tot = 0
    choose = xa

    x = weight(choose)

    biggest = 0
    for i in dics[choose]:
        heaviest = 0
        for a in x:
            if i in a:
                heaviest += 1
        if heaviest > biggest:
            biggest = heaviest
    if h.has_key(biggest):
        h[biggest] += [xa]
    else:
        h[biggest] = [xa]

        
    if biggest < smallest:
        smallest = biggest
        branch = xa

if len(h[smallest]) > 1:
    print h[smallest][0],h[smallest][1]
else:
    print h[smallest][0]

