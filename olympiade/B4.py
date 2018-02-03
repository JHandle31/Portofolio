import copy
puzzzle = [  ['A','B','C','C','C','C','F'],
	    ['A','B','D','D','E','E','F'],
	    ['G','G','G','G','H','H','F'],
	    ['G','G','G','G','H','H','F'],
	    ['I','I','I','J','H','H','F'],
	    ['I','I','I','J','H','H','F'],
	    ['K','K','K','L','L','L','L']
	   ]

arr = ['A','B','C','D','E','F','G','H','I','J','K','L']

def points(x):
    return { 'A' : 2,
      'B' : 2,
      'C' : 4,
      'D' : 2,
      'E' : 2,
      'F' : 6,
      'G' : 8,
      'H' : 8,
      'I' : 6,
      'J' : 2,
      'K' : 3,
      'L' : 4
      }[x]


direction = [1,-1]


def getCoordinates(d,puzzle):
    arr = []
    for x in range(len(puzzle)):
        for i in range(len(puzzle[x])):
            if puzzle[x][i] == d:
                arr.append([x,i])
    return arr

def colllisionCheck(inst,localPuzzle):
    cooarr = []
    for c in getCoordinates(inst,localPuzzle):
        for i in direction:
            if ((c[0] + i < 0) or (c[0] + i > 6)):
                i = 0
            cooarr.append(localPuzzle[c[0]+i][c[1]])
        for i in direction:
            if ((c[1] + i < 0) or (c[1] + i > 6)):
                i = 0
            cooarr.append(localPuzzle[c[0]][c[1]+i])
    cooarr = filter(lambda a : a!=inst, cooarr)
    cooarr = filter(lambda a : a!='1', cooarr)
    return cooarr

#The changing to one function which changes the (a) into 1's
#Then it returns all the letters next to the 1's
def changeToZero(dd,a):
    for i in dd:
        for j in getCoordinates(i,a):
            a[j[0]][j[1]] = '0'
    return a
            
def changeToOne(choice,a):
    for i in getCoordinates(choice,a):
        a[i[0]][i[1]] = '1'
    z = colllisionCheck('1',a)
    b = changeToZero(z,a)
    return b

def findNewOne(localPuzzle):
    x = colllisionCheck('0',localPuzzle)
    z = removeDuplicates(x)
    return z

def removeDuplicates(dad):
    newarr = []
    for inst in dad:
        if inst not in newarr:
            newarr.append(inst)
    return newarr


for i in range(5):
    x = 0
    maxtot = 0
    puzarr = []
    allComboArr = 'L'
    a = copy.deepcopy(puzzzle)
    b = changeToOne(allComboArr,a)
    allComboArr = findNewOne(b)


    a = copy.deepcopy(a)
    b = changeToOne(allComboArr[1],a)
    allComboArr = findNewOne(b)
    try:
        a = copy.deepcopy(a)
        puzarr.append(a)
        b = changeToOne(allComboArr[i],a)
        allComboArr = findNewOne(b)
    except:
        print 'out of range'
        break




    print allComboArr
    for d in a:
        print d
        for c in d:
            if c == '1':
                    x += 1
    for inst in allComboArr:
        print '%s == %s' % (inst,points(inst))
        maxtot += points(inst)
    print 'With a max of %s ' % (x)
    print 'Check this out if above 20 ####%s####' % (x+maxtot)
    print '\n'
    
