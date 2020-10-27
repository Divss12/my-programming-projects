'''
Graph format:
{
    nodename = [[outgoing connections],explored bool,leader,finishing time]
}
'''

graph = {
    1 : [[7],False,None,None],
    2 : [[5],False,None,None],
    3 : [[9],False,None,None],
    4 : [[1],False,None,None],
    5 : [[8],False,None,None],
    6 : [[3,8],False,None,None],
    7 : [[4,9],False,None,None],
    8 : [[2],False,None,None],
    9 : [[6],False,None,None]
}
n = len(graph)

def graph_rev(graph):
    out = {}
    for k,v in graph.items():
        for i in v[0]:
            if i in out.keys():
                out[i][0].append(k)
            else:
                out[i] = [[k]] + graph[i][1:]
    return out

def DFSloop(graph,n):

    s,t = [], []
    
    def DFS(graph,i):
            
        graph[i][1] = True 
        graph[i][2] = s[-1]
        
        for j in graph[i][0]:
            if not graph[j][1]:
                DFS(graph,j)
        t.append(1)
        graph[i][3] = len(t)
    
    for i in range(n,0,-1):
        if not graph[i][1]:
            s.append(i)
            DFS(graph,i)
 
    
abc = graph_rev(graph)
DFSloop(abc,n)
print(abc)
print(graph_rev(abc))
            