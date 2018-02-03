def partitions(n):
    # base case of recursion: zero is the sum of the empty list
    if n == 0:
        yield []
        return
        
    # modify partitions of n-1 to form partitions of n
    for p in partitions(n-1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]
            


def pointcounter(x):
    return{
        1 : 30,
        2 : 45,
        3 : 56,
        4 : 68,
        5 : 84,
        6 : 85,
        7 : 108,
        8 : 120,
        9 : 136,
        10 : 158,
        11 : 163,
        12 : 179,
        13 : 196,
        14 : 206,
        15 : 210,
        16 : 226,
        17 : 255,
        18 : 256,
        19 : 282,
        20 : 295,
        21 : 304,
        22 : 321,
        23 : 322,
        24 : 339,
        25 : 350
    }[x]

best = 0
besta = []

for x in partitions(25):
    totalpoints = 0
    for i in x:
        totalpoints += pointcounter(i)
    totalpoints -= ((len(x)-1) * 5)
    if totalpoints > best:
        best = totalpoints
        besta = x
print best, besta
