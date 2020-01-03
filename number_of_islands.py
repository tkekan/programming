
def outOfBounds(matrix, row,col):
    if row >= len(matrix) or row < 0 or col >= len(matrix[0]) or col < 0:
        return False
    return True


def dfs(matrix, row, col):  
    
    #print row,col
    if not outOfBounds(matrix, row, col):
        return
    if matrix[row][col] == 0 or matrix[row][col] == '#':
        return 
    
    matrix[row][col] = '#'
    
    return (dfs(matrix, row ,col+1) or dfs(matrix, row , col -1) or 
            dfs(matrix, row+1, col) or dfs(matrix, row-1, col) or 
            dfs(matrix, row+1, col+1) or dfs(matrix, row-1,col-1) or
            dfs(matrix, row+1, col-1) or dfs(matrix, row-1,col+1))
    


def findConnected(matrix, m, n):
    count = 0
    #print matrix
    for row in range(0,m):
        for col in range(0,n):
            if matrix[row][col] == 1:
                count += 1
                dfs(matrix, row, col)
            
    for r in range(0, m):
        for c in range(0, n):
            if matrix[r][c] == '#':
                matrix[r][c] = 1
        
    return count

matrix = [
 [1, 0, 1, 0, 0, 0],
 [0, 0, 0, 0, 1, 1], 
 [1, 0, 1, 0, 0, 0],
 [0, 0, 0, 0, 1, 0]
]

print findConnected(matrix, len(matrix),len(matrix[0]))

