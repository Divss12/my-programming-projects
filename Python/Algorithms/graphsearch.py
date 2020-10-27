"""
GRAPH FORMAT:
{nodename = [edges to other nodes]}

nodename contains tail(s); while the list contains the head(s) ((for a directed graph))
for an undirected graph, there would be tails and heads on either side of the edge
"""

graph1 = {
    0: [1],
    1: [0,2,3],
    2: [1,4],
    3: [1,7],
    4: [2,5,6],
    5: [4],
    6: [4,7],
    7: [3,6,8,9],
    8: [7],
    9: [7]
}


def bfsearch(graph,s,t):
    expl = {0: s}
    q = [s]
    i = 0
    while q != []:
        i += 1
        v = q.pop(0)
        for w in graph[v]:
            if w not in expl.values():
                expl[i] = w
                q.append(w)         
                
def dfsearch(graph,s):
    expl = [s]
    q = [s]
    i = 0
    while q != []:
        i += 1
        v = q.pop(-1)
        for w in graph[v]:
            if w not in expl:
                expl.append(w)
                q.append(w)
                
def dfswrapper(graph,s):
    expl = []        
    def dfsearchrec(graph,s):
        expl.append(s)
        for i in graph[s]:
            if i not in expl:
                dfsearchrec(graph,i)
    dfsearchrec(graph,s)
    
def revgraph(graph):
    outgraph = {}
    for k,v in graph.items():
        for i in v:
            if i in outgraph.keys():
                outgraph[i].append(k)
            else:
                outgraph[i] = [k]
    return outgraph