import random

graph1 = {
    0: [1,3,9],
    1: [0,2,4],
    2: [1,3,6,4],
    3: [0,2,7],
    4: [1,2,5,7],
    5: [4,7,9],
    6: [2,8],
    7: [3,4,5,8,9],
    8: [6,7],
    9: [0,5,7]
}

graph2 = {}
temp = 0

with open('kargerMinCut.txt','r') as f:
    for l in f:
        k = list(map(int,l.strip().split('\t')))
        graph2[k[0]] = k[1:]

defg = 17
for i in range(100):
    def randcont(graph):
        while len(graph) > 2:

            a = list(graph.keys())[random.randrange(0,len(list(graph.keys())))]
            b = graph[a][random.randrange(0,len(graph[a]))]        
            
            graph[a] += graph[b]
            graph.pop(b)
            for k,v in graph.items():
                if k == a:
                    graph[k] = [i for i in graph[k] if i != a and i != b]
                else:
                    for i,j in enumerate(v):
                        if j == b:
                            graph[k][i] = a

        return graph 

    abc = randcont(graph2)
    hijk = len(abc[list(abc.keys())[0]])
    if hijk < defg:
        print(hijk)
        defg = hijk