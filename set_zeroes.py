def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    
    rows = len(matrix)
    cols = len(matrix[0])

    
    for r in range(0,rows):
	for c in range(0,cols):
	    if matrix[r][c] == 0:
		matrix[r] = [0 for x in range(0,cols)]
		if rows > 1:
		    transpose_m = zip(*matrix)
		    transpose_m[c] = [0 for x in range(0,rows)]
 	            if len(transpose_m) > 1:
		        matrix = zip(*transpose_m)
		    else:
			matrix = [[x] for x in transpose_m[0]]
    print matrix

matrix = [[1,2,3,4],[4,5,6,7],[9,8,0,1]]
matrix = setZeroes(matrix)
