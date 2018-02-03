a = list(raw_input(''))
g = int(raw_input(''))
n = []
for i in a:
    x = ord(i) + g
    if (x > 90):
        x -= 26
    n.append(x)

print ''.join(map(chr, n))

