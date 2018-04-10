



def findPath(matrix, r, c, ROWS, COLS):
    if r > ROWS - 1 or r < 0 or c > COLS - 1 or c < 0:
        return False
    print "path %d,%d" %(r,c)
    if r == ROWS - 1 and c == COLS - 1:
        return True
    visited[r][c] = True
    if (matrix[r][c] == 0  and
        ( matrix[r][c+1] == 0 and not visited[r][c+1] and findPath(matrix, r, c + 1, ROWS, COLS)) or
        ( matrix[r + 1][c] == 0 and not visited[r+1][c] and findPath(matrix, r + 1, c, ROWS, COLS)) or
        ( matrix[r - 1][c] == 0 and not visited[r-1][c] and findPath(matrix, r - 1, c , ROWS, COLS)) or
        ( matrix[r - 1][c - 1] == 0 and not visited[r - 1][c - 1] and findPath(matrix, r - 1, c - 1, ROWS, COLS)) or
        ( matrix[r + 1][c - 1] == 0 and not visited[r + 1][c - 1] and findPath(matrix, r + 1, c - 1, ROWS, COLS)) or
        ( matrix[r + 1][c+1] == 0 and not visited[r + 1][c+1] and findPath(matrix, r + 1, c + 1, ROWS, COLS)) or
        ( matrix[r - 1][c - 1] == 0 and not visited[r - 1][c - 1] and findPath(matrix, r - 1, c - 1, ROWS, COLS)) or
        ( matrix[r - 1][c + 1] == 0 and not visited[r - 1][c + 1] and findPath(matrix, r - 1, c + 1, ROWS, COLS))):
        return True
    else:
        return False



ROWS = 4
COLS = 4
matrix = [[0,1,1,0], [0,0,1,0], [1,1,0,1], [0,0,0,0]]
visited = [[False for x in range(0, 4)] for y in range(0,4)]
val = findPath(matrix, 0, 0, ROWS, COLS)    
print val
