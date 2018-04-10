
"""
def maxpath(array, row, col):
    rows = len(array)
    cols = len(array[0])
    tc = [[0 for x in range(1,rows + 1) for y in range(1,cols + 1)]

    for r in range(1,len(array) + 1):
    for c in range(1,len(array[0]) + 1):
"""			

'''
    This function finds if the row and columns are 
    out of range
'''
def outrange(r,c, rows, cols):
    if r > rows or c < 0 or c > cols:
		return 1
    else:
    	return 0

'''
    This function recursively finds the maximum path starting from position (p,q) within the board
    It uses mnemo as the mnemonization technique to store the subproblems that might be calculated 
    in some other paths while fidning the maximum path
'''
def recursiveMaxPaths(array, r, c, rows, cols, mnemo):
    if outrange(r,c,rows,cols):
	return 0
    leftdown,rightdown,centerdown = 0,0,0

    value = array[r][c]
    if not outrange(r+1,c-1,rows,cols):
        if mnemo[r+1][c-1] == -1:
            leftdown = recursiveMaxPaths(array,r+1,c-1,rows,cols, mnemo)
            mnemo[r+1][c-1] = leftdown
        else:
            leftdown = mnemo[r+1][c-1]
    else:
        leftdown = 0

    if not outrange(r+1,c+1,rows,cols):
        if mnemo[r+1][c+1] == -1:
            rightdown = recursiveMaxPaths(array,r+1,c+1,rows,cols, mnemo)
            mnemo[r+1][c+1] = rightdown
        else:
            rightdown = mnemo[r+1][c+1]
    else:
        rightdown = 0

    if not outrange(r+1,c,rows,cols):
        if mnemo[r+1][c] == -1:
            centerdown = recursiveMaxPaths(array,r+1,c,rows,cols, mnemo)
            mnemo[r+1][c] = centerdown
        else:
            centerdown = mnemo[r+1][c]
    else:
        centerdown = 0
	
    mnemo[r][c] = value + max(leftdown, rightdown, centerdown)
    return mnemo [r][c]

'''
    This function in the starting function that does some error checking and calls the
    recursiveMaxPaths to return the path which is having the maximum sum
'''
def maxPath(board, p, q):
    if not board or not board[0]:
        return 0
    ROWS = len(board)
    COLUMNS = len(board[0])
    if outrange(p,q,ROWS,COLUMNS):
	print "Error!..Starting point is out of range!"
	return 1
    mnemo = [[-1 for x in range(0,COLUMNS)] for y in range(0,ROWS)]
    value = recursiveMaxPaths(board, p, q, len(board) - 1, len(board[0]) - 1, mnemo)
    return value
	
#array = [[1,2,3,4],[5,6,7,8],[9,0,0,1]]
array = [[1,2,3,4]]
#array = [[1,2,3,4],[5,6,7,8],[9,0,0,1]]
#array = [[1,2,3,4],[5,6,7,8],[9,0,0,1],[10,100,1,1]]
#array = [[]]

value = maxPath(array, 0, 1)
print "The sum of path with maximum value is %d" % value
