def isBipartite(graph):
    """
    :type graph: List[List[int]]
    :rtype: bool
    """
    colors = [0] * len(graph)
    src = 0
    colors[src] = 1
    
    for i in range(0,len(graph)):
        for j in range(0,len(graph[i])):
            if colors[graph[i][j]] == 0:
                colors[graph[i][j]] = ~colors[i]
            elif colors[graph[i][j]] == colors[i]:
                return False
    return True

graph = [[1,3], [0,2], [1,3], [0,2]]
print isBipartite(graph)
