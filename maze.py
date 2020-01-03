def dfs(maze, st, dest):
        if (st[0] == dest[0] and st[1] == dest[1]):
            return True
        
        if (st[0] < 0 or st[0] >= len(maze) or st[1] < 0 or st[1] >= len(maze[0]) or maze[st[0]][st[1]] == 1):
            return False
        
        maze[st[0]][st[1]] = -1
        dirs = [[0,1],[0,-1],[1,0],[1,0]]
        for p in dirs: 
            r = p[0]
            c = p[1]
            nextr = st[0] + r
            nextc = st[1] + c
            changed = False
            while (0 <= nextc < len(maze[0]) and 0 <= nextr < len(maze) and 
                   maze[nextr][nextc] != -1 and maze[nextr][nextc] != 1):
                maze[nextr][nextc] = -1
                nextr += r
                nextc += c
                changed = True
            if changed:    
                if dfs(maze,[nextr-r,nextc-c],dest):
                    return True
        return False
    
        
def hasPath(maze, start, destination):
    """
    :type maze: List[List[int]]
    :type start: List[int]
    :type destination: List[int]
    :rtype: bool
    """
    return dfs(maze, start, destination)


maze = [[0,0,0,0,1,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,1,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,1],[0,0,0,0,1,0,0]]
st = [0,0]
dest = [8,6]
print hasPath(maze,st,dest)

