'''
graph = {
    nodename = [[outgoing connection 1,distance] , [outgoing connection 2,distance] , ...]
}
'''

def dijkstra(graph,s):
    t = set(list(graph.keys()))
    X = [s]
    A = {s: 0}
    B = {s: [s]}
    while set(X) != t:
        v = [None,None]
        d = 1000000000
        for i in X:
            for j in graph[i]:
                if j[0] not in X:
                    if A[i] + j[1] < d:
                        v = [i,j[0]]
                        d = A[i] + j[1]
                        
        X.append(v[1])
        A[v[1]] = d
        B[v[1]] = B[v[0]] + [v[1]]
    
    return [X,A,B]

graph = {}

with open('dijkstraData.txt','r') as f:
    for line in f:
        data = line.split('\t')[:-1]
        graph[int(data[0])] = [[int(j) for j in i.split(',')] for i in data[1:]]

ABC = dijkstra(graph,1)[1]
L = [7,37,59,82,99,115,133,165,188,197]

for i in L:
    print(i,ABC[i])
