import random
def pointcounter(d):
    return{
        'AB' : 3,
        'AF' : 23,
        'AE' : 7,
        'BA' : 3,
        'BF' : 20,
        'BC' : 3,
        'CB' : 3,
        'CF' : 25,
        'CG' : 3,
        'CH' : 16,
        'CD' : 20,
        'DC' : 20,
        'DH' : 13,
        'EF' : 14,
        'EJ' : 40,
        'EI' : 16,
        'FB' : 20,
        'FC' : 25,
        'FE' : 14,
        'FJ' : 27,
        'FG' : 12,
        'GF' : 12,
        'GC' : 3,
        'GH' : 4,
        'GL' : 28,
        'GK' : 10,
        'GJ' : 30,
        'HD' : 13,
        'HG' : 4,
        'HC' : 16,
        'HL' : 9,
        'IE' : 16,
        'IJ' : 19,
        'IN' : 17,
        'IM' : 26,
        'JE' : 40,
        'JF' : 27,
        'JG' : 30,
        'JK' : 23,
        'JN' : 21,
        'JI' : 19,
        'KG' : 10,
        'KL' : 25,
        'KP' : 5,
        'KO' : 21,
        'KN' : 18,
        'KJ' : 23,
        'LH' : 9,
        'LG' : 28,
        'LK' : 25,
        'LP' : 21,
        'MI' : 26,
        'MN' : 23,
        'NI' : 17,
        'NJ' : 21,
        'NM' : 23,
        'NK' : 18,
        'NO' : 25,
        'ON' : 25,
        'OK' : 21,
        'OP' : 23,
        'PO' : 23,
        'PK' : 5,
        'PL' : 21,
        }[d]


graph = {'A' : ['B', 'E', 'F'],
             'B' : ['A', 'C', 'F'],
	     'C' : ['B','D','F','G','H'],
	     'D' : ['C','H'],
	     'E' : ['A','F','I','J'],
	     'F' : ['A','B','C','E','G','J'],
	     'G' : ['C','F','H','J','K','L'],
	     'H' : ['C','D','G','L'],
	     'I' : ['E','J','M','N'],
	     'J' : ['E','I','F','G','N', 'K'],
	     'K' : ['J','G','L', 'N', 'O', 'P'],
	     'L' : ['H','G','K','P'],
	     'M' : ['I','N'],
	     'N' : ['I','J','K','M','O'],
	     'O' : ['K','N','P'],
	     'P' : ['K','L','O']}

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

arras = ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
for ia in arras:
    x = find_all_paths(graph,'A',ia)

    best = 315
    d = 0
    for i in x:
        totalpoints = 0
        for j in range(1,len(i)):
            totalpoints += pointcounter(i[j-1] +i[j])
        if totalpoints < best:
            best = totalpoints
            d = i
    print best, d
