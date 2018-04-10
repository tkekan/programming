from collections import defaultdict


def dfshelper(self,vertex,visited, stack):
    visited[vertex] = True
    stack.append(vertex)
    for val in self.V[vertex]:
        if visited[val] == False:
            dfshelper(self,val,visited, stack)    

class graph():
    def __init__(self):
        self.V = defaultdict(list)
    def addEdge(self,v,e):
        self.V[v].append(e)
    def dfs(self):
        stack = []
        visited = {x:False for x in self.V}
        for i in self.V:
            if not visited[i]:
                dfshelper(self,i,visited,stack)
        print stack

g = graph()
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,1)
g.addEdge(2,3)
g.addEdge(2,4)
g.addEdge(3,1)
g.addEdge(3,2)
g.addEdge(3,5)
g.addEdge(4,2)
g.addEdge(4,5)
g.addEdge(5,4)
g.addEdge(5,3)
g.dfs()



