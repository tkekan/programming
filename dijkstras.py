from collections import defaultdict


class Graph():
    def __init__(q, V):
        q.d = defaultdict(list)
        q.V = V

    def addE(q, v,u,w):
        q.d[v].append((u,w))

    def minD(q, dist, setv):
        min = float('inf')
        for v in range(0,q.V):
            if not setv[v] and dist[v] < min:
                minV = v
                min = dist[v]

        return minV
    def dijkstras(q,s):
        setv = [False] * q.V
        distance = [float('inf')] * q.V
        distance[s] = 0
        for count in range(0, q.V):
            u = q.minD(distance, setv)
            setv[u] = True
            for updateV,weight in q.d[u]:
                if not setv[updateV] and distance[updateV] > weight + distance[u]:
                    distance[updateV] = weight + distance[u]
        print distance

g = Graph(9)
g.addE(0,1,4)
g.addE(0,7,8)
g.addE(1, 0, 4)
g.addE(1, 2, 8)
g.addE(1, 7, 11)
g.addE(2, 1, 8)
g.addE(2, 3, 7)
g.addE(2,8, 2)
g.addE(2, 5, 4)
g.addE(3, 2, 7)
g.addE(3,4,9)
g.addE(3, 5, 14)
g.addE(4, 3, 9)
g.addE(4,5, 10)
g.addE(5,2,4)
g.addE(5,3,14)
g.addE(5, 4, 10)
g.addE(5,6,2)
g.addE(6, 5, 2)
g.addE(6,8,6)
g.addE(6,7,1)
g.addE(7,0,8)
g.addE(7,1,11)
g.addE(7,8,7)
g.addE(7,6,1)
g.addE(8,2,2)
g.addE(8,7,7)
g.addE(8,6,6)
g.dijkstras(0)
