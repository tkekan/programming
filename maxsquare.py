def maximalSquare( matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    maxsq = 0
    rows = len(matrix)
    cols = len(matrix[0])
   
    
    dp = [[0 for y in range(0,cols)] for x in range(0,rows)]
    dp[0] = matrix[0]
   
    for y in range(0, rows):
        dp[y][0] = matrix[y][0]
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 1:
                dp[i][j] = min(int(dp[i-1][j-1]), int(dp[i-1][j]), int(dp[i][j-1])) + 1
                maxsq = max(maxsq, dp[i][j])
    return maxsq * maxsq

#matrix = ["10100","10111","11111","10010"]
matrix = [[1,0,1,0,0],
          [1,0,0,1,1],
          [1,1,1,1,1],
          [1,0,1,1,1]]
ret = maximalSquare(matrix)
print ret
